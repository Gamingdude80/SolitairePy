import pygame

class Card(pygame.sprite.Sprite):
    spritesheet = "Sprites\PC Computer - Solitaire - Cards.jpg"

    def __init__(self, suit, card_val, card_width=71, card_height=96):
        pygame.sprite.Sprite.__init__(self)

        self.suit = suit
        self.card_val = card_val
        self.card_width = card_width
        self.card_height = card_height
        self.sprite = self._get_sprite(suit, card_val, card_width, card_height)

    def draw_card(self, screen, x_pos, y_pos, scale=1):
        if scale != 1:
            screen.blit(pygame.transform.scale(self.sprite, (self.card_width * scale, self.card_height * scale)), (x_pos, y_pos))
        else:
            screen.blit(self.sprite, (x_pos, y_pos))

    def _get_sprite(self, suit, card_val, card_width, card_height):
        #Loads in the entire sprite sheet
        sheet = pygame.image.load(self.spritesheet).convert_alpha()
        sprite_x = 11
        sprite_y = 4
        special_cards = ['A', 'K', 'Q', "J"]
        types_of_cards = ["SPADES", "HEARTS", "CLUBS", "DIAMONDS", "BACK1", "BACK2"]

        #Uses the card's value to know the column
        if card_val.isdigit():
            sprite_x = int(card_val) - 1
        else:
            match card_val:
                case "A":
                    sprite_x = 0
                case "J":
                    sprite_x = 10
                case "Q":
                    sprite_x = 11
                case "K":
                    sprite_x = 12

        #Uses the suit to get the row to search in
        if suit.upper() in types_of_cards:
            sprite_y = types_of_cards.index(suit.upper())
        
        #Cuts out the sprite at the specific x, y position based on the width and height of the card
        sheet.set_clip(pygame.Rect(sprite_x * card_width, sprite_y * card_height, card_width, card_height))

        #Where the actual card sprite is grabbed after the sprite is cut out
        sprite = sheet.subsurface(sheet.get_clip())
        return sprite