from pygame import*
from sprite import Sprite
class Enemy(Sprite):
    direction = "left"

    def move(self):
        if self.rect.x < 350:
            self.direction = 'right'
        if self.rect.x > 550:
            self.direction= 'left'
        
        if self.direction == 'left':
            self.rect.x -= 2
        else:
            self.rect.x += 2