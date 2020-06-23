##Space Invaders Game 
##Author: Nicky
##June 6, 2020

import pygame
from random import randint
from math import sqrt
from pygame import mixer

##initialize pygame and gameWindow
pygame.init()
WIDTH = 1200
HEIGHT = 900
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

##Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (102, 0, 102)
BLUE = (0, 0, 128)
outline = 0

##game loops
running = True  
inMenu = True  
inMapSelect = True 
inWeaponSelect = True 
inSpaceshipSelect = True
inPlay = True 
inGameOver = True 
inSettings = False

##menu button colour change when hovering/clicking
playButtonColour = BLACK
playButtonText = WHITE
exitButtonColour = BLACK
exitButtonText = WHITE
settingsButtonColour = BLACK
settingsButtonText = WHITE

##settings buttons
escapeButtonColour = RED
escapeButtonText = WHITE
musicOnButton = BLACK
musicOffButton = WHITE
easyButton = WHITE
normalButton = BLACK
insaneButton = BLACK

##fonts
font = pygame.font.Font('freesansbold.ttf', 32)
titleFont = pygame.font.Font('freesansbold.ttf', 100)
clickToPlayFont = pygame.font.Font('freesansbold.ttf', 60)
chooseMapFont = pygame.font.Font('freesansbold.ttf', 50)
gameOverFont = pygame.font.Font('freesansbold.ttf', 120)
settingsText = pygame.font.Font('freesansbold.ttf', 16)

##scoring
scoreValue = 0

##background music and button sound effect
mixer.music.load('background.wav')
buttonClick = mixer.Sound('buttonClick.wav')

##background maps and map select images
menubackground = pygame.image.load('menubackground.jpg')
map1 = pygame.image.load('map1.jpg').convert_alpha()
map1half = pygame.image.load('map1half.jpg')
map2 = pygame.image.load('map2.jpg').convert_alpha()
map2half = pygame.image.load('map2half.jpg')
map1halfhighlighted = pygame.image.load('map1halfhighlighted.jpg')
map2halfhighlighted = pygame.image.load('map2halfhighlighted.jpg')

map1state = map1half
map2state = map2half
mapChoice = ''

##weapon images and weapon select images/properties
weapon1 = pygame.image.load('weapon1.png')
weapon2 = pygame.image.load('weapon2.png')
weapon3 = pygame.image.load('weapon3.png')
weapon4 = pygame.image.load('weapon4.png')
weapon1highlighted = pygame.image.load('weapon1highlighted.png')
weapon2highlighted = pygame.image.load('weapon2highlighted.png')
weapon3highlighted = pygame.image.load('weapon3highlighted.png')
weapon4highlighted = pygame.image.load('weapon4highlighted.png')
weapon1state = weapon1
weapon2state = weapon2
weapon3state = weapon3
weapon4state = weapon4
weaponchoice = ''

##spaceship images and properties
spaceship1 = pygame.image.load('spaceship1.png')
spaceship2 = pygame.image.load('spaceship2.png')
spaceshipX = 560
spaceshipY = 720
spaceshipChangeX = 6
spaceshipChangeY = 6
healthBar = 64

##spaceship select images 
spaceship1Display = pygame.image.load('spaceship1display.png')
spaceship2Display = pygame.image.load('spaceship2display.png')
spaceship1Displayhighlighted = pygame.image.load('spaceship1displayhighlighted.png')
spaceship2Displayhighlighted = pygame.image.load('spaceship2displayhighlighted.png')
spaceship1State = spaceship1Display
spaceship2State = spaceship2Display
spaceshipChoice = ''

##bullet properties
bullet1 = pygame.image.load('bullet1.png')
bullet2 = pygame.image.load('bullet2.png')
bullet3 = pygame.image.load('bullet3.png')
bullet4 = pygame.image.load('bullet4.png')
bulletChoice = ''
bulletX = 0
bulletY = 480
bulletChangeX = 0
bulletChangeY = 20
bulletState = "ready"

