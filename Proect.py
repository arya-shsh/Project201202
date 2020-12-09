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

# инициация,
# создаем объектов
pygame.init()
sc = pygame.display.set_mode((max_w, max_h))
clock = pygame.time.Clock()

# для отображения до цикла
# какиех-то объектов, обновляем экран
pygame.display.update()
sc.fill(PINK)
# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл для обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # TODO
    # изменяем объекты

    # обновляем экран
    # заливаем экран белым
    while count< max_circles:
        x = random.randint(0, max_w)
        y = random.randint(0, max_h)
        r = random.randint(min_r, max_r)
        pygame.draw.circle(sc, YELLOW, (x, y), r)
        count += 1
    pygame.display.update()
