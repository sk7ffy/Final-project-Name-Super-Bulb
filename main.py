from pygame import*
from button import Button
from sprite import Player
from sprite import Sprite
from enemy import Enemy
mixer.init()
mixer.music.load('328.mp3')
mixer.music.play()

main_win = display.set_mode((700,500))
display.set_caption('Super Bulb')
clock = time.Clock()
game = True
start_btn = Button(250,200,200,80,'start.png')
exit_btn = Button(250,400,200,100,'exit.png')
player = Player(100,200,50,50,'player.png')
enemy = Enemy(500,400,65,50,'amogus.png')
floor1 = Sprite(15,480,1000,200,'floor1.png')
island4 = Sprite(200,420,170,170,'island4.png')
island5 = Sprite(10,120,170,170,'island4.png')
island6 = Sprite(400,120,170,170,'island4.png')

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
        enemy.move()
        
        
        player.move()    
        player.jump()
        if player.is_jump == False:
            player.rect.y += 5

        if player.rect.colliderect(floor1.rect) :
            player.rect.bottom = floor1.rect.top
        enemy.draw(main_win)
        player.draw(main_win)
        floor1.draw(main_win)
        island4.draw(main_win)
        island5.draw(main_win)
        island6.draw(main_win)
        if player.rect.colliderect(island4.rect):
            player.rect.bottom = island4.rect.top
        if player.rect.colliderect(island5.rect):
            player.rect.bottom = island5.rect.top
        if player.rect.colliderect(island6.rect):
            player.rect.bottom = island6.rect.top
        if player.rect.colliderect(enemy.rect):
            print('Lose')
            player.rect.x = 70
            player.rect.y = 50



    else:
        main_win.fill((0,0,0))
        if start_btn.draw(main_win):
            run = True
        if exit_btn.draw(main_win):
            game = False
               

    display.update()
    clock.tick(120)







    