# подключаем модули
import pygame
import sys
import random
from shapes import *
import math


max_w = 600
max_h = 400
min_r = 10
max_r = 60
max_wr = 50
max_hr = 50
min_w = 40
min_h = 50
FPS = 60
ORANGE = (255,150,100)
BLACK = (0,0,0)
PINK = (254,38,152)
PURLE = (69,15,89)
YELLOW = (252, 247, 135)
LIGHT_PURLE = (122,1,178)
max_circles = 30
max_rect = 20
circles = []
rects = []

def draw_smile(sc,c, red, green, blue): #рисуем смайлик
    """Метод для прорисовки круглых смайлов в игре
    :param sc: отображение рабочей области
    :param c: переменная, которая отражает конкретный круг
    :return: None
    """
    color = (red, green, blue)
    for colors in color:
        if 256 < colors < 0:
            raise ValueError('Color shold be set in range 0-255')
    pygame.draw.circle(sc, c.color, (c.x, c.y), c.r) #рисуем кружочки
    pygame.draw.circle(sc, color, ((c.x - c.r//2), (c.y - c.r//2)), c.r//6) #рисуем глаза левый
    pygame.draw.circle(sc, color, ((c.x + c.r//2), (c.y - c.r//2)), c.r//6) #рисуем глаза правый
    pygame.draw.arc(sc,color,((c.x - 2*c.r//3),(c.y - c.r//6),(4*c.r//3),(c.r)),math.pi,2*math.pi,3) #рисуем улыбку

def reflection(c): #отражение от стенок
    """Метод для осуществления отржаения круглых смайлов от границ рабочей области
    :param c: переменная, которая отражает конкретный круг
    :return: None
    """
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
    """Метод для прорисовки прямоугольных смайлов в игре
    :param sc: отображение рабочей области
    :param i: переменная, которая отражает конкретный прямоугольник
    :return: None
    """
    RED = (255,0,0)
    BLACK = (0,0,0)
    pygame.draw.rect(sc,i.color,(i.x,i.y,i.w,i.h))
    pygame.draw.aalines(sc,RED, False,[[(i.x + i.w//8),(i.y + 3*i.h//4)], [(i.x + i.w//4),(i.y + 5*i.h//8)],[(i.x + 3*i.w//8),(i.y + 3*i.h//4)],[(i.x + i.w//2),(i.y + 5*i.h//8)],[(i.x + 5*i.w//8),(i.y + 3*i.h//4)],[(i.x + 3*i.w//4),(i.y + 5*i.h//8)],[(i.x + 7*i.w//8),(i.y + 3*i.h//4)]],20)
    pygame.draw.rect(sc,BLACK,((i.x + i.w//8),(i.y + i.h//4),i.w//8,i.h//8))
    pygame.draw.rect(sc,BLACK,((i.x + 6*i.w//8),(i.y + i.h//4),i.w//8,i.h//8))

def reflection_rect(c):#отражение прямоуг от краёв
    """Метод для осуществления отржаения прямоугльных смайлов от границ рабочей области
    :param c: переменная, которая отражает конкретный прямоугольник
    :return: None
    """
    if c.x == 0:
        c.vx = 1
    if c.y == 0:
        c.vy = 1
    if c.x + c.w >= max_w:
        c.vx = -1
    if c.y + c.h >= max_h:
        c.vy = -1

def game_over_handler(reason, clock, pygame, sc, f1, score):
    """Метод обработки события 'игра закончена'
    :param reason: переменная, задающая причину окончания игры
    :param clock: переменная для времени
    :param sc: отображение рабочей области
    :param f1: переменная, задающая шрифт
    :param score: перменная, передающая счет
    :return: None
    """
    clock.tick(FPS)
    f1 = pygame.font.Font('C:\WINDOWS\FONTS\CAMBRIA.TTC', 26) #шрифт
    text4 = f1.render(str(score), True,LIGHT_PURLE) #создает объект
    text7 = f1.render(reason, True, LIGHT_PURLE) #создает объект
    text8 = f1.render('Ваш счёт:', True,  LIGHT_PURLE) #создает объект
    sc.fill(YELLOW)
    sc.blit(text4, (410, 153))#отображение на экране
    sc.blit(text7, (150, 100))#отображение на экране
    sc.blit(text8, (270, 153))#отображение на экране
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

def main():
    """Основная функция
    :return: None
    """
    press = (0,0)
    counter = 0
    count = 0
    count_rect = 0
    speed = 2
    score = 0
    nonzero = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    in_menu = True
    game_over = False
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
                sys.exit(1)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            in_menu = False
        if keys[pygame.K_RIGHT]:
            sys.exit(1)
        clock.tick(FPS)
        f1 = pygame.font.Font('C:\WINDOWS\FONTS\CAMBRIA.TTC', 26) #шрифт
        text3 = f1.render('Правила игры!', True, PURLE)  # создает объект
        text1 = f1.render('<Играть', True, (26, 215, 250))  # создает объект
        text2 = f1.render('Выход>', True, (26, 215, 250))  # создает объект
        pravila = f1.render('Игра была написана двумя уставшими девушками', True, PURLE)
        pravila1 = f1.render('в предсессионное время, поэтому правила просты.', True, PURLE)
        pravila3 = f1.render('Если тебе не хватает радостных эмоций, то', True, PURLE)
        pravila4 = f1.render('кликай на смайлики-улыбаки, набирая баллы, можешь,', True, PURLE)
        pravila5 = f1.render('считать, что это дополнительные баллы в накоп.', True, PURLE)
        pravila6 = f1.render('Если ты понимаешь, что сессия сложна и ты не готов,', True, PURLE)
        pravila7 = f1.render('то не время играть в игрушки - кликай на обижульки', True, PURLE)
        pravila8 = f1.render('и отправляйся зубрить билеты, завершая игру!', True, PURLE)
        text10 = f1.render('Когда игра закончится, нажми "пробел",чтобы выйти.', True, PURLE)  # создает объект
        sc.blit(star, (0, 0))
        pygame.draw.rect(sc, PINK, (70, 330, 115, 50))  # прямоугольник кнопки
        pygame.draw.rect(sc, PINK, (540, 330, 105, 50))  # прямоугольник кнопки
        sc.blit(text1, (80, 335))  # отображение на экране
        sc.blit(text2, (549, 335))  # отображение на экране
        sc.blit(text3, (240, 10))
        sc.blit(pravila, (25, 45))
        sc.blit(pravila1, (25, 75))
        sc.blit(pravila3, (25, 105))
        sc.blit(pravila4, (25, 135))
        sc.blit(pravila5, (25, 165))
        sc.blit(pravila6, (25, 195))
        sc.blit(pravila7, (25, 225))
        sc.blit(pravila8, (25, 255))
        sc.blit(text10, (25, 285))
        pygame.display.update()
    while not game_over: #основной цикл игры
        clock.tick(FPS)
        counter += 1
        time -= 1
        if time == 0:
            game_over = True
            game_over_handler('Время истекло! Игра окончена:(', clock, pygame,
                              sc, f1, score)
        for i in pygame.event.get(): # цикл для обработки событий
            if i.type == pygame.QUIT:
                sys.exit(1)
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
                game_over_handler('Увы,вы проиграли! Игра окончена:(', clock, pygame, sc, f1,
                                  score)
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
            draw_smile(sc,i,random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        for i in rects:
            draw_rect(sc,i)
        f3 = pygame.font.Font('C:\WINDOWS\FONTS\ALGER.TTF', 36)  # шрифт
        f4 = pygame.font.Font('C:\WINDOWS\FONTS\COURBD.TTF', 20)  #шрифт  # шрифт
        text3 = f3.render(str(time//FPS), True, ORANGE) #создает объект
        sc.blit(text3, (650, 50))#отображение на экране
        text4 = f3.render(str(score), True, ORANGE) #создает объект
        sc.blit(text4, (656, 127))#отображение на экране
        text5 = f4.render('Счёт', True, BLACK) #создает объект
        sc.blit(text5, (645, 103))#отображение на экране
        text6 = f4.render('Время', True, BLACK) #создает объект
        sc.blit(text6, (635, 30))#отображение на экране
        pygame.display.update()
    pygame.quit()
    return score

if __name__ == "__main__":
    score = main()
    print(score)

