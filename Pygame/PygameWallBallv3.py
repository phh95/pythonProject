import pygame,sys

pygame.init()

# 更改窗体的尺寸
size = width, height = 600, 400
speed = [1,1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame 壁球")

# 载入壁球图片
ball = pygame.image.load("PYG02-ball.gif")
# 将载入的图片绘制在矩形对象上
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

# 事件处理部分，书写小球的运动和反弹的代码
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)* int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)* int(speed[1]/abs(speed[1]))
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)