from pygame import*
from button import Button
from sprite import Player
from sprite import Sprite
main_win = display.set_mode((700,500))
display.set_caption('Super Bulb')
clock = time.Clock()
game = True
start_btn = Button(250,200,200,80,'start.png')
exit_btn = Button(250,400,200,100,'exit.png')
player = Player(100,200,50,50,'player.png')
floor = Sprite(15,380,1000,200,'floor.png')

bg = image.load('background.png')
bg=transform.scale(bg,(900,500))
run = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = not run
            if e.key == K_SPACE:
                player.is_jump = True
    if run:
        main_win.blit(bg,(-100,0))
        
        player.move()    
        player.jump()
        if player.is_jump == False:
            player.rect.y += 5

        if player.rect.colliderect(floor.rect) :
            player.rect.bottom = floor.rect.top
        player.draw(main_win)
        floor.draw(main_win)

    else:
        main_win.fill((0,0,0))
        if start_btn.draw(main_win):
            run = True
        if exit_btn.draw(main_win):
            game = False
               

    display.update()
    clock.tick(60)







    