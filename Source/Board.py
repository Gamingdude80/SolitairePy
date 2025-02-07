from pygame import Color

class Board():
    def __init__(self, color="green4"):
        self.bg = Color(color)
        self.slots = []

        for x in range(0,7):
            self.slots.append([])

    def draw_bg(self, screen):
        screen.fill(self.bg)

    def change_bg(self, color):
        self.bg.update(color)