import pygame
pygame.init() #to do all the time at the beginning of the code

#Create window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

walk_right = [pygame.image.load('Golem_01_Walking_000.png'),
                pygame.image.load('Golem_01_Walking_001.png'),
                pygame.image.load('Golem_01_Walking_002.png'),
                pygame.image.load('Golem_01_Walking_003.png'),
                pygame.image.load('Golem_01_Walking_004.png'),
                pygame.image.load('Golem_01_Walking_005.png'),
                pygame.image.load('Golem_01_Walking_006.png'),
                pygame.image.load('Golem_01_Walking_007.png'),
                pygame.image.load('Golem_01_Walking_008.png'),
                pygame.image.load('Golem_01_Walking_009.png'),
                pygame.image.load('Golem_01_Walking_010.png'),
                pygame.image.load('Golem_01_Walking_011.png'),
                pygame.image.load('Golem_01_Walking_012.png'),
                pygame.image.load('Golem_01_Walking_013.png'),
                pygame.image.load('Golem_01_Walking_014.png'),
                pygame.image.load('Golem_01_Walking_015.png'),
                pygame.image.load('Golem_01_Walking_016.png'),
                pygame.image.load('Golem_01_Walking_017.png')
            ]

walk_left = [pygame.image.load('Golem_01_Walking_017.png'),
                pygame.image.load('Golem_01_Walking_016.png'),
                pygame.image.load('Golem_01_Walking_015.png'),
                pygame.image.load('Golem_01_Walking_014.png'),
                pygame.image.load('Golem_01_Walking_013.png'),
                pygame.image.load('Golem_01_Walking_012.png'),
                pygame.image.load('Golem_01_Walking_011.png'),
                pygame.image.load('Golem_01_Walking_010.png'),
                pygame.image.load('Golem_01_Walking_009.png'),
                pygame.image.load('Golem_01_Walking_008.png'),
                pygame.image.load('Golem_01_Walking_007.png'),
                pygame.image.load('Golem_01_Walking_006.png'),
                pygame.image.load('Golem_01_Walking_005.png'),
                pygame.image.load('Golem_01_Walking_004.png'),
                pygame.image.load('Golem_01_Walking_003.png'),
                pygame.image.load('Golem_01_Walking_003.png'),
                pygame.image.load('Golem_01_Walking_001.png'),
                pygame.image.load('Golem_01_Walking_000.png')
            ]
bg = pygame.image.load('Golem_01_Walking_000.png')
char = pygame.image.load('Golem_01_Walking_000.png')

screen_width = 500
screen_heigth = 500
x = 100
y = 100
width = 40
height = 60
vel = 5

is_jump = False
jump_count = 10
left = False
right = False
walk_count = 0

#all pygame programs have a main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
    if not(is_jump):
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < screen_heigth - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE] and y > vel:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
