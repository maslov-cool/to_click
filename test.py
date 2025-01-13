import pygame
import random
import math

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 501, 501
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('К щелчку')

    running = True
    cnt = 0
    pygame.draw.circle(screen, 'red', [width / 2, height / 2], 20)
    flag = False
    x, y = width / 2, height / 2
    mouse_x, mouse_y = 0, 0
    v = 1
    speed = [0, 0]
    alpha1 = 0
    clock = pygame.time.Clock()
    while running:
        if flag:
            if x == mouse_x and y == mouse_y:
                flag = False
            elif abs(x - mouse_x) < 1:
                x = mouse_x
                if abs(y - mouse_y) < 1:
                    y = mouse_y
                else:
                    if speed[1] == 1:
                        y += v * abs(math.sin(alpha1))
                    else:
                        y -= v * abs(math.sin(alpha1))
            elif abs(y - mouse_y) < 1:
                y = mouse_y
                if abs(x - mouse_x) < 1:
                    x = mouse_x
                else:
                    if speed[0] == 1:
                        x += v * abs(math.cos(alpha1))
                    else:
                        x -= v * abs(math.cos(alpha1))
            else:
                if speed[0] == 1:
                    x += v * abs(math.cos(alpha1))
                else:
                    x -= v * abs(math.cos(alpha1))

                if speed[1] == 1:
                    y += v * abs(math.sin(alpha1))
                else:
                    y -= v * abs(math.sin(alpha1))
            if flag:
                screen.fill('black')
                pygame.draw.circle(screen, 'red', [x, y], 20)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                flag = True
                if mouse_x > x:
                    speed[0] = 1
                else:
                    speed[0] = -1
                if mouse_y > y:
                    speed[1] = 1
                else:
                    speed[1] = -1
                alpha1 = (math.acos((max(x, mouse_x) - min(x, mouse_x)) / math.sqrt((y - mouse_y) ** 2
                                                                                    + (x - mouse_x) ** 2))
                          * 180 / math.pi)
        clock.tick(random.randrange(30, 201, 10))
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