##enemy properties
enemyList = []
enemyX = []
enemyY = []
enemyChangeX = []
enemyChangeY = []
numberEnemies = 10

##laser properties
laserList = []
laserX = []
laserY = []
laserChangeX = []
laserChangeY = []

##difficulty levels (easy, normal, insane)
easy = 5
normal = 15
insane = 30
difficultyLevel = easy

##functions
def quitGame():
    global running 
    global inMenu 
    global inMapSelect
    global inWeaponSelect 
    global inSpaceshipSelect
    global inPlay 
    global inGameOver 
    global inSettings
    running = False
    inMenu = False
    inMapSelect = False
    inWeaponSelect = False
    inSpaceshipSelect = False
    inPlay = False
    inGameOver = False
    inSettings = False

def redrawMenuWindow():
    global playButtonColour
    global playButtonText
    global settingsButtonColour
    global settingsButtonText
    global inMenu
    global inMapSelect
    global inWeaponSelect
    global inSpaceshipSelect
    global inPlay
    global inGameOver
    global inSettings
    global healthBar
    global scoreValue
    global welcomeLine

    inMapSelect = True
    inWeaponSelect = True
    inSpaceshipSelect = True
    inPlay = True
    inGameOver = True
    healthBar = 64
    scoreValue = 0

    gameWindow.blit(menubackground, (0, 0))
    titleText = titleFont.render("SPACE INVADERS", True, WHITE)
    gameWindow.blit(titleText, (160, 150))
    pygame.draw.rect(gameWindow, playButtonColour, (350, 375, 500, 300), outline)
    clickToPlayText = clickToPlayFont.render("CLICK TO PLAY", True, playButtonText)
    gameWindow.blit(clickToPlayText, (370, 500))
    pygame.draw.rect(gameWindow, settingsButtonColour, (350, 700, 500, 150))
    menuSettingsText = clickToPlayFont.render("SETTINGS", True, settingsButtonText)
    gameWindow.blit(menuSettingsText, (440, 750))

    gameWindow.blit(spaceship1Display, (60, 400))
    gameWindow.blit(spaceship2Display, (900, 400))

    welcomeText = clickToPlayFont.render(str(welcomeLine), True, WHITE)
    gameWindow.blit(welcomeText, (160, 270))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        quitGame()
    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()
        if cursorX > 350 and cursorX < 850 and cursorY > 375 and cursorY < 675:
            playButtonColour = WHITE
            playButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)                
                inMenu = False
        else:
            playButtonColour = BLACK
            playButtonText = WHITE
                
        if cursorX > 350 and cursorX < 850 and cursorY > 700 and cursorY < 950:
            settingsButtonColour = WHITE
            settingsButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                inSettings = True
        else:
            settingsButtonColour = BLACK
            settingsButtonText = WHITE

        while inSettings:
            redrawSettingsWindow()
            pygame.display.update()

    pygame.display.update()

def redrawMapSelectWindow():
    global map1state
    global map2state
    global inMapSelect
    global mapChoice
    pygame.event.clear()
    gameWindow.blit(map1state, (0, 0))
    gameWindow.blit(map2state, (600, 1))
    chooseMapText = chooseMapFont.render("CHOOSE YOUR MAP", True, WHITE)
    gameWindow.blit(chooseMapText, (340, 50))
    map1Text = chooseMapFont.render("PLANET INVASION", True, WHITE)
    gameWindow.blit(map1Text, (70, 750))
    map2Text = chooseMapFont.render("ASTEROID ATTACK", True, WHITE)
    gameWindow.blit(map2Text, (670, 750))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        quitGame()

    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()

        if cursorX >= 0 and cursorX < 600 and cursorY >= 0 and cursorY <= 900:
            map1state = map1halfhighlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                mapChoice = map1
                inMapSelect = False
        else:
            map1state = map1half

        if cursorX >= 600 and cursorX <= 1200 and cursorY >= 0 and cursorY <= 900:
            map2state = map2halfhighlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                mapChoice = map2
                inMapSelect = False
        else:
            map2state = map2half

    pygame.display.update()

