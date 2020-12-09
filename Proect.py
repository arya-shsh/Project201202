# подключаем модули
import pygame
import sys
import random

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
pygame.init()
sc = pygame.display.set_mode((max_w, max_h))
clock = pygame.time.Clock()

# для отображения до цикла
# какиех-то объектов, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл для обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            press = i.pos

    # TODO
    # изменяем объекты

    # обновляем экран
    # заливаем экран розовым
    sc.fill(PINK)
    while count< max_circles:
        x = random.randint(0, max_w)
        y = random.randint(0, max_h)
        r = random.randint(min_r, max_r)
        circles.append((x,y,r)) # сохраняем созданные круги в списке
        count += 1
    for i in circles:
        if (press[0]-i[0])**2+(press[1]-i[1])**2<= i[2]**2: #проверяем принадлежность координат нажатия координатам круга
            circles.remove(i)
            count-=1 #вместо осчезнувшего круга добавляем новый
    for i in circles:
        pygame.draw.circle(sc, YELLOW, (i[0], i[1]), i[2]) #рисуем кружочки

    pygame.display.update()
