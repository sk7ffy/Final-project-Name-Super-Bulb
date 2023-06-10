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
hit = False
main_win = display.set_mode((1300,500))
font.init()
font = font.SysFont("Arial", 32)
text = font.render('Treasure:'+str(score) ,True, (0, 98, 255))
text3 =font.render('Winner',True, (0, 98, 255))
text2 = font.render('Lose', True, (255, 0, 4))
text4 = font.render('Lvl:2', True, (255, 0, 4))
display.set_caption('Super Bulb')
clock = time.Clock()
game = True
start_btn = Button(550,200,200,200,'start.png')
exit_btn = Button(550,400,200,100,'exit.png')
player= Player(100,200,50,50,'player111.png')
enemy = Enemy(300,410,45,50,'enemy3.png')
enemy2 = Enemy(200,230,45,50,'enemy3.png')
floor1 = Sprite(15,480,1500,200,'floor1.png')
islan = Sprite(200,227,150,50,'islan.png')
island5 = Sprite(10,320,150,50,'islan.png')
island6 = Sprite(500,270,150,50,'islan.png')
treasure1 = Sprite(100,400,70,70,'treasure.png')
treasure2 = Sprite(500,200,70,70,'treasure.png')
treasure3 = Sprite(300,140,70,70,'treasure.png')
treasure4 = Sprite(1100,100,70,70,'treasure.png')
islan2 = Sprite(1000,180,150,50,'islan.png')
islan3 = Sprite(780,350,150,50,'islan.png')

bg = image.load('background.png')
bg=transform.scale(bg,(1500,500))
bg2 = image.load('buts.jpg')
bg2 = transform.scale(bg2,(1500,500))

bullets = sprite.Group()

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
        enemy2.move()
        text = font.render('Treasure:'+str(score) ,True, (0, 98, 255))

        main_win.blit(text,(0,50))

        treasure1.draw(main_win)
        treasure2.draw(main_win)
        treasure3.draw(main_win)
        treasure4.draw(main_win)
        
        

        
            
        
        
        player.move()    
        player.jump()
        if player.is_jump == False:
            player.rect.y += 5

        if player.rect.colliderect(floor1.rect) :
            player.rect.bottom = floor1.rect.top
        enemy.draw(main_win)
        enemy2.draw(main_win)
        player.draw(main_win)
        floor1.draw(main_win)
        islan.draw(main_win)
        island5.draw(main_win)
        island6.draw(main_win)
        islan2.draw(main_win)
        islan3.draw(main_win)
        if player.rect.colliderect(islan.rect):
            player.rect.bottom = islan.rect.top
        if player.rect.colliderect(island5.rect):
            player.rect.bottom = island5.rect.top
        if player.rect.colliderect(island6.rect):
            player.rect.bottom = island6.rect.top
        if player.rect.colliderect(islan3.rect):
            player.rect.bottom = islan3.rect.top
        if player.rect.colliderect(islan2.rect):
            player.rect.bottom = islan2.rect.top


        if player.rect.colliderect(enemy.rect):
            main_win.blit(text2,(0,220))
            mixer.music.play()
            display.update() 
            sleep(2)
            player.rect.x = 70
            player.rect.y = 50
        if player.rect.colliderect(enemy2.rect):
            main_win.blit(text2,(0,220))
            mixer.music.play()
            display.update() 
            sleep(2)
            player.rect.x = 70
            player.rect.y = 50

        if player.rect.colliderect(treasure1.rect):
            score = score + 1
            treasure1.rect.x = 2000
        if player.rect.colliderect(treasure2.rect):
            score = score + 1
            treasure2.rect.x = 2000
        if player.rect.colliderect(treasure3.rect):
            score = score + 1
            treasure3.rect.x = 2000
        if player.rect.colliderect(treasure4.rect):
            score = score + 1
            treasure4.rect.x = 2000
        
        if score == 4:
            main_win.blit(text4,(500,220))
            display.update() 
            


            
            
            islan.rect.x = 100
            islan.rect.y = 400 
            island5.rect.x = 180
            island5.rect.y = 280
            treasure1.rect.y=200
            treasure1.rect.x = 200
            island6.rect.y = 170
            island6.rect.x = 100
            treasure2.rect.y = 400
            treasure2.rect.x = 10
            treasure3.rect.y = 50
            treasure3.rect.x = 880
            islan3.rect.y = 300
        if score == 7:
            main_win.blit(text3,(500,220))
            display.update() 
            sleep(2) 
            
              

            

        



    else:
        main_win.blit(bg2,(-100,0))
        if start_btn.draw(main_win):
            run = True
        if exit_btn.draw(main_win):
            game = False
               

    display.update()
    clock.tick(120)







    