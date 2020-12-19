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
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    pygame.draw.rect(sc,i.color,(i.x,i.y,i.w,i.h))
    pygame.draw.aalines(sc, color, False,[[(i.x + i.w//8),(i.y + 3*i.h//4)], [(i.x + i.w//4),(i.y + 5*i.h//8)],[(i.x + 3*i.w//8),(i.y + 3*i.h//4)],[(i.x + i.w//2),(i.y + 5*i.h//8)],[(i.x + 5*i.w//8),(i.y + 3*i.h//4)],[(i.x + 3*i.w//4),(i.y + 5*i.h//8)],[(i.x + 7*i.w//8),(i.y + 3*i.h//4)]],10)
    pygame.draw.rect(sc,BLACK,((i.x + i.w//8),(i.y + i.h//4),i.w//8,i.h//8))
    pygame.draw.rect(sc,BLACK,((i.x + 6*i.w//8),(i.y + i.h//4),i.w//8,i.h//8))
def reflection_rect(c):#отражение прямоуг от краёв
    if c.x == 0:
        c.vx = 1
    if c.y == 0:
        c.vy = 1
    if c.x + c.w >= max_w:
        c.vx = -1
    if c.y + c.h >= max_h:
        c.vy = -1
FPS = 60
RED = (255,0,0)
PINK = (255, 110, 199)
YELLOW = (252, 247, 135)
BLACK = (0,0,0)
LIGHT_PINK = (249, 89, 224)
LIGHT_YELLOW = (231,250,90)
ORANGE = (255,150,100)
max_w = 600
max_h = 400
min_r = 10
max_r = 60
max_circles = 30
count = 0
circles = []
rects = []
press = (0,0)
counter = 0 
speed = 2 #чем меньше значение тем быстрее
max_wr = 50
max_hr = 50
count_rect = 0
max_rect = 20
min_w = 40
min_h = 50
score = 0
game_over = False
in_menu = True
nonzero = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
time = 40*FPS #столько кадров игра
star = pygame.image.load('fon.jpg')
shine = pygame.image.load('myy.jpg')
pygame.init() #инициализация модуля игры
pygame.mixer.music.load('uno.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)
pygame.font.init() #инициализация шрифтов
sc = pygame.display.set_mode((max_w+100, max_h))
clock = pygame.time.Clock()
# для отображения до цикла
# какиех-то объектов, обновляем экран
pygame.display.update() #первоначальное обновление экрана
# главный цикл
while in_menu: #цикл пока находимся в меню
    for i in pygame.event.get():
        if i.type == pygame.QUIT:#обработка выхода
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            press = i.pos
    clock.tick(FPS)
    f1 = pygame.font.Font('C:\Windows\Fonts\RockwellNova.ttf', 26) #шрифт
    text3 = f1.render('Правила игры!', True, (200, 80, 254)) #создает объект
    text1 = f1.render('Играть', True, (26, 215, 250)) #создает объект
    text2 = f1.render('Выход', True, (144, 249, 89)) #создает объект
    sc.blit(star,(0,0))
    pygame.draw.rect(sc,LIGHT_YELLOW,(70,330,105,50)) #прямоугольник кнопки
    pygame.draw.rect(sc,LIGHT_PINK,(540,330,100,50)) #прямоугольник кнопки
    pygame.draw.rect(sc,(200,246,254),(230,13,230,40)) #прямоугольник кнопки
    sc.blit(text1, (74, 335))#отображение на экране
    sc.blit(text2, (549, 335))#отображение на экране
    sc.blit(text3, (240, 15))#отображение на экране
    if 70<=press[0]<=70+105 and 330<= press[1]<=330+50: #нажатие на кнопки в меню
        in_menu = False
    if 540<=press[0]<=540+100 and 330<= press[1]<=330+50:
        in_menu = False
        game_over = True
    pygame.display.update()
while not game_over:#основной цикл игры
    counter += 1
    time -= 1
    if time == 0:
        game_over =True
    clock.tick(FPS)
    for i in pygame.event.get(): # цикл для обработки событий
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            press = i.pos
    sc.blit(shine,(0,0))
    while count< max_circles:#добавляем круги в список
        x = random.randint(0, max_w)
        y = random.randint(0, max_h)
        r = random.randint(min_r, max_r)
        vx = random.randint (-1,1)
        vy = random.randint(-1,1)
        if vx == 0 and vy == 0:
            vx, vy = random.choice(nonzero)
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
        vx = random.randint (-1,1)
        vy = random.randint(-1,1)
        if vx == 0 and vy == 0:
            vx, vy = random.choice(nonzero)
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
            count -= 1 #вместо осчезнувшего круга добавляем новый
            score += 1
    for i in rects: #проверяем нажатие на прямоугольник
        if (i.x <= press[0]<= i.x + i.w) and (i.y <= press[1] <= i.y + i.h):
            rects.remove(i)
            count_rect -= 1
            game_over = True
    press = -100,-100
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
    f3 = pygame.font.Font('C:\WINDOWS\FONTS\ALGER.TTF', 36) #шрифт
    f4 = pygame.font.Font('C:\WINDOWS\FONTS\COURBD.TTF', 20) #шрифт
    text3 = f3.render(str(time//FPS), True, ORANGE) #создает объект
    sc.blit(text3, (650, 50))#отображение на экране
    text4 = f3.render(str(score), True, ORANGE) #создает объект
    sc.blit(text4, (658, 127))#отображение на экране
    text5 = f4.render('Счёт', True, BLACK) #создает объект
    sc.blit(text5, (645, 103))#отображение на экране
    text6 = f4.render('Время', True, BLACK) #создает объект
    sc.blit(text6, (635, 30))#отображение на экране
    pygame.display.update()
print(score)
