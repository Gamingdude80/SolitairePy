import pygame
from Card import Card
from Board import Board 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
fps = 1
running = True

#Makes the board
board = Board((0,149,83))

suits = ["SPADES", "HEARTS", "CLUBS", "DIAMONDS"]

#making the cards
card_pile = [] 
used_cards = []
for x in range(0,4):
    for y in range(0,13):
        temp_card = Card(suits[x], str(y + 1))
        card_pile.append(temp_card)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Drawing the board
    board.draw_bg(screen)

    #Drawing all the cards
    collumn_height = 0
    for x in range(1,8):
        collumn_height += 1
        for y in range(0,collumn_height):
            card_pile[y+x-1].draw_card(screen, 130 * (x - 1) + 50, 200 + (y * 50), scale=1.5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    #Sets the fps of the game
    clock.tick(fps)

pygame.quit()