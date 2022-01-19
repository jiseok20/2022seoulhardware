import socket
import cv2
import pickle
import struct
import argparse
import json
import logging
import serial
import threading
import time
import smtplib, imaplib, os
import email
from email.header import decode_header, make_header
from email.message import EmailMessage
import sys

def send_mail(receive_data):
    if receive_data == b'2':
        id_ = 'your email'
        pw = 'your password'
        subject = EmailMessage()
        subject['From'] = '똘기'
        subject['To'] = 'semhappy@naver.com'
        subject['Subject'] = '[똘기] 경고!!'
        subject.set_content('움직이지 않아요')
        mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mail.login(id_, pw)
        mail.send_message(subject)
        mail.quit()

ip = ''  # ip 주소
port = 50001  # port 번호

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 객체를 생성
s.bind((ip, port))  # 바인드(bind) : 소켓에 주소, 프로토콜, 포트를 할당
s.listen(10)  # 연결 수신 대기 상태(리스닝 수(동시 접속) 설정)
print('클라이언트 연결 대기')

# 연결 수락(클라이언트 소켓 주소를 반환)
conn, addr = s.accept()
print(addr)  # 클라이언트 주소 출력

a = serial.Serial(port='COM10', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE
                    ,timeout=0, bytesize=serial.EIGHTBITS)

data = b""  # 수신한 데이터를 넣을 변수
payload_size = struct.calcsize(">L")

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to image or video. Skip to capture frames from camera')
parser.add_argument('--thr', default=0.2, type=float, help='Threshold value for pose parts heat map')
parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

args = parser.parse_args()

BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
              "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
              ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
              ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]

inWidth = args.width
inHeight = args.height

net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

while True:
    # 프레임 수신
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # 역직렬화(de-serialization) : 직렬화된 파일이나 바이트를 원래의 객체로 복원하는 것
    frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")  # 직렬화되어 있는 binary file로 부터 객체로 역직렬화
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # 프레임 디코딩

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    net.setInput(
        cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert (len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv2.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > args.thr else None)
    X = 0
    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert (partFrom in BODY_PARTS)
        assert (partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            POINTX = []
            num = 0
            for i in range(0, 18):
                if points[i] != None:
                    POINTX.append(points[i][0])
                    num += 1
            if num == 0:
                X = 0
            elif (num >= 1) and (num <= 4):
                X = 1
            else:
                X = sum(POINTX) / num - frameWidth / 2
                X = (X + 320) / 91 + 2
    X = int(X)
    print(X)
    cv2.imshow("a", frame)
    a.write(bytes((str(X)), 'utf-8'))
    t, _ = net.getPerfProfile()
    freq = cv2.getTickFrequency() / 1000
    receive_data = a.read()  # serial에 출력되는 데이터를 읽어준다.
    send_warning = threading.Thread(target=send_mail(receive_data))
    send_warning.start()
    # 1초 마다 키 입력 상태를 받음
    if cv2.waitKey(1) == ord('q'):  # q를 입력하면 종료
        break