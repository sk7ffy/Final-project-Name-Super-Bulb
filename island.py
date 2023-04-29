class Island():
    def __init__(self,x,y,width,height):
        def __init__(self,x,y,width ,height,image_name):
        self.image=transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.jumpCount = 10
    def draw(self,window):
         window.blit(self.image,(self.rect.x,self.rect.y))