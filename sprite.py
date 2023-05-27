from pygame import*
class Sprite(sprite.Sprite):
    def __init__(self,x,y,width ,height,image_name):
        self.image=transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.jumpCount = 10
    def draw(self,window):
         window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 2
        if keys[K_RIGHT]:
            self.rect.x += 2
        
        
    def jump(self):
        if self.is_jump:
            if self.jumpCount >= -1:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.is_jump = False
                self.jumpCount = 8