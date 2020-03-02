import pygame


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
        self.cell_size = 50

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
        return self.list

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
                return '(' + str((i[0] - 10) // 30) + ',', str((i[1] - 10) // 30) + ')'


def level():
    global x, y, b, goo, gamerPosition, gamer, endNum
    if goo > 5:
        endNum = True
        return
    file = "Data/levels\level" + str(goo) + ".txt"
    f = open(file)
    b = [i for i in f]
    x = 0
    y = 0
    goo += 1
    gamer = pygame.image.load("data\sprites\mar.png")
    gamerPosition = [0, 0]
    screen.blit(gamer, gamerPosition)


def draw():
    global x, y, gamer, gamerPosition, g, d, \
        list_box, x1, y1, b, list_under
    screen.fill(BLACK)  # fill the screen with black
    if len(b) > 0:
        list_box = []
        list_under = []
        for i in b:
            x = 0
            for j in i:
                if j == '*':
                    ballImg = pygame.image.load("data\sprites\grass.png")
                    ballPosition = [x, y]
                    screen.blit(ballImg, ballPosition)
                elif j == '#':
                    ballImg = pygame.image.load("data\sprites\ox.png")
                    ballPosition = [x, y]
                    screen.blit(ballImg, ballPosition)
                    list_box.append(ballPosition)
                elif j == '@':
                    d = x
                    g = y
                    ballImg = pygame.image.load("data\sprites\grass.png")
                    ballPosition = [x, y]
                    screen.blit(ballImg, ballPosition)
                elif j == '?':
                    ballImg = pygame.image.load("data\sprites\ofinish.png")
                    ballPosition = [x, y]
                    screen.blit(ballImg, ballPosition)
                    x1, y1 = x, y
                elif j == '!':
                    list_under.append([x, y])
                x += 50
            y += 50


# инициализация Pygame:
pygame.init()

# размеры окна:
screen_width = 450
screen_height = 500

# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode((screen_width, screen_height))
BLACK = (0, 0, 0)

# рисование текстуры
ballImg = pygame.image.load("data\sprites\grass.png")
ballPosition = [0, 0]
screen.fill(BLACK)  # fill the screen with black
screen.blit(ballImg, ballPosition)  # draw the ball
pygame.display.update()  # update the screen

# смена (отрисовка) кадра:
pygame.display.flip()

# создание игрового поля
board = Board(20, 15)

# Открытие уровня
goo = 1
level()
endNum = False

# Первая отрисовка карты
draw()

# Скорость передвижения
speed = 50

# Отрисовка персонажа
gamer = pygame.image.load("data\sprites\mar.png")
gamerPosition = [d, g]
screen.blit(gamer, gamerPosition)

# Начало цикла
running = True

while running:
    for event in pygame.event.get():
        if endNum == True:
            screen.fill(BLACK)  # fill the screen with black
            end = pygame.image.load("data\images\END.png")
            endPosition = [0, 0]
            screen.blit(end, endPosition)
            pygame.display.update()  # update the screen
            if event.type == pygame.QUIT:
                running = False
            continue
        # Выход
        if event.type == pygame.QUIT:
            running = False
        # get all the keys being pressed
        keys = pygame.key.get_pressed()
        # depending on what key the user presses, update ball x and y position accordingly
        if keys[pygame.K_UP]:
            a = gamerPosition[1]
            gamerPosition[1] -= speed
            if gamerPosition in list_box:
                gamerPosition[1] = a
            if gamerPosition[1] == screen_height or gamerPosition[1] < 0:
                gamerPosition[1] = a
        if keys[pygame.K_DOWN]:
            a = gamerPosition[1]
            gamerPosition[1] += speed
            if gamerPosition in list_box:
                gamerPosition[1] = a
            if gamerPosition[1] == screen_height or gamerPosition[1] < 0:
                gamerPosition[1] = a
        if keys[pygame.K_LEFT]:
            a = gamerPosition[0]
            gamerPosition[0] -= speed
            if gamerPosition in list_box:
                gamerPosition[0] = a
            if gamerPosition[0] == screen_width or gamerPosition[0] < 0:
                gamerPosition[0] = a
        if keys[pygame.K_RIGHT]:
            a = gamerPosition[0]
            gamerPosition[0] += speed
            if gamerPosition in list_box:
                gamerPosition[0] = a
            if gamerPosition[0] == screen_width or gamerPosition[0] < 0:
                gamerPosition[0] = a
        if gamerPosition[0] == x1 and gamerPosition[1] == y1:
            level()
        if gamerPosition in list_under:
            gamerPosition = [0, 0]
        x = 0
        y = 0
        draw()
        screen.blit(gamer, gamerPosition)  # draw the ball
        pygame.display.update()  # update the screen

# завершение работы:
pygame.quit()