def redrawWeaponSelectWindow():
    global inWeaponSelect
    global bulletChoice
    global weapon1state
    global weapon2state
    global weapon3state
    global weapon4state
    pygame.event.clear()
    gameWindow.fill(BLACK)
    chooseWeaponText = chooseMapFont.render("CHOOSE YOUR WEAPON", True, WHITE)
    gameWindow.blit(chooseWeaponText, (290, 50))
    pygame.draw.line(gameWindow, WHITE, (600, 150), (600, 900))
    pygame.draw.line(gameWindow, WHITE, (0, 510), (1200, 510))
    gameWindow.blit(weapon1state, (175, 160))
    gameWindow.blit(weapon2state, (760, 155))
    gameWindow.blit(weapon3state, (175, 530,))
    gameWindow.blit(weapon4state, (770, 530))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        quitGame()

    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()

        if cursorX >= 0 and cursorX < 600 and cursorY >= 150 and cursorY <= 510:
            weapon1state = weapon1highlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                bulletChoice = bullet1
                inWeaponSelect = False
        else:
            weapon1state = weapon1

        if cursorX >= 600 and cursorX < 1200 and cursorY >= 150 and cursorY <= 510:
            weapon2state = weapon2highlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                bulletChoice = bullet2
                inWeaponSelect = False
        else:
            weapon2state = weapon2
        
        if cursorX >= 0 and cursorX < 600 and cursorY >= 510 and cursorY <= 900:
            weapon3state = weapon3highlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                bulletChoice = bullet3
                inWeaponSelect = False
        else:
            weapon3state = weapon3

        if cursorX >= 600 and cursorX < 1200 and cursorY >= 510 and cursorY <= 900:
            weapon4state = weapon4highlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                bulletChoice = bullet4
                inWeaponSelect = False
        else:
            weapon4state = weapon4

    pygame.display.update()

def redrawSpaceshipSelectionWindow():
    global inSpaceshipSelect
    global spaceship1State
    global spaceship2State
    global spaceshipChoice
    pygame.event.clear()
    gameWindow.fill(BLACK)
    chooseSpaceshipText = chooseMapFont.render("CHOOSE YOUR SPACESHIP", True, WHITE)
    gameWindow.blit(chooseSpaceshipText, (275, 50))
    pygame.draw.line(gameWindow, WHITE, (600, 150), (600, 900))
    gameWindow.blit(spaceship1State, (145, 350))
    gameWindow.blit(spaceship2State, (780, 350))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        quitGame()

    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()

        if cursorX >= 0 and cursorX < 600 and cursorY >= 150 and cursorY <= 900:
            spaceship1State = spaceship1Displayhighlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                spaceshipChoice = spaceship1
                inSpaceshipSelect = False
        else:
            spaceship1State = spaceship1Display

        if cursorX >= 600 and cursorX <= 1200 and cursorY >= 150 and cursorY <= 900:
            spaceship2State = spaceship2Displayhighlighted
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                spaceshipChoice = spaceship2
                inSpaceshipSelect = False
        else:
            spaceship2State = spaceship2Display

    pygame.display.update()

