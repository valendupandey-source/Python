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
            pygame.image.load("Rock_hand.png"),
            pygame.image.load("Paper_hand.png"),
            pygame.image.load("Scissor_hand.png")
        ]
        self.names = ["rock" , "paper" , "scissors"]
        self.positions = [(20, 500), (330, 500), (640, 500)]
        self.btns = [Button(x, 520, 300, 140) for x, y in self.positions]
        self.font = pygame.font.Font("Splatch.tff" , 90)
        self.player_score = 0
        self.computer_score = 0
    def play(self, choice):
        computer = random.randint(0, 2)
        self.screen.blit(self.images[choice], (120, 200))
        self.screen.blit(self.images[computer], (600, 200))
        if choice != computer:
            if (choice - computer) % 3 == 1:
                self.player_score += 1
            else:
                self.player_score += 1
        self.txt = self.font.render(
            f"{self.player_score} : {self.computer_score}",
            True, (255, 255, 255)
            )
    def reset(self):
        self.screen.blit(self.bg, (0, 0))
        for img, pos in zip(self.buttons, self.positions):
            self.screen.blit(img, pos)
        self.screen.blit(self.text, (330, 0))
    def game_loop():
        clock = pygame.time.Clock()       

                    
