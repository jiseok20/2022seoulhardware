import sys
import numpy as np
import cv2
import time
from  PIL import Image
import random
import copy
import pygame

oldx=oldy=-1
count=0
image1 = cv2.imread("2.jpg",cv2.IMREAD_COLOR)
image2 = cv2.imread("3.jpg", cv2.IMREAD_COLOR)
image3 = cv2.imread("4.jpg", cv2.IMREAD_COLOR)
image4 = cv2.imread("5.jpg", cv2.IMREAD_COLOR)
image5 = cv2.imread("6.jpg", cv2.IMREAD_COLOR)
image6 = cv2.imread("7.jpg", cv2.IMREAD_COLOR)
image7 = cv2.imread("8.jpg", cv2.IMREAD_COLOR)
image8 = cv2.imread("9.jpg", cv2.IMREAD_COLOR)
image9 = cv2.imread("10.jpg", cv2.IMREAD_COLOR)
image10 = cv2.imread("11.jpg", cv2.IMREAD_COLOR)
image11 = cv2.imread("12.jpg", cv2.IMREAD_COLOR)
image12 = cv2.imread("13.jpg", cv2.IMREAD_COLOR)
image13 = cv2.imread("14.jpg", cv2.IMREAD_COLOR)
image14 = cv2.imread("15.jpg", cv2.IMREAD_COLOR)
image15 = cv2.imread("16.jpg", cv2.IMREAD_COLOR)
image16 = cv2.imread("17.jpg", cv2.IMREAD_COLOR)
image17 = cv2.imread("18.jpg", cv2.IMREAD_COLOR)
image18 = cv2.imread("19.jpg", cv2.IMREAD_COLOR)
image19 = cv2.imread("20.jpg", cv2.IMREAD_COLOR)
image20 = cv2.imread("21.jpg", cv2.IMREAD_COLOR)
image21 = cv2.imread("23.jpg", cv2.IMREAD_COLOR)
image22 = cv2.imread("24.jpg", cv2.IMREAD_COLOR)
image23 = cv2.imread("25.jpg", cv2.IMREAD_COLOR)
image24 = cv2.imread("26.jpg", cv2.IMREAD_COLOR)
image25 = cv2.imread("27.jpg", cv2.IMREAD_COLOR)
image26 = cv2.imread("28.jpg", cv2.IMREAD_COLOR)
image27 = cv2.imread("29.jpg", cv2.IMREAD_COLOR)
image28 = cv2.imread("30.jpg", cv2.IMREAD_COLOR)
image29 = cv2.imread("31.jpg", cv2.IMREAD_COLOR)
image30 = cv2.imread("32.jpg", cv2.IMREAD_COLOR)
image31 = cv2.imread("33.jpg", cv2.IMREAD_COLOR)
image32 = cv2.imread("34.jpg", cv2.IMREAD_COLOR)
image33 = cv2.imread("35.jpg", cv2.IMREAD_COLOR)
image34 = cv2.imread("36.jpg", cv2.IMREAD_COLOR)
image35 = cv2.imread("37.jpg", cv2.IMREAD_COLOR)
image36 = cv2.imread("38.jpg", cv2.IMREAD_COLOR)
image37 = cv2.imread("39.jpg", cv2.IMREAD_COLOR)
def SOUND(voice):
    #player=pygame.mixer.Sound(voice)
    pygame.mixer.init()
    pygame.mixer.music.load(voice)
    pygame.mixer.music.play()
    #player.play()
    #time.sleep(2.0)
    #player.stop()

