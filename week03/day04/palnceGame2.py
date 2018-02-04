import sys
import random
import pygame

from week03.day04.BulletClass import Bullet
from week03.day04.data import *
from week03.day04.heroClass import Hero
from week03.day04.ButtonClass import Button
from week03.day04.EnemyClass import Enemy
from week03.day04.WingPlanceClass import wingPlace
from week03.day04.wpBulletClass import wpBullet

from week03.day04.fontScore import scoresurface


pygame.init()
pygame.mixer.init()

bulletgroup = pygame.sprite.Group()
wpbulletgroup = pygame.sprite.Group()

winSurface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("飞机大战")

# 画背景
bgsurface = pygame.image.load("./images/background.png").convert()
# heroSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
# heroSurface2 = pygame.image.load("./images/me2.png").convert_alpha()

# 创建hero的对象
hero = Hero()
wingplance = wingPlace()

# 时钟对象创建
clock = pygame.time.Clock()
curScore = 0
# 写字 font对象及surface对象
mfont = pygame.font.Font("font/font.ttf", 20)
mfontSurface1 = scoresurface(mfont,hero.booldbar,(0,0,225),"hero:")
mfontSurface2 = scoresurface(mfont,wingplance.booldbar,(225,0,0),"Wingpalce:")



# 背景音乐
pygame.mixer.music.load("./sound/game_music.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
# 子弹发射时的音效
bullentSound = pygame.mixer.Sound("sound/bullet.wav")
bullentSound.set_volume(0.5)
enemyDownSound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemyDownSound.set_volume(0.5)

# 暂停/继续按钮
mBtn = Button()

# 初始化hero的坐标(display的正中间距离下方50处)


# 创建子弹的list
bulletList = []
for i in range(BULLETCOUNTS):
    mbullet = Bullet()
    bulletList.append(mbullet)
# 创建僚机子弹的list
wpbulletList = []
for i in range(BULLETCOUNTS):
    wpmbullet = wpBullet()
    wpbulletList.append(wpmbullet)


# 用来计数  while TRUE当前为第count次循环
count = 0
bulletListIndex = 0


while True:
    # 背景音乐的播放

    # 绘制背景
    winrect = winSurface.blit(bgsurface, (0, 0))
    # print(bulletList[0].rect.width)
    # winSurface.blit(bulletList[0].surface, (100, 100))

    # 每10zheng 发射一颗子弹
    if (count % 10 == 0):
        if (hero.booldbar > 0):
            bulletList[bulletListIndex].isActive = True
            bulletList[bulletListIndex].rect.left = hero.rect.left + hero.rect.width // 2 - bulletList[
                                                                                                0].rect.width // 2
            bulletList[bulletListIndex].rect.top = hero.rect.top - bulletList[0].rect.height
        if (wingplance.booldbar > 0):
            wpbulletList[bulletListIndex].isActive = True

            wpbulletList[bulletListIndex].rect.left = wingplance.rect.left + wingplance.rect.width // 2 - wpbulletList[0].rect.width // 2
            wpbulletList[bulletListIndex].rect.top = wingplance.rect.top - wpbulletList[0].rect.height
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
    for wpbulletitem in wpbulletList:
        if wpbulletitem.isActive == True:
            wpbulletgroup.add(wpbulletitem)
            # print(bullet.rect.top)
            # 如果不是暂停子弹移动
            if not mBtn.isPause:
                wpbulletitem.move()
            winSurface.blit(wpbulletitem.surface, (wpbulletitem.rect.left, wpbulletitem.rect.top))
            # winSurface.blit(wpbulletitem.surface, (100,100))

    # 僚机子弹与英雄的碰撞检测   英雄子弹与僚机的碰撞检测
    mlist1=pygame.sprite.spritecollide(hero,wpbulletgroup,True,pygame.sprite.collide_mask)
    mlist2=pygame.sprite.spritecollide(wingplance,bulletgroup,True,pygame.sprite.collide_mask)
    # 僚机子弹与英雄的有碰撞
    if (len(mlist1)>0):
        for item in mlist1:
            if hero.booldbar >0:
            # print(item.rect.left, item.rect.top)
                hero.booldbar -=5
                item.isActive = False

    # 英雄子弹与僚机的有碰撞
    if (len(mlist2)>0):
        for item in mlist2:
            if wingplance.booldbar >0:
                wingplance.booldbar -=5
                # print(item.rect.left, item.rect.top)
                item.isActive = False

        pass


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
    if(wingplance.booldbar>0):
        winSurface.blit(wingplance.surface, (wingplance.rect.left, wingplance.rect.top))

    if (hero.booldbar > 0):
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
        if boolsTuple[pygame.K_w]:
            wingplance.moveUp()
        if boolsTuple[pygame.K_s]:
            wingplance.moveDown()
        if boolsTuple[pygame.K_a]:
            wingplance.moveLeft()
        if boolsTuple[pygame.K_d]:
            wingplance.moveRight()
    else:
        pygame.mixer.music.pause()
        bullentSound.stop()
    # hero的绘制
    # 每1/60s刷新一次画布
    mfontSurface1.score = hero.booldbar
    mfontSurface2.score = wingplance.booldbar
    mfontSurface1.refalshsurface()
    mfontSurface2.refalshsurface()
    winSurface.blit(mfontSurface1.surface, (10, 10))
    winSurface.blit(mfontSurface2.surface, (300, 10))
    winSurface.blit(mBtn.btnSurface, (400, 30))

    pygame.display.flip()
    clock.tick(60)

    # pygame.time.wait(1000)
    pass
