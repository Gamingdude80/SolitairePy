import pygame
import configparser

from Board import Board
from CardStack import CardStack
from Card import Card, Suits, Faces, Backs

#Importing the config settings
card_config = configparser.ConfigParser()
card_config.read_file(open("config\config.cfg"))

card_width = int(card_config["CARDS"]["card_width"])
card_height = int(card_config["CARDS"]["card_height"])
card_scale = float(card_config["CARDS"]["card_scale"])

# pygame setup
pygame.init()
screen = pygame.display.set_mode((int(card_config["SCREEN"]["screen_width"]), 
                                  int(card_config["SCREEN"]["screen_height"])))
clock = pygame.time.Clock()
fps = int(card_config["SCREEN"]["fps"])
running = True
card_sprites = card_config["SPRITES"]["card_sprite_sheet"]

#Makes the board
board = Board((0,99,0))

#making the cards
draw_pile = CardStack(card_width, card_height, card_sprites) 
discard_pile = CardStack(card_width, card_height, card_sprites)

for x in range(0,4):
    for y in range(0,13):
        temp_card = Card(Suits(x).name, str(y + 1), card_width, card_height, card_sprites)
        draw_pile.add_card(temp_card)

#Drawing the board
board.draw_bg(screen)

#Drawing the stacks/piles
draw_pile.display_stack(screen, 20, 20, scale=card_scale)

#Drawing all the cards
collumn_height = 0
for x in range(1,8):
    collumn_height += 1
    for y in range(0,collumn_height):
        draw_pile.draw_card().display_card(screen, 130 * (x - 1) + 50, 200 + (y * 50), scale=card_scale)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    #Sets the fps of the game
    clock.tick(fps)

pygame.quit()