def redrawGameOverWindow():
    global inMenu
    global inGameOver
    global inSettings
    global playButtonColour
    global settingsButtonColour
    global exitButtonColour
    global playButtonText
    global exitButtonText
    global settingsButtonText
    global difficultyLevel
    global easy
    global normal
    global insane
    pygame.event.clear()
    gameWindow.blit(menubackground, (0, 0))
    pygame.draw.rect(gameWindow, playButtonColour, (340, 375, 515, 300), outline)
    pygame.draw.rect(gameWindow, settingsButtonColour, (5, 375, 320, 300), outline)
    pygame.draw.rect(gameWindow, exitButtonColour, (870, 375, 320, 300), outline)

    gameOverText = gameOverFont.render("GAME OVER", True, WHITE)
    gameWindow.blit(gameOverText, (200, 150))
    clickToPlayText = clickToPlayFont.render("PLAY AGAIN", True, playButtonText)
    gameWindow.blit(clickToPlayText, (405, 500))
    exitText = clickToPlayFont.render("EXIT", True, exitButtonText)
    gameWindow.blit(exitText , (950, 490))
    settingsText = clickToPlayFont.render("SETTINGS", True, settingsButtonText)
    gameWindow.blit(settingsText, (10, 500))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        quitGame()
    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()
        if cursorX > 340 and cursorX < 855 and cursorY > 375 and cursorY < 675:
            playButtonColour = WHITE
            playButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                inMenu = True
                inGameOver = False
                inSettings = False
        else:
            playButtonColour = BLACK
            playButtonText = WHITE

        if cursorX > 880 and cursorX < 1175 and cursorY > 375 and cursorY < 675:
            exitButtonColour = WHITE
            exitButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                quitGame()
        else:
            exitButtonColour = BLACK
            exitButtonText = WHITE

        if cursorX > 20 and cursorX < 320 and cursorY > 375 and cursorY < 675:
            settingsButtonColour = WHITE
            settingsButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                inSettings = True

        else:
            settingsButtonColour = BLACK
            settingsButtonText = WHITE

        while inSettings:
            redrawSettingsWindow()
            pygame.display.update()

    displayScore(50, 825)
    pygame.display.update()

def redrawSettingsWindow():
    global inSettings
    global inMenu
    global escapeButtonColour
    global escapeButtonText
    global easyButton
    global normalButton
    global insaneButton
    global musicOnButton
    global musicOffButton
    global difficultyLevel
    global easy
    global normal
    global insane
    pygame.event.clear()
    gameWindow.blit(menubackground, (0, 0))
    pygame.draw.line(gameWindow, WHITE, (0, 650), (1200, 650))
    pygame.draw.line(gameWindow, WHITE, (400, 650), (400, 900))
    pygame.draw.line(gameWindow, WHITE, (800, 650), (800, 900))
    infoText = font.render("Game Info", True, WHITE)
    gameWindow.blit(infoText, (500, 60))
    levelText = font.render("Level", True, WHITE)
    gameWindow.blit(levelText, (30, 675))
    musicText = font.render("Music", True, WHITE)
    gameWindow.blit(musicText, (430, 675))
    creditsTitle = font.render("Credits", True, WHITE)
    gameWindow.blit(creditsTitle, (830, 675))
    creditsText = settingsText.render("Space Invaders Variation by Nicholas Chew", True, WHITE)
    gameWindow.blit(creditsText, (830, 780))

    pygame.draw.rect(gameWindow, escapeButtonColour, (20, 20, 160, 80))
    backText = font.render("BACK", True, escapeButtonText)
    gameWindow.blit(backText, (52, 47))
    pygame.draw.rect(gameWindow, musicOnButton, (500, 750, 80, 80))
    pygame.draw.rect(gameWindow, musicOffButton, (600, 750, 80, 80))
    onText = settingsText.render("On", True, WHITE)
    gameWindow.blit(onText, (500, 830))
    offText = settingsText.render("Off", True, WHITE)
    gameWindow.blit(offText, (600, 830))

    pygame.draw.rect(gameWindow, easyButton, (40, 750, 80, 80))
    pygame.draw.rect(gameWindow, normalButton, (130, 750, 80, 80))
    pygame.draw.rect(gameWindow, insaneButton, (220, 750, 80, 80))
    easyText = settingsText.render("Easy", True, WHITE)
    gameWindow.blit(easyText, (40, 830))
    normalText = settingsText.render("Normal", True, WHITE)
    gameWindow.blit(normalText, (130, 830))
    insaneText = settingsText.render("Insane", True, WHITE)
    gameWindow.blit(insaneText, (220, 830))

    line1Text = settingsText.render("Kill the aliens to earn points but watch out for their lasers! You die if you are hit four times or if the aliens cross your safety zone.", True, WHITE)
    line2Text = settingsText.render("Use the arrow keys to move and spacebar to shoot your bullets.", True, WHITE)
    line3Text = settingsText.render("Feel free to customize your map, ship, and weapon each time you play.", True, WHITE)
    line4Text = settingsText.render("Adjust the difficulty of gameplay in the settings below.", True, WHITE)
    line5Text = settingsText.render("Hit Escape to leave the game and feel free to turn the music on or off, Have fun!", True, WHITE)
    gameWindow.blit(line1Text, (120, 150))
    gameWindow.blit(line2Text, (120, 200))
    gameWindow.blit(line3Text, (120, 250))
    gameWindow.blit(line4Text, (120, 300))
    gameWindow.blit(line5Text, (120, 350))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        quitGame()

    for event in pygame.event.get():
        (cursorX, cursorY) = pygame.mouse.get_pos()
        if cursorX > 20 and cursorX < 180 and cursorY > 20 and cursorY < 140:
            escapeButtonColour = WHITE
            escapeButtonText = BLACK
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                inSettings = False
        else:
            escapeButtonColour = RED
            escapeButtonText = WHITE

        if cursorX > 500 and cursorX < 580 and cursorY > 750 and cursorY < 830:
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                mixer.music.play(-1)
                musicOnButton = WHITE
                musicOffButton = BLACK

        if cursorX > 600 and cursorX < 680 and cursorY > 750 and cursorY < 830:
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                pygame.mixer.music.stop()
                musicOffButton = WHITE
                musicOnButton = BLACK

        if cursorX > 40 and cursorX < 120 and cursorY > 750 and cursorY < 830:
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                easyButton = WHITE
                normalButton = BLACK
                insaneButton = BLACK
                difficultyLevel = easy

        if cursorX > 130 and cursorX < 210 and cursorY > 750 and cursorY < 830:
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                easyButton = BLACK
                normalButton = WHITE
                insaneButton = BLACK
                difficultyLevel = normal

        if cursorX > 220 and cursorX < 300 and cursorY > 750 and cursorY < 830:
            if event.type == pygame.MOUSEBUTTONUP:
                buttonClick.play()
                pygame.time.delay(200)
                easyButton = BLACK
                normalButton = BLACK
                insaneButton = WHITE
                difficultyLevel = insane

    pygame.display.update()

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def displayScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    gameWindow.blit(score, (x, y))

