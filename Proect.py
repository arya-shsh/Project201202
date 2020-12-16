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
press = (0,0)
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
    for i in circles: #проверяем нажатие на круг
        if (press[0]-i.x)**2+(press[1]-i.y)**2<= i.r**2: #проверяем принадлежность координат нажатия координатам круга
            circles.remove(i)
            count-=1 #вместо осчезнувшего круга добавляем новый
    for i in circles:
        draw_smile(sc,i)
    pygame.display.update()

