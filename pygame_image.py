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
    koka_img_rct = koka_img.get_rect() #8-1
    koka_img_rct.center = 300,200 #8-2
    tmr = 0 
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() 
        if key_lst[pg.K_UP]:
            koka_img_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:  
            koka_img_rct.move_ip((0,+1))
        if key_lst[pg.K_RIGHT]:
            koka_img_rct.move_ip((1,0))
        if key_lst[pg.K_LEFT]:
            koka_img_rct.move_ip((-1,0))  
        x = -(tmr % 3200) #6 #7-1 #7-2
        screen.blit(bg_img, [x, 0]) #3 #6
        screen.blit(bg1_img,[x+1600,0]) #7-1
        screen.blit(bg_img, [x+3200, 0]) #7-2
        screen.blit(bg_img, [x+4800, 0]) #7-2
        screen.blit(koka_img, koka_img_rct) #4 #8-5

        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()