def imshow_fullscreen(winname,img):
    cv2.namedWindow(winname, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(winname,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow(winname,img)
def READ_COLOR():
    imshow_fullscreen("READ_COLOR",image1)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("READ_COLOR", image2)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("READ_COLOR", image3)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("READ_COLOR", image4)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("READ_COLOR", image5)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("READ_COLOR", image6)
    SOUND("글자의 색을 읽어보세요.mp3")
    cv2.waitKey(5000)
    cv2.destroyWindow("READ_COLOR")
def BRAIN_TEST():
    imshow_fullscreen("BRAIN_TEST", image7)
    SOUND("사진을 기억하세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("BRAIN_TEST", image8)
    SOUND("빨간 낙엽의 개수는.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("BRAIN_TEST", image9)
    cv2.waitKey(5000)
    imshow_fullscreen("BRAIN_TEST", image10)
    SOUND("사진을 기억하세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("BRAIN_TEST", image11)
    SOUND("학은 무엇을 바라보고 있나요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("BRAIN_TEST", image12)
    cv2.waitKey(5000)
    cv2.destroyWindow("BRAIN_TEST")
def INIT_GAME():
    imshow_fullscreen("INIT_GAME", image13)
    SOUND("동물 이름을 맞춰보세요.mp3")
    cv2.waitKey(20000)
    imshow_fullscreen("INIT_GAME", image14)
    cv2.waitKey(10000)
    imshow_fullscreen("INIT_GAME", image15)
    SOUND("과일 이름을 맞춰보세요.mp3")
    cv2.waitKey(20000)
    imshow_fullscreen("INIT_GAME", image16)
    cv2.waitKey(10000)
    cv2.destroyWindow("INIT_GAME")
def PROVERB():
    imshow_fullscreen("PROVERB", image17)
    SOUND("속담의 빈칸을 채워보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("PROVERB", image18)
    SOUND("clap.mp3")
    cv2.waitKey(3000)
    imshow_fullscreen("PROVERB", image19)
    SOUND("속담의 빈칸을 채워보세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("PROVERB", image20)
    SOUND("clap.mp3")
    cv2.waitKey(3000)
    cv2.destroyWindow("PROVERB")
def SECRET():
    name = cv2.imread("22.jpg",cv2.IMREAD_COLOR)
    imshow_fullscreen("MAKERS",name)
    cv2.waitKey(5000)
    cv2.destroyWindow("MAKERS")
def  ROCK_PAPER_SCISSORS():
    imshow_fullscreen("ROCK_PAPER_SCISSORS", image25)
    SOUND("1.mp3")
    cv2.waitKey(2000)
    imshow_fullscreen("ROCK_PAPER_SCISSORS", image26)
    SOUND("2.mp3")
    cv2.waitKey(2000)
    imshow_fullscreen("ROCK_PAPER_SCISSORS", image27)
    SOUND("3.mp3")
    cv2.waitKey(2000)
    n = random.randint(0,2)
    if n == 0:
        imshow_fullscreen("ROCK_PAPER_SCISSORS", image28)
        SOUND("clap2.MP3")
        cv2.waitKey(5000)
    elif n==1:
        imshow_fullscreen("ROCK_PAPER_SCISSORS", image29)
        SOUND("clap2.MP3")
        cv2.waitKey(5000)
    elif n==2:
        imshow_fullscreen("ROCK_PAPER_SCISSORS", image30)
        SOUND("clap2.MP3")
        cv2.waitKey(5000)
    cv2.destroyWindow("ROCK_PAPER_SCISSORS")
def MATH_PROBLEM():
    imshow_fullscreen("MATH_PROBLEM", image31)
    SOUND("연산을 하세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("MATH_PROBLEM", image32)
    SOUND("clap.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("MATH_PROBLEM", image33)
    SOUND("연산을 하세요.mp3")
    cv2.waitKey(5000)
    imshow_fullscreen("MATH_PROBLEM", image34)
    SOUND("clap.mp3")
    cv2.waitKey(5000)
    cv2.destroyWindow("MATH_PROBLEM")
def QUIZ():
    imshow_fullscreen("QUIZ", image35)
    SOUND("다음 나오는 질문에 편하게 대답해주세요.mp3")
    cv2.waitKey(5000)
    n = random.randint(0, 1)
    if n == 0:
        imshow_fullscreen("QUIZ", image36)
        SOUND("가장 최근에 만난 사람은 누구신가요.mp3")
        cv2.waitKey(5000)
    elif n == 1:
        imshow_fullscreen("QUIZ", image37)
        SOUND("집전화와 휴대전화.mp3")
        cv2.waitKey(5000)
    cv2.destroyWindow("QUIZ")
def FIND_WRONG_PICTURE():
    global count
    n = random.randint(0, 1)
    new = copy.deepcopy(image21)
    new2=copy.deepcopy(image23)
    if n == 0:
        imshow_fullscreen("FIND_WRONG_PICTURE", image21)
        SOUND("두 그림의 다른 점을 7개 찾아보세요.mp3")
        cv2.setMouseCallback('FIND_WRONG_PICTURE', on_mouse2, new)
    elif n == 1:
        imshow_fullscreen("FIND_WRONG_PICTURE", image23)
        SOUND("당근지팡이팽이음표옷걸이.mp3")
        cv2.setMouseCallback('FIND_WRONG_PICTURE', on_mouse3, new2)
    cv2.waitKey()
def on_mouse(event,x,y,flags,param):
    global oldx,oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx,oldy = x,y
        if 0<x<266 and 0<y<160:
            READ_COLOR()
            SOUND("click.mp3")
        elif 267<x<532 and 0<y<160:
            BRAIN_TEST()
            SOUND("click.mp3")
        elif 533<x<800 and 0<y<160:
            INIT_GAME()
            SOUND("click.mp3")
        elif 0<x<266 and 161<y<320:
            PROVERB()
            SOUND("click.mp3")
        elif 267<x<532 and 161<y<320:
            SECRET()
            SOUND("click.mp3")
        elif 533<x<800 and 161<y<320:
            FIND_WRONG_PICTURE()
            SOUND("click.mp3")
        elif 0<x<266 and 321<y<480:
            ROCK_PAPER_SCISSORS()
            SOUND("click.mp3")
        elif 267<x<532 and 321<y<480:
            MATH_PROBLEM()
            SOUND("click.mp3")
        elif 533<x<800 and 321<y<480:
            QUIZ()
            SOUND("click.mp3")
def on_mouse2(event,x,y,flags,param):
    global oldx, oldy
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        if (92 - 20 < x < 92 + 20 or 92 + 345 - 20 < x < 92 + 345 + 20) and 145 - 20 < y < 145 + 20:
            cv2.circle(param, (92, 145), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (92+ 345, 145), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (257 - 20 < x < 257 + 20 or 257 + 345 - 20 < x < 257 + 345 + 20) and 187 - 20 < y < 187 + 20:
            cv2.circle(param, (257, 187), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (257 + 345, 187), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (65 - 20 < x < 65 + 20 or 65 + 345 - 20 < x < 65 + 345 + 20) and 322 - 20 < y < 322 + 20:
            cv2.circle(param, (65, 322), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (65 + 345, 322), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (221 - 20 < x < 221 + 20 or 221 + 345 - 20 < x < 221 + 345 + 20) and 405 - 20 < y < 405 + 20:
            cv2.circle(param, (221, 405), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (221 + 345, 405), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (260 - 20 < x < 260 + 20 or 260 + 345 - 20 < x < 260 + 345 + 20) and 382 - 20 < y < 382 + 20:
            cv2.circle(param, (260, 382), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (260 + 345, 382), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (361 - 20 < x < 361 + 20 or 361 + 345 - 20 < x < 361 + 345 + 20) and 216 - 20 < y < 216 + 20:
            cv2.circle(param, (361, 216), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (361 + 345, 216), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (336 - 20 < x < 336 + 20 or 336 + 345 - 20 < x < 336 + 345 + 20) and 135 - 20 < y < 135 + 20:
            cv2.circle(param, (336, 135), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (336 + 345, 135), 20, (0, 255, 0), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
    if count == 7:
        cv2.destroyWindow('FIND_WRONG_PICTURE')
        count = 0
        imshow_fullscreen("FIND_WRONG_PICTURE", image22)
        SOUND("wow2.mp3")
        cv2.waitKey(5000)
        cv2.destroyWindow('FIND_WRONG_PICTURE')
def on_mouse3(event,x,y,flags,param):
    global oldx, oldy
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        if (560 - 20 < x < 560 + 20) and 120 - 20 < y < 120 + 20:
            cv2.circle(param, (x, y), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (94, 36), 20, (0, 0, 255), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (208 - 20 < x < 208 + 20) and 273 - 20 < y < 273 + 20:
            cv2.circle(param, (x, y), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (465, 36), 20, (0, 0, 255), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (212 - 20 < x < 212 + 20) and 390 - 20 < y < 390 + 20:
            cv2.circle(param, (x, y), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (187, 36), 20, (0, 0, 255), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (569 - 20 < x < 569 + 20) and 376 - 20 < y < 376 + 20:
            cv2.circle(param, (x, y), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (285, 36), 20, (0, 0, 255), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
        elif (600 - 20 < x < 600 + 20) and 292 - 20 < y < 292 + 20:
            cv2.circle(param, (x, y), 20, (0, 255, 0), thickness=2)
            cv2.circle(param, (370, 36), 20, (0, 0, 255), thickness=2)
            SOUND("wow.mp3")
            imshow_fullscreen('FIND_WRONG_PICTURE', param)
            count = count + 1
    if count == 5:
        cv2.destroyWindow('FIND_WRONG_PICTURE')
        count = 0
        imshow_fullscreen("FIND_WRONG_PICTURE", image24)
        SOUND("wow2.mp3")
        cv2.waitKey(5000)
        cv2.destroyWindow('FIND_WRONG_PICTURE')
main_img = cv2.imread("1.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow('MAIN_HOME', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('MAIN_HOME',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('MAIN_HOME',on_mouse,main_img)
cv2.imshow('MAIN_HOME',main_img)
cv2.waitKey()
cv2.destroyAllWindows()