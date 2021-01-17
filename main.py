import pygame as pg
WINDOW_SIZE = (640, 480)
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()
class Button:
    def __init__(self):
        pass
    def draw(self):
        pass
    def is_click(self):
        pass
    def do(self):
        pass
    def set_text(self):
        pass
    def set_color(self):
        pass
    def set_size(self):
        pass
FPS = 30
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False  
    pg.display.update()
pg.quit()