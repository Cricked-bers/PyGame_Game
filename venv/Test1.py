import pygame
import os


# создание клетчатого поля
class Board:
    # создание поля
    def __init__(self, width, height):
        self.list = []
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 40

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # рисование клеток, распределение
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + j * self.cell_size,
                                                           self.top + i * self.cell_size,
                                                           self.cell_size, self.cell_size), 1)
                self.list.append((self.left + j * self.cell_size, self.top + i * self.cell_size))

    # реакция на нажатие мыши и вывод позиции мыши
    def get_cell(self, mouse_pos):
        mouse_pos = list(mouse_pos)
        self.list = list(set(self.list))
        # print(mouse_pos)
        # print(sorted(self.list))
        if self.left < mouse_pos[0] < (self.width * self.cell_size) + self.left and self.top < mouse_pos[1] < (
                self.height * self.cell_size) + self.top:
            pass
        for i in sorted(self.list):
            if i[0] < mouse_pos[0] < i[0] + self.cell_size and i[1] < mouse_pos[1] < i[1] + self.cell_size:
                print('(' + str((i[0] - 10) // 30) + ',', str((i[1] - 10) // 30) + ')')


# инициализация Pygame:
pygame.init()

# размеры окна:
size = width, height = 800, 600

# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

# смена (отрисовка) кадра:
pygame.display.flip()
# создание игрового поля

board = Board(20, 15)

# run = true
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # вывод координат клетки
        if event.type == pygame.MOUSEBUTTONUP:
            board.get_cell(event.pos)
    screen.fill((0, 0, 0))
    # вызов сетки
    '''board.render()'''
    pygame.display.flip()
# завершение работы:
pygame.quit()
