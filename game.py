import pygame
import random
import math

pygame.init()
screen_width=800
screen_height=600

gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader Game")
icon=pygame.image.load('C:/Users/Raghavi/Downloads/launch.png')
pygame.display.set_icon(icon)

# background
backg=pygame.image.load('C:/Users/Raghavi/Downloads/background.png')

#Player
playerImg=pygame.image.load('C:/Users/Raghavi/Downloads/player.png')
playerX=370
playerY=480

def player(X,Y):
    gamewindow.blit(playerImg,(X,Y))
    
    
#enemy
'''enemyImg=pygame.image.load('C:/Users/Raghavi/Downloads/enemy.png')
enemyX=24
enemyY=23

enemyX=random.randint(0,736)
enemyY=random.randint(50,150)
enemyX_change=4
enemyY_change=40
'''


enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemy=6


for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('C:/Users/Raghavi/Downloads/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)


def enemy(X,Y,i):
    gamewindow.blit(enemyImg[i],(X,Y))
       

# bullet creation
bulletImg=pygame.image.load('C:/Users/Raghavi/Downloads/bullet.png')
#bulletImg="•"
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"


def fire_bullet(X,Y):
    global bullet_state
    bullet_state="fire"
    gamewindow.blit(bulletImg,(X+16,Y+12))
    
    
def testCollison(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    else:
        return False
    
score=0
fonnt=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


def show_score(X,Y):
    score1=fonnt.render("Score :"+str(score),True,(255,255,255))
    gamewindow.blit(score1,(X,Y))


text=pygame.font.Font('freesansbold.ttf',72)
def game_over(X,Y):
    text=fonnt.render("game over",True,(255,255,255))
    gamewindow.blit(text,(200,250))
    
    
block_update=5
playerX_change=0
closewindow=False
white=(255,255,255)
MAGENTA = (255, 0, 255)

while not closewindow:
    gamewindow.fill(MAGENTA)
    gamewindow.blit(backg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            closewindow=True
            
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-block_update
            if event.key==pygame.K_RIGHT:
                playerX_change=block_update
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change =0
            
    playerX+= playerX_change
    
    if playerX<=0:
        playerX=0
    elif playerX>=736:
       playerX=736
       
    
    #enemy movement
    for i in range(no_of_enemy):
        
        
        #when the game will be over
        if enemyY[i]>440:
            for j in range(no_of_enemy):
                enemyY[j]=20000
            
            game_over()
            break
        
        enemyX[i]+enemyX_change[i]
        
        if enemyX[i]<=0:
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i] = -4
            enemyY[i]+= enemyY_change[i]
        collison=testCollison(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison:
            bulletY=480
            bullet_state = "ready"
            score = score + 1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)
        
        
    # bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
        
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
       
    
        #print(score)
    player(playerX,playerY)
    
    show_score(textX,textY)
    pygame.display.update()