import sys
import random
import pygame

from week03.day04.BulletClass import Bullet
from week03.day04.data import *
from week03.day04.heroClass import Hero
from week03.day04.ButtonClass import Button
from week03.day04.EnemyClass import Enemy
from week03.day04.fontScore import scoresurface


pygame.init()
pygame.mixer.init()

enemygroup = pygame.sprite.Group()
bulletgroup = pygame.sprite.Group()

winSurface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("飞机大战")

# 画背景
bgsurface = pygame.image.load("./images/background.png").convert()
# heroSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
# heroSurface2 = pygame.image.load("./images/me2.png").convert_alpha()

# 时钟对象创建
clock = pygame.time.Clock()
curScore = 0
# 写字 font对象及surface对象
mfont = pygame.font.Font("font/font.ttf", 20)
mfontSurface = scoresurface(mfont,curScore,(0,0,225),"score")

# 暂停/继续按钮
mBtn = Button()

# 背景音乐
pygame.mixer.music.load("./sound/game_music.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
# 子弹发射时的音效
bullentSound = pygame.mixer.Sound("sound/bullet.wav")
bullentSound.set_volume(0.5)
enemyDownSound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemyDownSound.set_volume(0.5)

# 创建hero的对象
hero = Hero()
# 初始化hero的坐标(display的正中间距离下方50处)
# hero.rect.left = DISPLAY_WIDTH // 2 - hero.rect.width // 2
# hero.rect.top = DISPLAY_HEIGHT - hero.rect.height - OFFSIDE

# 创建子弹的list
bulletList = []
for i in range(BULLETCOUNTS):
    mbullet = Bullet()
    bulletList.append(mbullet)
# 创建敌人的list
enemyList = []
for i in range(ENEMYCOUNTS):
    menemy = Enemy()
    enemyList.append(menemy)

# 用来计数  while TRUE当前为第count次循环
count = 0
bulletListIndex = 0
enemyListIndex = 0

while True:
    # 背景音乐的播放

    # 绘制背景
    winrect = winSurface.blit(bgsurface, (0, 0))
    # print(bulletList[0].rect.width)
    # winSurface.blit(bulletList[0].surface, (100, 100))

    # 敌人的产生规则  随机 随时
    if not mBtn.isPause:
        if (count % 10 == 0):
            isArise = random.randint(0, 1)
            if isArise:
                enemyList[enemyListIndex].isActive = True
                enemyList[enemyListIndex].rect.left = random.randint \
                    (0, DISPLAY_WIDTH - enemyList[enemyListIndex].rect.width)
                enemyList[enemyListIndex].rect.top = 0
                enemyListIndex = (enemyListIndex + 1) % 10
                # winSurface.blit(enemyList[enemyListIndex].surface,
                #              (enemyList[enemyListIndex].rect.left, enemyList[enemyListIndex].rect.top))
    # 每10zheng 发射一颗子弹
    if (count % 10 == 0):
        bulletList[bulletListIndex].isActive = True
        bulletList[bulletListIndex].rect.left = hero.rect.left + hero.rect.width // 2 - bulletList[0].rect.width // 2
        bulletList[bulletListIndex].rect.top = hero.rect.top - bulletList[0].rect.height
        # winSurface.blit(bulletList[bulletListIndex].surface,
        #                 (bulletList[bulletListIndex].rect.left, bulletList[bulletListIndex].rect.top))
        bulletListIndex = (bulletListIndex + 1) % 10
        if not mBtn.isPause:
            bullentSound.play(1)
        # winSurface.blit(bulletList[0].surface,(10,10))
        pass
    # 每颗子弹自己移动
    for bullet in bulletList:
        if bullet.isActive == True:
            bulletgroup.add(bullet)
            # print(bullet.rect.top)
            # 如果不是暂停子弹移动
            if not mBtn.isPause:
                bullet.move()
            winSurface.blit(bullet.surface, (bullet.rect.left, bullet.rect.top))
    # 敌人与子弹的相互碰撞检测


    # 每架敌人自己移动
    for enemy in enemyList:
        if enemy.isActive == True:
            # 检测敌人是否与子弹的 精灵碰撞
            mbulletlist = pygame.sprite.spritecollide(enemy, bulletgroup, True, pygame.sprite.collide_mask)
            # 如果不是暂停 子弹移动
            if not mBtn.isPause:
                if len(mbulletlist)>0:
                    enemyDownSound.play(0)
                    curScore+=100
                    enemy.isBoom =True

                if enemy.isBoom and count%3==0:
                    enemy.enemyBoom()
                    enemy.boomIndex+=1
                if not enemy.isBoom:
                    enemy.move()
                    pass

            winSurface.blit(enemy.surface, (enemy.rect.left, enemy.rect.top))

    # 将碰撞后剩余存活的子弹设置为 isActive = True
    for item in bulletList:
        item.isActive = False
    for item in bulletgroup:
        item.isActive = True

    # 绘制 hero 并且有动画效果
    if count % 5 == 0:
        herosurface = hero.surfaces[0]
    else:
        herosurface = hero.surfaces[1]
    # 画出 hero 和字的图像
    winSurface.blit(herosurface, (hero.rect.left, hero.rect.top))


    # 事件处理
    # 获得触发事件的列表
    eventList = pygame.event.get()
    for event in eventList:
        # 点击退出 时的事件出理
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            # print(mBtn.rect.left,mBtn.rect.top)
            if mBtn.rect.collidepoint(event.pos):
                # print(event.pos)
                if (mBtn.isPause):
                    mBtn.isPause = False
                else:
                    mBtn.isPause = True
                    # mBtn.Btn_PauseGame()
                    # winSurface.blit(mBtn.buttonSurfaces[3], (400, 30))

    # 鼠标 的顺发事件处理  鼠标在暂停图标的不同图片显示
    if mBtn.rect.collidepoint(pygame.mouse.get_pos()):
        # print(pygame.mouse.get_pos())
        # winSurface.blit(mBtn.buttonSurfaces[2], (400, 30))
        mBtn.isOver = True
    else:
        mBtn.isOver = False
        # print(boolsmouseTuple)
    mBtn.Btn_MosueOver()
    # 键盘控制飞机的上下左右飞行事件
    # 獲取所有的鍵盤的pressed狀態
    # 获得键盘状态事件
    # print(pygame.mouse.get_pos())
    if not mBtn.isPause:
        pygame.mixer.music.unpause()
        count += 1

        pass
        boolsTuple = pygame.key.get_pressed()
        # print(boolsTuple,"count======================",count)
        if boolsTuple[pygame.K_UP]:
            hero.moveUp()
        if boolsTuple[pygame.K_DOWN]:
            hero.moveDown()
        if boolsTuple[pygame.K_LEFT]:
            hero.moveLeft()
        if boolsTuple[pygame.K_RIGHT]:
            hero.moveRight()
    else:
        pygame.mixer.music.pause()
        bullentSound.stop()
        enemyDownSound.stop()
    # hero的绘制
    # 每1/60s刷新一次画布
    mfontSurface.score = curScore
    mfontSurface.refalshsurface()
    winSurface.blit(mfontSurface.surface, (10, 10))
    winSurface.blit(mBtn.btnSurface, (400, 30))

    pygame.display.flip()
    clock.tick(60)

    # pygame.time.wait(1000)
    pass
