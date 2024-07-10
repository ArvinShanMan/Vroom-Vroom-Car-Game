import pygame
import time
import random  # Import the random module

pygame.init()

crash_sound = pygame.mixer.Sound("237375__squareal__car-crash.wav")


pygame.display.set_caption("Vroom Vroom")

Width_Xaxis = 800
Height_Yaxis = 600

gameDisplay = pygame.display.set_mode((Width_Xaxis, Height_Yaxis))

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
bright_green = (0, 200, 0)
bright_red = (200, 0, 0)
crashed = False

car_width = 73

carImg = pygame.image.load('Vandi.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

# Game over text boundaries
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("OpenSans-BoldItalic.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((Width_Xaxis / 2), (Height_Yaxis / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((Width_Xaxis/2),(Height_Yaxis/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit)

        pygame.display.update()
        clock.tick(15) 
    

def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def paused():
    global pause
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((Width_Xaxis/2),(Height_Yaxis/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quit)

        pygame.display.update()
        clock.tick(15)  

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('RobotoCondensed-Bold.ttf', 115)
        TextSurf, TextRect = text_objects("Vroom Vroom", largeText)
        TextRect.center = ((Width_Xaxis / 2), (Height_Yaxis / 2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("START!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pause = False
    pygame.mixer.music.load('jazzboy.wav')
    pygame.mixer.music.play(-1)
    x = (Width_Xaxis * 0.45)
    y = (Height_Yaxis * 0.8)
    
    thing_starx = random.randrange(0, Width_Xaxis)
    thing_starty = -600
    thing_speed = 7 
    thing_width = 100
    thing_height = 100

    x_change = 0
    dodged = 0  # Initialize the dodged counter
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    x_change = -5
                elif event.key == pygame.K_RIGHT or event.key == ord("d"):
                    x_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    x_change = 0
                elif event.key == pygame.K_RIGHT or event.key == ord("d"):
                    x_change = 0   
                if event.key == pygame.K_p:
                    pause = True
                    paused()

        if pause:
            continue

        x += x_change

        gameDisplay.fill(white)
        things(thing_starx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)  # Display the dodged counter

        if x > Width_Xaxis - car_width or x < 0:
            crash()

        if thing_starty > Height_Yaxis:
            thing_starty = 0 - thing_height
            thing_starx = random.randrange(0, Width_Xaxis)
            dodged += 1
            thing_speed += 1  # Increase speed
            thing_width += (dodged * 1.2)  # Increase width

        # Check for collision
        if y < thing_starty + thing_height:
            if (x > thing_starx and x < thing_starx + thing_width) or (x + car_width > thing_starx and x + car_width < thing_starx + thing_width):
                crash()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Show the intro screen
game_intro()

# Start the game loop
game_loop()
