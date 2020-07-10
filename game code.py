import pygame
import random
import os

pygame.init()

#For Adding music
#pygame.mixer.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,1)
orange = (255,255,0)
marroon = (115,0,0)
lime = (220,255,250)
pink = (150,250,240)
purple = (240,0,255)


# Creating window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# For background image
#bg = pygame.image.load("image name.jpg")
#bg = pygame.transform.scale(bg, (screen_width, screen_height)).convert_alpha


# Game Title
pygame.display.set_caption("THE SNAKE GAME")
pygame.display.update()
clock = pygame.time.Clock()


#font size
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

size = pygame.font.SysFont(None, 200)
def textscreen(text, color, x, y):
    screentext = size.render(text, True, color)
    gameWindow.blit(screentext, [x,y])

textsize = pygame.font.SysFont(None, 35)
def txtscreen(text, color, x, y):
    scrtext = textsize.render(text, True, color)
    gameWindow.blit(scrtext, [x,y])

# For increasing snake length
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# For starting screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(orange)

        text_screen("THE", blue, 80, 150)
        textscreen("SNAKE", marroon, 100, 200)
        text_screen("GAME", blue, 550, 330)
        txtscreen("PRESS SPACE TO CONTINUE...", purple, 200,510)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        gameloop()
        pygame.display.update()
        clock.tick(30)


# Main Game Loop
def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 40
    snk_x = 50
    snk_y = 50
    velocity_x = 0
    velocity_y = 0
    radius = 10
    apple = random.randint(100, 700)
    berry = random.randint(100, 500)
    score = 0
    move_velocity = 3
    fps = 30
    snake_size = 20
    snake_list = []
    snake_length = 1


#check highscore file is exit or not
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

# open file for read
    file = open ("highscore.txt", "r")
    high_score =  file.read()
    file.close()


#For game window
    while not exit_game:

        if game_over:
        # Add new high score
            with open("highscore.txt", "w") as f:
                f.write(str(high_score))
        # Game over window
            gameWindow.fill(lime)
            textscreen("GAME", marroon, 80, 90)
            textscreen("OVER", marroon, 330, 240)
            txtscreen("PRESS ENTER TO RESTART", blue, 200, 470)
            for event in pygame.event.get():
             # For quit game
                if event.type == pygame.QUIT:
                    exit_game = True

            # for restart game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
            # For quit game
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                #For control the game
                    if event.key == pygame.K_RIGHT:
                        velocity_x = move_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - move_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - move_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = move_velocity
                        velocity_x = 0


        # For moving the snake
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            snk_x = snk_x + velocity_x
            snk_y = snk_y + velocity_y

        # scoring stage

            if score % 20 == 19:
                if abs(snk_x - apple) < 8 and abs(snk_y - berry) < 8:
                    score += 10
                    apple = random.randint(20, 500)
                    berry = random.randint(20, 400)
                    fps += 5
                    snake_length += 10
                    if score>int(high_score):
                        high_score = score
            else:
                if abs(snk_x - apple) < 8 and abs(snk_y - berry) < 8:
                    score +=1
                    apple = random.randint(20, 500)
                    berry = random.randint(20, 400)
                    fps += 1
                    snake_length +=10
                    if score>int(high_score):
                        high_score = score

        # For snake background screen
            gameWindow.fill(green)
        # show background image on screen
        # gameWindow.blit(bg, (0,0))

            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("High Score: " + str(high_score), red, 480, 5)


        # food type
            if score % 20 ==19:
                pygame.draw.circle(gameWindow, red, [apple, berry], 9)
            else:
                pygame.draw.circle(gameWindow, blue, [apple, berry], 7)



        # Snake body
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]

        # when snake touch itself
            if head in snake_list[:-1]:
                game_over = True

        # when snake touch boundary
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height \
                    or snk_x<0 or snk_x>screen_width or snk_y<0 or snk_y>screen_height:
                game_over = True
        # snake formed here
            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.draw.circle(gameWindow, yellow, [snk_x, snk_y], radius)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
