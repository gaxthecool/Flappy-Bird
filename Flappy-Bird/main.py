#initializing needed modules and screen display
import pygame
import random
import asyncio
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load('Flappy-Bird/frame-1.png')
pygame.display.set_icon(icon)

# defining the variables used the game
playerImg1 = pygame.transform.scale(pygame.image.load('Flappy-Bird/frame-1.png'), (40, 40))
bgImg = pygame.image.load("Flappy-Bird/bg.png")
pipes = pygame.image.load("Flappy-Bird/pipes.png")
pipes2 = pygame.image.load("Flappy-Bird/pipes copy.png")
pipes3 = pygame.image.load('Flappy-Bird/pipes2.png')
pipes4 = pygame.image.load('Flappy-Bird/pipes2 copy.png')
bgImgScaled = pygame.transform.scale(bgImg, (800, 800))
playerX = 50
playerY = 480
pipe_y = random.randint(-400, -200)
pipe_x = 400
pipe2_y = pipe_y + 900
pipe2_x = 400
pipe3_y = random.randint(-400, -200)
pipe3_x = 800
pipe4_y = pipe3_y + 900
pipe4_x = 800
playerY_change = 0
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("Monaco", 20)
text_font_end = pygame.font.SysFont("Monaco", 10)
game_speed = 6
pipes_moving = False
pipes2_moving = False
pipes3_moving = False
pipes4_moving = False
pipe_dir = 1
bird_speed = 8
pipe1_number = 0
pipe2_number = 0
game_start = 0
player_rect = playerImg1.get_rect(center=(playerX, playerY))
pipe1_rect = pipes.get_rect(center=(pipe_x, pipe_y))
pipe2_rect = pipes2.get_rect(center=(pipe2_x, pipe2_y))
pipe3_rect = pipes3.get_rect(center=(pipe3_x, pipe3_y))
pipe4_rect = pipes4.get_rect(center=(pipe4_x, pipe4_y))
pygame.mixer.music.load('Flappy-Bird/FlappyBirdMusic.ogg')
pygame.mixer.music.play(-1)
button_font = pygame.font.SysFont("Monaco", 15)
# frame assets
bronze = pygame.transform.scale(pygame.image.load('Flappy-Bird/bronze.png'), (128, 128))
gold = pygame.transform.scale(pygame.image.load('Flappy-Bird/gold.png'), (128, 128))
silver = pygame.transform.scale(pygame.image.load('Flappy-Bird/silver.png'), (128, 128))
none = pygame.transform.scale(pygame.image.load('Flappy-Bird/none_medal.png'), (128, 128))
platinum = pygame.transform.scale(pygame.image.load('Flappy-Bird/platinum.png'), (128, 128))
end_frame = pygame.transform.scale(pygame.image.load('Flappy-Bird/EndGame_frame (1).png'), (300, 256))
restart_button_surface = pygame.image.load('Flappy-Bird/restartgame.png')
restart_button_rect = restart_button_surface.get_rect()
restart_button_rect.topleft = (400, 250)

#debug
end_pipe_touching = ''
rep = 0
# functions used to draw sprites on the screen
def player():
    screen.blit(playerImg1, player_rect)


def bg(x, y):
    screen.blit(bgImgScaled, (x, y))


def pipes_1():
    screen.blit(pipes, pipe1_rect)


def pipes_2():
    screen.blit(pipes2, pipe2_rect)


def pipes_3():
    screen.blit(pipes3, pipe3_rect)


def pipes_4():
    screen.blit(pipes4, pipe4_rect)


def draw_text(text, font, color, x, y):
    txt_img = font.render(text, True, color)
    screen.blit(txt_img, (x, y))

# game logic
running = True
game_over = False

