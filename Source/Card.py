import pygame
from enum import Enum

class Card(pygame.sprite.Sprite):
    def __init__(self, suit, card_val, card_width, card_height, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.card_val = card_val
        self.card_width = card_width
        self.card_height = card_height
        self.spritesheet = spritesheet
        self.sprite = self._get_sprite(suit, card_val, card_width, card_height)

    def display_card(self, screen, x_pos, y_pos, scale=1):
        if scale != 1:
            screen.blit(pygame.transform.scale(self.sprite, (self.card_width * scale, self.card_height * scale)), (x_pos, y_pos))
        else:
            screen.blit(self.sprite, (x_pos, y_pos))

    def _get_sprite(self, suit, card_val, card_width, card_height):
        #Loads in the entire sprite sheet
        sheet = pygame.image.load(self.spritesheet).convert_alpha()
        sprite_x = 11
        sprite_y = 4

        #Uses the card's value to know the column
        if card_val.isdigit():
            sprite_x = int(card_val) - 1
        else:
            match card_val:
                case "A":
                    sprite_x = Faces.ACE.value
                case "J":
                    sprite_x = Faces.JACK.value
                case "Q":
                    sprite_x = Faces.QUEEN.value
                case "K":
                    sprite_x = Faces.KING.value

        #Uses the suit to get the row to search in
        sprite_y = Suits[suit.upper()].value
        
        #Cuts out the sprite at the specific x, y position based on the width and height of the card
        sheet.set_clip(pygame.Rect(sprite_x * card_width, sprite_y * card_height, card_width, card_height))

        #Where the actual card sprite is grabbed after the sprite is cut out
        sprite = sheet.subsurface(sheet.get_clip())
        return sprite
    
class Backs(Enum):
    DEFAULT = (12,4)
    YES = (10,4)
    NO = (11,4)
    WEAVE1 = (0,4)
    WEAVE2 = (1,4)

class Suits(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3
    BACK1 = 4
    BACK2 = 5

class Faces(Enum):
    ACE = 0
    JACK = 10
    QUEEN = 11
    KING = 12