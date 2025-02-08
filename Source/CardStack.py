import pygame
from Card import Card, Backs

class CardStack:
    def __init__(self, card_width, card_height, spritesheet):
        self.cards = []
        self.card_width = card_width
        self.card_height = card_height
        self.spritesheet = spritesheet
        self.sprite = self._get_sprite()

    def add_card(self, card:Card):
        self.cards.append(card)

    def draw_card(self, suit=None, card_value=None):
        try:
            if suit and card_value:
                for card in self.cards:
                    if card.suit == suit and card.card_val == card_value:
                        return(self.cards.pop(self.cards.index(card)))
                raise IndexError
            else:
                return(self.cards.pop())
        except IndexError:
            return None
        
    def display_stack(self, screen, x_pos, y_pos, scale=1):
        if scale != 1:
            screen.blit(pygame.transform.scale(self.sprite, (self.card_width * scale, self.card_height * scale)), (x_pos, y_pos))
        else:
            screen.blit(self.sprite, (x_pos, y_pos))

    def _get_sprite(self):
        #Loads in the entire sprite sheet
        sheet = pygame.image.load(self.spritesheet).convert_alpha()

        if len(self.cards) == 0:
            stack_back = Backs.YES
        else:
            stack_back = Backs.DEFAULT
            
        #Cuts out the sprite at the specific x, y position based on the width and height of the card
        sheet.set_clip(pygame.Rect(stack_back.value[0] * self.card_width,
                                   stack_back.value[1] * self.card_height,
                                   self.card_width,
                                   self.card_height))

        #Where the actual card sprite is grabbed after the sprite is cut out
        sprite = sheet.subsurface(sheet.get_clip())
        return sprite