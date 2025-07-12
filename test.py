import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Screen Example")

ammo = 10


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and ammo < 10:
                ammo+=1
            elif event.key == pygame.K_DOWN and ammo > 0:
                ammo-=1
                

    screen.fill((30, 30, 30))  # Fill the screen with a dark gray color

    bulletSpace = 25
    pygame.draw.rect(screen, (0, 0, 0), (55, 55, 260 - 10, 40), 0, 100)
    for bullets in range(ammo):
        pygame.draw.rect(screen, "brown", (55 + bullets*bulletSpace, 55, 15, 40))
    pygame.draw.rect(screen, (255, 255, 255), (45, 45, 260, 60), 10, 100)

    pygame.display.flip()

pygame.quit()
sys.exit()