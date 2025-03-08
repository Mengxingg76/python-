import pygame
import random
import copy
import os
# 🐍的点
snakeList=[[10,10]]
# 🍎的点
foodPoint = [random.randint(60,490),random.randint(60,490)]
# 移动方向
moveUp = False
moveDown = True
moveLeft = False
moveRight = False
moveSpeed = 10
# 分数获取
score = 0
upScore = 1
### 游戏初始化
pygame.init()
# 设置游戏字体
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)

# 设置游戏刷新帧率
clock = pygame.time.Clock()
# 设置屏幕大小
screen = pygame.display.set_mode((500,500))
#绘制标题
pygame.display.set_caption('贪吃蛇小游戏')
background = pygame.image.load("./python/贪吃蛇/grass.jpg")  # 确保图片路径正确
# background = pygame.transform.scale(background, (500, 500))  # 调整图片大小以适应屏幕
### 进入游戏
# 游戏暂停开关
gameSwitch = True
while gameSwitch :
    # 设置FPS帧率
    clock.tick(24)
    #加载导入的图片
    screen.blit(background, (0, 0))  # 将背景图片绘制到屏幕左上角
    # 渲染分数文本
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # 白色文本

    background_rect = pygame.Rect(0, 0, 500, 50)  # 矩形位置和大小
    pygame.draw.rect(screen, (255, 255, 255), background_rect)  # 绘制蓝色背景矩形

    screen.blit(score_text, (10, 10))  # 将分数文本绘制到屏幕左上角

    # 使用键盘控制🐍的移动方向
    for event in pygame.event.get():
        # 判断按键是否按下 再判断按键类型
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and moveDown == False:
                moveUp = True
                moveLeft = False
                moveRight = False
            elif event.key == pygame.K_DOWN and moveUp == False:
                moveDown = True
                moveLeft = False
                moveRight = False   
            elif event.key == pygame.K_LEFT and moveRight == False:
                moveUp = False
                moveDown = False
                moveLeft = True
            elif event.key == pygame.K_RIGHT and moveLeft == False:
                moveUp = False
                moveDown = False
                moveRight = True
            elif event.key == pygame.K_ESCAPE :
                gameSwitch = False
    # 绘制🍎
    foodRect = pygame.draw.circle(screen,[255,0,0],foodPoint,10,0)

    # 绘制🐍
    snakeRect = []
    for snakePoint in snakeList :
        snakeRect.append(pygame.draw.circle(screen,[0,255,0],snakePoint,5,0))
        # 检测🐍和🍎体积碰撞
        if foodRect.collidepoint(snakePoint) :
            snakeList.append(foodPoint)
            # 重新生成食物
            foodPoint = [random.randint(60,490),random.randint(60,490)]
            score+=upScore
            upScore+=1
            break

    ## 移动 修改🐍的位置
    snakeLen = len(snakeList) -1

    while snakeLen > 0:
        # 把后面的点往前面移动
        snakeList[snakeLen] = copy.deepcopy(snakeList[snakeLen-1])
        snakeLen -=1

    # 🐍头单独处理
    if moveDown:
        snakeList[0][1]+=moveSpeed
        if snakeList[0][1] > 500:
            snakeList[0][1] = 50
    elif moveUp:
        snakeList[0][1]-=moveSpeed
        if snakeList[0][1] < 50:
            snakeList[0][1] = 500
    elif moveLeft:
        snakeList[0][0]-=moveSpeed
        if snakeList[0][0] < 0:
            snakeList[0][0] = 500
    elif moveRight:
        snakeList[0][0]+=moveSpeed
        if snakeList[0][0] > 500:
            snakeList[0][0] = 0   

    # 🐍头碰到🐍身 结束游戏
    headRect = snakeRect[0]
    count = len(snakeRect)
    while count > 1:
        if headRect.colliderect(snakeRect[count - 1]):
            # 游戏结束
            gameSwitch = False
        count -=1

    
    # 显示屏幕
    pygame.display.update()

print("游戏结束!",score,"分")
pygame.quit()