import os
import sys
import pygame


class Background:
    image = None
    
    def __init__(self, image):
        
        self.image = image
        
    def draw(self, screen):
        
        print 't'
        
    def update(self, dt):
        
        print 't'
        

class Game:
    screen = None
    screen_size = None
    run = None
    background = None
    
    def __init__(self):
        print 't'