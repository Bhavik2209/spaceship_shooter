import pygame
import random
import math

# initializing pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
# change title
pygame.display.set_caption("SPACE_BATTLE")
# player image
playerimg = pygame.image.load('icons8-spaceship-64.png')
playerX = 400
playerY = 480
playerx_change = 0
# enemy image

enemyimg = []
enemyX = []
enemyY = []
enemyx_change = []
enemyy_change = []
num_enemies = 12
for i in range(num_enemies):
    enemyimg.append(pygame.image.load('icons8-mongrol-48.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyx_change.append(0.5)
    enemyy_change.append(70)

 # bullet image
 # ready- you can't see the bullet on the screen
 # fire- the bullet is currently moving
bulletimg = pygame.image.load('icons8-bullet-32.png')
bulletX = 0
bulletY = 480
bulletx_change = 0
bullety_change = 0.9
bullet_state = "ready"

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over
gameover_font = pygame.font.Font('freesansbold.ttf', 64)


def score_show(x, y):
    score_1 = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_1, (x, y))


def gameover_text():
    over_font = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_font, (200, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                         (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# chage logo image
icon = pygame.image.load('gamer.png')
pygame.display.set_icon(icon)
# Game loop
running = True
while running:
    screen.fill((43, 42, 42))
    # playerX+=0.1

    for event in pygame.event.get():
        # playerx_change=0
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerX += playerx_change
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    # enemy movement
    for i in range(num_enemies):

        # game over

        if enemyY[i] > 470:
            for j in range(num_enemies):
                enemyY[j] = 2000
            gameover_text()
            break
        enemyX[i] += enemyx_change[i]
        if enemyX[i] <= 0:
            enemyx_change[i] = 0.3
            enemyY[i] += enemyy_change[i]
        elif enemyX[i] >= 736:
            enemyx_change[i] = -0.3
            enemyY[i] += enemyy_change[i]

         # collision
        collision_1 = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_1:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    # bullet movememnt
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bullety_change

    player(playerX, playerY)
    score_show(textX, textY)
    pygame.display.update()