#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pygame



class Background:
    '''This class representing the backgorund game '''
    image = None
    
    def __init__(self): 
        screen = pygame.display.get_surface()
        back   = pygame.Surface( screen.get_size() ).convert()
        back.fill( ( 0, 0, 0 ) )
        self.image = back
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        
    def update(self, dt):
        pass
        

class Game:
    screen = None
    screen_size = None
    run = True
    background = None
    
    def __init__(self, size, fullscreen):
        actors = {}
        pygame.init()
        flags = DOUBLEBUF
        
        if fullscreen:
            flags |= FULLSCREEN
            
        self.screen = pygame.display.set_mode( size, flags )
        self.screen_size = self.screen.get_size()

        pygame.mouse.set_visible( 0 )
        pygame.display.set_caption( 'Título da Janela' )
        
        
    def actor_update(self, dt):
        self.background.update( dt )
        
        
    def handle_event(self):
        for event in pygame.event.get():
            t = event.type
            if t in ( KEYDOWN, KEYUP ):
                k = event.key
        
            if t == QUIT:
                self.run = False

            elif t == KEYDOWN:
                if   k == K_ESCAPE:
                    self.run = False
        
        
    def actor_draw(self):
        self.background.draw( self.screen )
        
        
    def loop(self):
        # Criamos o fundo
        self.background = Background()

        # Inicializamos o relogio e o dt que vai limitar o valor de
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 16


        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick( 1000 / dt )

            # Handle Input Events
            self.handle_events()

            # Atualiza Elementos
            self.actors_update( dt )

            # Desenhe para o back buffer
            self.actors_draw()
            
            # ao fim do desenho temos que trocar o front buffer e o back buffer
            pygame.display.flip()

            print "FPS: %0.2f" % clock.get_fps()
    