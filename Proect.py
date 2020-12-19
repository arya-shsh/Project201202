# подключаем модули
import pygame
import sys
import random
from shapes import *
import math
def draw_smile(sc,c): #рисуем смайлик
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    pygame.draw.circle(sc, c.color, (c.x, c.y), c.r) #рисуем кружочки
    pygame.draw.circle(sc, color, ((c.x - c.r//2), (c.y - c.r//2)), c.r//6) #рисуем глаза левый
    pygame.draw.circle(sc, color, ((c.x + c.r//2), (c.y - c.r//2)), c.r//6) #рисуем глаза правый
    pygame.draw.arc(sc,color,((c.x - 2*c.r//3),(c.y - c.r//6),(4*c.r//3),(c.r)),math.pi,2*math.pi,3) #рисуем улыбку
def reflection(c): #отражение от стенок
    global max_w, max_h
    if c.x - c.r <= 0:
        c.vx = 1
    if c.y - c.r <= 0:
        c.vy = 1
    if c.x + c.r >= max_w:
        c.vx = -1
    if c.y + c.r >= max_h:
        c.vy = -1
def draw_rect(sc,i): #рисуем прямоуг
    pygame.draw.rect(sc,i.color,(i.x,i.y,i.w,i.h))
def reflection_rect(c):#отражение прямоуг от краёв
    if c.x == 0:
        c.vx = 1
    if c.y == 0:
        c.vy = 1
    if c.x + c.w >= max_w:
        c.vx = -1
    if c.y + c.h >= max_h:
        c.vy = -1
# определяем константы,
# классы и функции
FPS = 60
PINK = (255, 110, 199)
YELLOW = (252, 247, 135)
max_w = 600
max_h = 400
min_r = 10
max_r = 60
max_circles = 13
count = 0
circles = []
rects = []
press = (0,0)
speed = 2 #cкорость,чем меньше значение, тем быстрее движении
counter = 0
max_rect = 10
min_w = 34
min_h = 34
max_wr = 50
max_hr = 50
count_rect = 0
# инициация,
# создаем объектов
pygame.init() #инициализация модуля игры
sc = pygame.display.set_mode((max_w, max_h))
clock = pygame.time.Clock()
# для отображения до цикла
# какиех-то объектов, обновляем экран
pygame.display.update() #первоначальное обновление экрана
# главный цикл
while True:#основной цикл игры
    # задержка
    clock.tick(FPS)
    # цикл для обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            press = i.pos
    # изменяем объекты
    # обновляем экран
    sc.fill(PINK) # заливаем экран розовым
    while count< max_circles:#добавляем круги в список
        x = random.randint(0, max_w)
        y = random.randint(0, max_h)
        r = random.randint(min_r, max_r)
        vx = random.randint (-1,1)
        vy = random.randint(-1,1)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        peresechenie = False
        new = Circle(x,y,r,color,vx,vy)
        for i in circles:
            if new.peresechenie(i):
                peresechenie = True
        if not peresechenie:
            circles.append(new) # сохраняем созданные круги в списке
            count += 1
    while count_rect < max_rect: #создаем прямоуг в список
        x = random.randint(0, max_w)
        y = random.randint(0, max_h)
        w = random.randint(min_w, max_wr)
        h = random.randint(min_h,max_hr)
        vx = random.randint(-1,1)
        vy = random.randint(-1,1)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        new = Rect(x,y,w,h,color,vx,vy)
        rects.append(new)
        count_rect += 1
    for i in circles: #проверяем нажатие на круг
        if (press[0]-i.x)**2+(press[1]-i.y)**2<= i.r**2: #проверяем принадлежность координат нажатия координатам круга
            circles.remove(i)
            count-=1 #вместо осчезнувшего круга добавляем новый
    for i in rects: #проверяем нажатие на прямоугольник
        if (i.x <= press[0]<= i.x + i.w) and (i.y <= press[1] <= i.y + i.h):
            rects.remove(i)
            count_rect -= 1
    if counter % speed == 0: #скорость движения
        for i in circles: #добавили движение
            i.x += i.vx
            i.y += i.vy
            reflection(i)
        for i in rects:
            i.x += i.vx
            i.y += i.vy
            reflection_rect(i)
    for i in circles:
        draw_smile(sc,i)
    for i in rects:
        draw_rect(sc,i)
    pygame.display.update()
