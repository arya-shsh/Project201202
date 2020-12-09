#подключаем модули
import pygame
import sys
 
#определяем константы,
#классы и функции
FPS = 60
 
#инициация,
#создаем объектов
pygame.init()
sc = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
 
#для отображения до цикла
#какиех-то объектов, обновляем экран
pygame.display.update()
 
#главный цикл
while True:
 
    #задержка
    clock.tick(FPS)
 
    #цикл для обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    #TODO
    #изменяем объекты

    
 
    #обновляем экран
    pygame.display.update()