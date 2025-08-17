import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("简易马里奥")

WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 200, 0)

clock = pygame.time.Clock()
player_x, player_y = 100, 300
player_width, player_height = 40, 50
player_vel_x = 0
player_vel_y = 0
gravity = 0.5
jump_power = -10
on_ground = False
ground_y = 350

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel_x = -5
    elif keys[pygame.K_RIGHT]:
        player_vel_x = 5
    else:
        player_vel_x = 0

    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_power
        on_ground = False

    player_vel_y += gravity
    player_x += player_vel_x
    player_y += player_vel_y

    if player_y + player_height >= ground_y:
        player_y = ground_y - player_height
        player_vel_y = 0
        on_ground = True

    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, HEIGHT - ground_y))
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
