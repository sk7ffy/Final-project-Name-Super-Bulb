from pygame import*
from button import Button
main_win = display.set_mode((700,500))
display.set_caption('Super Bulb')
clock = time.Clock()
game = True
background
start_btn = Button(250,300,200,80,'start.png')
exit_btn = Button(250,200,200,100,'exit.png')
run = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = not run
        if run:
            main_win.fill((255,0,0))
        else:
            main_win.fill((0,0,0))
        if start_btn.draw(main_win):
            run = True
        if exit_btn.draw(main_win):
            game = False
            

    display.update()
    clock.tick(60)