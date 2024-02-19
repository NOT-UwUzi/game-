# Simple pygame program

# Import and initialize the pygame library
import pygame
import math
pygame.init()

# Set up sprites
slime_forward_1 = pygame.image.load("Assets\Slime\slime_forward_1.png")
slime_forward_2 = pygame.image.load("Assets\Slime\slime_forward_2.png")
slime_forward_3 = pygame.image.load("Assets\Slime\slime_forward_3.png")

slime_left_1 = pygame.image.load("Assets\Slime\slime_left_1.png")
slime_left_2 = pygame.image.load("Assets\Slime\slime_left_2.png")
slime_left_3 = pygame.image.load("Assets\Slime\slime_left_3.png")
slime_left_4 = pygame.image.load("Assets\Slime\slime_left_4.png")

slime_right_1 = pygame.image.load("Assets\Slime\slime_right_1.png")
slime_right_2 = pygame.image.load("Assets\Slime\slime_right_2.png")
slime_right_3 = pygame.image.load("Assets\Slime\slime_right_3.png")
slime_right_ 4= pygame.image.load("Assets\Slime\slime_right_4.png")

basic_block = pygame.image.load("Assets\Blocks\Basic_block.png")
deco_block = pygame.image.load("Assets\Blocks\deco_block.png")
one_way_left = pygame.image.load("Assets\Blocks\one_way_left.png")
one_way_right = pygame.image.load("Assets\Blocks\one_way_right.png")

poison_indiv = pygame.image.load("Assets\Obstacles\Poison\poison_indiv.png")
poison_left = pygame.image.load("Assets\Obstacles\Poison\poison_left.png")
poison_middle = pygame.image.load("Assets\Obstacles\Poison\poison_middle.png")
poison_right = pygame.image.load("Assets\Obstacles\Poison\poison_right.png")

spike_upside_indiv = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_indiv.png")
spike_upside_left = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_left.png")
spike_upside_middle = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_middle.png")
spike_upside_right = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_right.png")

spike_upside_indiv = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_indiv.png")
spike_upside_left = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_left.png")
spike_upside_middle = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_middle.png")
spike_upside_right = pygame.image.load("Assets\Obstacles\Spikes\spike_upside_right.png")

# lava_flowing = pygame.image.load("Assets\Obstacles\Lava\lava_flowing.png")

gravity_up = pygame.image.load("Assets\Obstacles\Gravity\gravity_up.png")
gravity_down = pygame.image.load("Assets\Obstacles\Gravity\gravity_down.png")

# game_menu = pygame.image.load("Assets\GUI\game_menu.png")
# gravity_bar = pygame.image.load("Assets\GUI\gravity_bar.png")
# button = pygame.image.load("Assets\GUI\button.png")

level1 = pygame.image.load("Assets\Levels\level1.png")
# level2 = pygame.image.load("Assets\Levels\level2.png")
# level3 = pygame.image.load("Assets\Levels\level3.png")
# level4 = pygame.image.load("Assets\Levels\level4.png")
# level5 = pygame.image.load("Assets\Levels\level5.png")
# level6 = pygame.image.load("Assets\Levels\level6.png")
# level7 = pygame.image.load("Assets\Levels\level7.png")
# level8 = pygame.image.load("Assets\Levels\level8.png")
# level9 = pygame.image.load("Assets\Levels\level9.png")
# boss = pygame.image.load("Assets\Levels\level10.png")

#level_list = [game_menu, level1, level2, level3, level4, level5, level6, level7, level8, level9, boss]

# Set up the drawing window
level = 0
#current_level = level_list[level]
#if button_pressed == true:
screen = pygame.display.set_mode([500, 500])
velocity = 7.5
class char(object):  # represents the chara cter, not the game
    def __init__(self):
        """ The constructor of the class """
        #self.image = pygame.image.load(img_path) #NOT SURE WHAT IM COOKING PLEASE HELP
        # the position
        self.x = 0
        self.y = 0



        
x = 20
y = 480

# Run until the user asks to quit
isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the background with white

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x>0:
        x -= velocity
    elif keys[pygame.K_RIGHT] and x < 480:
        x += velocity
    

    if(isJump == False): 
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * velocity/40
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    screen.fill((0, 0, 0)) 


    pygame.draw.rect(screen, (255, 0, 0), (x, y, 20, 20)) 

    pygame.display.update()


pygame.quit()
