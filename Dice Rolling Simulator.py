import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 380))
pygame.display.set_caption("Dice Game")
font = pygame.font.SysFont(None, 36)

# Put your dice image filenames here
dice_images = [
    pygame.image.load("Dice_side_1.png"),
    pygame.image.load("Dice_side_2.png"),
    pygame.image.load("Dice_side_3.png"),
    pygame.image.load("Dice_side_4.png"),
    pygame.image.load("Dice_side_5.png"),
    pygame.image.load("Dice_side_6.png")
]
dice_images = [pygame.transform.scale(img, (120, 120)) for img in dice_images]

roll_btn = pygame.Rect(60, 280, 110, 50)
stop_btn = pygame.Rect(230, 280, 110, 50)

current_dice = 0
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if roll_btn.collidepoint(event.pos):
                current_dice = random.randint(0, 5)
                score += current_dice + 1
            elif stop_btn.collidepoint(event.pos):
                running = False

    screen.fill((30, 30, 40))
    screen.blit(dice_images[current_dice], (140, 50))
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (145, 200))

    pygame.draw.rect(screen, (0, 180, 0), roll_btn)
    pygame.draw.rect(screen, (200, 0, 0), stop_btn)
    screen.blit(font.render("ROLL", True, (255, 255, 255)), (80, 293))
    screen.blit(font.render("STOP", True, (255, 255, 255)), (250, 293))

    pygame.display.flip()

print("Final Score:", score)
pygame.quit()
