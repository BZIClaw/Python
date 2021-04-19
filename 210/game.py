import pygame
import random
import math

# 初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("第一期游戏 - 太空之战")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("bg.png")

# 显示玩家
playerImg = pygame.image.load("player.png")
playerX = 400
playerY = 500
playerStep = 0

def move_player():
    global playerX

    playerX += playerStep
    # 防止飞机出界
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

# 添加敌人
numbers_of_enemies = 6
class Enemy():
    def __init__(self):
        self.img = pygame.image.load("enemy.png")
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(1, 2)
    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)

enemies = []
for i in range(numbers_of_enemies):
    enemies.append(Enemy())

def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)

def show_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 736 or e.x < 0:
            e.step *= -1
            e.y += 40

# 子弹类
class Bullet():
    def __init__(self):
        self.img = pygame.image.load("bullet.png")
        self.x = playerX + 15
        self.y = playerY + 10
        self.step = 3
    def hit(self):
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                e.reset()

bullets = []
def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

# 游戏主循环
running = True
while running:
    screen.blit(bgImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 2
            elif event.key == pygame.K_LEFT:
                playerStep = -2
            elif event.key == pygame.K_SPACE:
                print("发射子弹...")
                bullets.append(Bullet())
        elif event.type == pygame.KEYUP:
            playerStep = 0

    screen.blit(playerImg, (playerX, playerY))

    move_player()
    show_enemy()
    show_bullets()

    pygame.display.update()