def spaceship(x, y):
    gameWindow.blit(spaceshipChoice, (x, y))
    pygame.draw.rect(gameWindow, GREEN, (spaceshipX, spaceshipY + 70, healthBar, 10))

def enemy(x, y, i):
    gameWindow.blit(enemyList[i], (x, y))

def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    gameWindow.blit(bulletChoice, (x, y - 64))

def fireLaser(x, y):
    global difficultyLevel
    gameWindow.blit(laserList[i], (x + 16, y + 64))
    laserY[i] += difficultyLevel
    laserX[i] += laserChangeX[i]

def enemyKilled(enemyX, enemyY, bulletX, bulletY):
    bulletCollision = distance(enemyX + 32, enemyY - 32, bulletX + 32, bulletY - 32)
    if bulletCollision < 35:    
        return True
    else:
        return False

def spaceshipHit(enemyX, enemyY, spaceshipX, spaceshipY):
    spaceshipCollision = distance(enemyX + 24, enemyY - 24, spaceshipX + 24, spaceshipY - 24)
    if spaceshipCollision < 48:
        return True
    else:
        return False

def spaceshipShot(laserX, laserY, spaceshipX, spaceshipY):
    spaceshipCollision = distance(laserX + 16, laserY + 32, spaceshipX + 24, spaceshipY - 24)
    if spaceshipCollision < 30:
        return True
    else:
        return False

username = input("Enter your name: ")
welcomeLine = 'Welcome ' + username + '!'

