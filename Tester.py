#https://www.pygame.org/pcr/wavey_text/index.php

# !/usr/bin/env python

"""
example animated entry for the pygame text contest

if you would like to change this for your own entry, modify
the class so it returns the next image of the rendered text
each call to animate(). Note the image size should not change
for this simple framework.
"""
import os, sys, math, pygame, pygame.font, pygame.image
from pygame.locals import *


class textWavey:
    def __init__(self, font, message, fontcolor, amount=10):
        self.base = font.render(message, 0, fontcolor)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = self.base.get_rect().inflate(0, amount).size
        self.offset = 0.0

    def animate(self):
        s = pygame.Surface(self.size)
        height = self.size[1]
        self.offset += 0.5
        for step in self.steps:
            src = Rect(step, 0, 2, height)
            dst = src.move(0, math.cos(self.offset + step * .02) * self.amount)
            s.blit(self.base, dst, src)
        return s


entry_info = 'edibles'

# this code will display our work, if the script is run...
if __name__ == '__main__':
    pygame.init()

    # create our fancy text renderer
    bigfont = pygame.font.Font("fonts/Condition.ttf", 360)
    white = 255, 255, 255
    red = 255, 0, 0
    renderer = textWavey(bigfont, entry_info, white, 10)
    renderer2 = textWavey(bigfont, entry_info, red, 10)
    text = renderer.animate()
    text2 = renderer2.animate()
    # create a window the correct size
    win = pygame.display.set_mode(text.get_size())
    win.blit(text, (0, 0))
    win.blit(text2, (0, 80))
    pygame.display.flip()

    # wait for the finish
    finished = 0
    while not finished:
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type is KEYDOWN and event.key == K_s:  # save it
                name = os.path.splitext(sys.argv[0])[0] + '.bmp'
                print
                'Saving image to:', name
                pygame.image.save(win, name)
            elif event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
                finished = 1

        text = renderer.animate()
        text2 = renderer2.animate()
        win.blit(text, (0, 0))
        win.blit(text2, (0, 80))
        pygame.display.flip()