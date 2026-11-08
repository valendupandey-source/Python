import pygame
import random
class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def clicked(self, pos):
        return self.rect.collidepoint(pos)
class RpsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960,640))   
        pygame.display.set_ccaption("RPS Smasher") 
        self.bg = pygame.image.load("Space.jpeg")    
        self.buttons = [
            pygame.image.load("Rock.png"),
            pygame.image.load("Paper.png"),
            pygame.image.load("Scissor.png")
        ]
        self.images = [
            pygame.image.load(""),
            pygame.image.load(""),
            pygame.image.load("")
        ]

        