while running:
    while inMenu:
        redrawMenuWindow()
    
    while inMapSelect:
        redrawMapSelectWindow()
        
    while inWeaponSelect:
        redrawWeaponSelectWindow()

    while inSpaceshipSelect:
        redrawSpaceshipSelectionWindow()

    while inPlay:
        pygame.event.clear()
        pygame.time.delay(10)
        gameWindow.blit(mapChoice, (0, 0))
        pygame.draw.line(gameWindow, WHITE, (0, 450), (1200, 450))
        explosionSound = mixer.Sound('explosion.wav')

        spaceship(spaceshipX, spaceshipY)
        displayScore(50, 825)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            quitGame() 

        if keys[pygame.K_g]:
            inPlay = False

        if keys[pygame.K_LEFT]:
            spaceshipX -= spaceshipChangeX
            if spaceshipX < 0:
                spaceshipX = 0
        if keys[pygame.K_RIGHT]:
            spaceshipX += spaceshipChangeX
            if spaceshipX > WIDTH - 64:
                spaceshipX = WIDTH - 64
        if keys[pygame.K_UP]:
            spaceshipY -= spaceshipChangeY
            if spaceshipY < 0:
                spaceshipY = 0
        if keys[pygame.K_DOWN]:
            spaceshipY += spaceshipChangeY
            if spaceshipY > HEIGHT - 90:
                spaceshipY = HEIGHT - 90

        if keys[pygame.K_SPACE] and bulletState == "ready":
            bulletSound = mixer.Sound('bulletsound.wav')
            bulletSound.play()
            bulletX = spaceshipX
            fireBullet(bulletX, bulletY)
        
        # bullet movement
        if bulletY <= 0:
            bulletY = spaceshipY
            bulletState = "ready"
        if bulletState == "fire":
            fireBullet(bulletX, bulletY)
            bulletY -= bulletChangeY
            
        for i in range(numberEnemies):
            
            enemyList.append(pygame.image.load('enemy.png'))
            enemyX.append(randint(0, 1130))
            enemyY.append(randint(0, 200))
            enemyChangeX.append(4)
            enemyChangeY.append(50)
            laserList.append(pygame.image.load('enemylaser.png'))
            laserX.append(enemyX[i])
            laserY.append(enemyY[i])
            laserChangeX.append(0)
            laserChangeY.append(difficultyLevel)

            if enemyY[i] >= 386:
                for j in range(numberEnemies):
                    enemyY[j] = 3000
                    pygame.time.delay(800)
                    explosionSound.play()
                    inPlay = False

            enemyX[i] += enemyChangeX[i]
            if enemyX[i] <= 0:
                enemyChangeX[i] = 3
                enemyY[i] += enemyChangeY[i]
            elif enemyX[i] >= WIDTH - 64:
                enemyChangeX[i] = -3
                enemyY[i] += enemyChangeY[i]

            if laserY[i] >= 900:
                laserY[i] = enemyY[i]
                laserX[i] = enemyX[i]

            if enemyKilled(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = spaceshipY
                bulletState = "ready"
                scoreValue += 1
                enemyX[i] = randint(0, 530)
                enemyY[i] = randint(0, 200)

            if spaceshipHit(enemyX[i], enemyY[i], spaceshipX, spaceshipY):
                explosionSound.play()
                pygame.time.delay(800)
                spaceshipX = 560
                spaceshipY = 720
                healthBar -= 16

            elif spaceshipShot(laserX[i], laserY[i], spaceshipX, spaceshipY):
                explosionSound.play()
                pygame.time.delay(800)
                spaceshipX = 560
                spaceshipY = 720
                laserX[i] = enemyX[i]
                laserY[i] = enemyY[i]
                healthBar -= 16

            fireLaser(laserX[i], laserY[i])
            enemy(enemyX[i], enemyY[i], i)

        if healthBar == 0:
            inPlay = False
            explosionSound.play()
            pygame.time.delay(1000)

        pygame.display.update()

    while inGameOver:
        redrawGameOverWindow()

pygame.quit()