async def main():
    global rep
    global game_start
    global running
    global player_rect
    global playerY_change
    global game_over
    global pipe1_number
    global pipe2_number
    global end_pipe_touching
    global pipes_moving, pipes2_moving, pipes3_moving, pipes4_moving
    while True:
        bg(0, 0)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # detecting for any keys pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_start += 1
                    playerY_change = 0 - bird_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    playerY_change = bird_speed

            if game_over == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        playerY_change = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        playerY_change = 0
                if restart_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
                    if event.key == pygame.K_UP:
                        game_start += 1
                        playerY_change = 0 - bird_speed

        # establishes a starting screen
        if game_start == 0:
            if rep == 0:
                draw_text('Welcome to Flappy Bird!', text_font, (0, 0, 255), 20, 30)
                draw_text('Press the Up Arrow Key to Start!', text_font, (0, 0, 255), 20, 50)
            player_rect.y = 480
        if game_start == 1:
            if rep == 0:
                draw_text('Welcome to Flappy Bird!', text_font, (135, 206, 235), 20, 30)
                draw_text('Press the Up Arrow Key to Start!', text_font, (135, 206, 235), 20, 50)
            pipes_moving = True
            pipes2_moving = True
            pipes3_moving = True
            pipes4_moving = True

        # game over conditions; checks if the game should be over based on if the player collides with the pipes
        if pipe1_number > 0:
            if player_rect.colliderect(pipe1_rect):
                end_pipe_touching = 'pipe1'
                player_rect.x += 100
                player_rect.y = 800
            elif player_rect.colliderect(pipe2_rect):
                end_pipe_touching = 'pipe2'
                player_rect.x += 100
                player_rect.y = 800

        if player_rect.colliderect(pipe3_rect):
            end_pipe_touching = 'pipe3'
            player_rect.x += 100
            player_rect.y = 800
        elif player_rect.colliderect(pipe4_rect):
            end_pipe_touching = 'pipe4'
            player_rect.x += 100
            player_rect.y = 800

        if player_rect.y <= 0:
            game_over = True
            pipes_moving = False
            pipes2_moving = False
            pipes3_moving = False
            pipes4_moving = False
        elif player_rect.y >= 800:
            game_over = True
            pipes_moving = False
            pipes2_moving = False
            pipes3_moving = False
            pipes4_moving = False

        # these pieces of code are enabling pipe movement
        if pipes_moving:
            pipe1_rect.x -= game_speed * pipe_dir
            if pipe1_rect.x < 0:
                pipe1_rect.y = random.randint(-400, -200)
                pipe1_number += 1
                if pipe1_number % 2 == 1:
                    pipe1_rect.x = 800
                elif pipe1_number % 2 == 0:
                    pipe1_rect.x = 800
        if pipes2_moving:
            pipe2_rect.x -= game_speed * pipe_dir
            if pipe2_rect.x < 0:
                pipe2_rect.y = pipe1_rect.y + 900
                if pipe1_number % 2 == 1:
                    pipe2_rect.x = 800
                elif pipe1_number % 2 == 0:
                    pipe2_rect.x = 800
        if pipes3_moving:
            pipe3_rect.x -= game_speed * pipe_dir
            if pipe3_rect.x < 0:
                pipe3_rect.y = random.randint(-400, -200)
                pipe2_number += 1
                if pipe2_number % 2 == 1:
                    pipe3_rect.x = 800
                elif pipe2_number % 2 == 0:
                    pipe3_rect.x = 800
        if pipes4_moving:
            pipe4_rect.x -= game_speed * pipe_dir
            if pipe4_rect.x < 0:
                pipe4_rect.y = pipe3_rect.y + 900
                if pipe2_number % 2 == 1:
                    pipe4_rect.x = 800
                elif pipe2_number % 2 == 0:
                    pipe4_rect.x = 800
        player_rect.y += playerY_change
        player()
        if pipe1_number > 0:
            pipes_1()
            pipes_2()
        pipes_3()
        pipes_4()
        draw_text(f'Score: {pipe1_number + pipe2_number}', text_font, (0, 0, 255), 20, 0)

        # end game logic
        if game_over == True:
            print(end_pipe_touching)
            rep += 1
            pipes_moving = False
            pipes2_moving = False
            pipes3_moving = False
            pipes4_moving = False
            playerY_change = 0
            draw_text('Game Over!', text_font, (255, 0, 0), 350, 0)
            if pipe1_number + pipe2_number < 10:
                screen.blit(end_frame, (210, 210))
                screen.blit(none, (230, 230))
                draw_text('The bird is still warming up. Try again!', text_font_end, (0,0,0), 230, 370)
            elif pipe1_number + pipe2_number >= 10 and pipe1_number + pipe2_number < 30:
                screen.blit(end_frame, (210, 210))
                screen.blit(bronze, (230, 230))
                draw_text('Not bad! Those pipes are starting to fear you.', text_font_end, (0, 0, 0), 230, 370)
            elif pipe1_number + pipe2_number >= 30 and pipe1_number + pipe2_number < 50:
                screen.blit(end_frame, (210, 210))
                screen.blit(silver, (230, 230))
                draw_text("Looking good! You're flying with confidence.", text_font_end, (0, 0, 0), 230, 370)
            elif pipe1_number + pipe2_number >= 50 and pipe1_number + pipe2_number < 70:
                screen.blit(end_frame, (210, 210))
                screen.blit(gold, (230, 230))
                draw_text("Amazing! You've mastered the skies.", text_font_end, (0, 0, 0), 230, 370)
            elif pipe1_number + pipe2_number >= 70:
                screen.blit(end_frame, (210, 210))
                screen.blit(platinum, (230, 230))
                draw_text("Unstoppable! The pipes never stood a chance.", text_font_end, (0, 0, 0), 230, 370)
            screen.blit(restart_button_surface, (400, 250))
            pygame.mixer.music.stop()
            if restart_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
                pygame.mixer.music.play(-1)
                pipe1_number = 0
                pipe2_number = 0
                playerX = 150
                playerY = 480
                player_rect = playerImg1.get_rect(center=(playerX, playerY))
                game_over = False
                game_start = 0
                if game_start == 1:
                    pipes2_moving = True
                    pipes3_moving = True
                    pipes4_moving = True
        pygame.display.update()
        clock.tick(60)

        await asyncio.sleep(0)

asyncio.run(main())