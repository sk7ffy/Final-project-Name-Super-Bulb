from pygame import*
from button import Button
from sprite import Player
from sprite import Sprite
from enemy import Enemy
from time import sleep
mixer.init()
mixer.music.load('328.mp3')
mixer.music.play()
score = 0
mixer.music.load('deadsound.mp3')

main_win = display.set_mode((700,500))
font.init()
font = font.SysFont("Arial", 32)
text = font.render('Treasure:'+str(score) ,True, (0, 98, 255))
text2 = font.render('Lose', True, (255, 0, 4))
display.set_caption('Super Bulb')
clock = time.Clock()
game = True
start_btn = Button(250,200,200,200,'start.png')
exit_btn = Button(250,400,200,100,'exit.png')
player = Player(100,200,50,50,'player.png')
enemy = Enemy(300,410,45,50,'amogus.png')
floor1 = Sprite(15,480,1000,200,'floor1.png')
island4 = Sprite(200,420,170,170,'island4.png')
island5 = Sprite(10,120,170,170,'island4.png')
island6 = Sprite(400,120,170,170,'island4.png')
treasure1 = Sprite(100,400,100,100,'treasure.png')
treasure2 = Sprite(500,200,100,100,'treasure.png')
treasure3 = Sprite(300,400,100,100,'treasure.png')

bg = image.load('background.png')
bg=transform.scale(bg,(900,500))
bg2 = image.load('buts.jpg')
bg2 = transform.scale(bg2,(900,500))


run = False
level = 0

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
        text = font.render('Treasure:'+str(score) ,True, (0, 98, 255))

        main_win.blit(text,(0,50))

        treasure1.draw(main_win)
        treasure2.draw(main_win)
        treasure3.draw(main_win)
        
        

        
            
        
        
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
            main_win.blit(text2,(0,220))
            mixer.music.play()
            display.update()
            sleep(1)
            player.rect.x = 70
            player.rect.y = 50
        if player.rect.colliderect(treasure1.rect):
            score = score + 1
            treasure1.rect.x = 800
        if player.rect.colliderect(treasure2.rect):
            score = score + 1
            treasure2.rect.x = 800
        if player.rect.colliderect(treasure3.rect):
            score = score + 1
            treasure3.rect.x = 800



    else:
        main_win.blit(bg2,(-100,0))
        if start_btn.draw(main_win):
            run = True
        if exit_btn.draw(main_win):
            game = False
               

    display.update()
    clock.tick(120)







    