import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #1
    koka_img = pg.image.load("fig/3.png") #2
    koka_img = pg.transform.flip(koka_img,True,False) #2
    bg1_img = pg.transform.flip(bg_img,True,False)#7-1
    tmr = 0 
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr % 3200) #6 #7-1 #7-2
        screen.blit(bg_img, [x, 0]) #3 #6
        screen.blit(bg1_img,[x+1600,0]) #7-1
        screen.blit(bg_img, [x+3200, 0]) #7-2
        screen.blit(bg_img, [x+4800, 0]) #7-2
        screen.blit(koka_img, [300, 200]) #4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()