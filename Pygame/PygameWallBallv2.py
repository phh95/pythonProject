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
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)


