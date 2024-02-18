# Simple pygame program

# Import and initialize the pygame library
import pygame
import math
pygame.init()

# Set up sprites
# character = pygame.image.load("Assets\Character\char_forward.png")
# character_left1 = pygame.image.load("Assets\Character\char_left1.png")
# character_left2 = pygame.image.load("Assets\Character\char_left2.png")
# character_right1 = pygame.image.load("Assets\Character\char_right1.png")
# character_right2 = pygame.image.load("Assets\Character\char_right2.png")
# character_death = pygame.image.load("Assets\Character\char_dead.png")

basic_block = pygame.image.load("Assets\Blocks\basic_block.png")
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

# gravity_up = pygame.image.load("Assets\Obstacles\Gravity\gravity_up.png")
# gravity_down = pygame.image.load("Assets\Obstacles\Gravity\gravity_down.png")
#
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

level_list = [game_menu, level1, level2, level3, level4, level5, level6, level7, level8, level9, boss]

# Set up the drawing window
level = 0
current_level = level_list[level]
if button_pressed == true:
    level += 1
screen = pygame.display.set_mode([500, 500])
velocity = 20

class char(object):  # represents the chara cter, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(img_path) #NOT SURE WHAT IM COOKING PLEASE HELP
        # the position
        self.x = 0
        self.y = 0

def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
    
        if key[pygame.K_UP]: # up key
            self.y -= dist # move up
        elif key[pygame.K_SPACE] and y < 480 and air == False:
            air = True
        else: # let gravity exist
            self.y += dist # go down
        
        if(isJump == False): 
            if key[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * velocity/20
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        

def draw(self, surface): #self is char, surface is background
    """ Draw on surface """
    # blit yourself at your current position
    surface.blit(self.image, (self.x, self.y))

# Run until the user asks to quit
run = True
while run:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(15)

    # First game menu
    gameDisplay.blit(game_menu, (0,0))

    # Sprites
    screen.blit(char, (0,0))
    pygame.display.update()

pygame.quit()
