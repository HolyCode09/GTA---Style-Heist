import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Screen Example")

health = 10
gColor = 150
rColor = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and health < 10:
                health += 1
                if health <= 5:
                    gColor += 30
                if health > 5:
                    rColor -= 30
            elif event.key == pygame.K_DOWN and health > 0:
                health -= 1
                if health > 4:
                    rColor += 30
                if health <= 4:
                    gColor -= 30
            print(rColor, gColor, health, (health * 25) - 10)
                





    screen.fill((30, 30, 30))  # Fill the screen with a dark gray color

    pygame.draw.rect(screen, (0, 0, 0), (55, 55, 260 - 10, 40), 0, 100)
    pygame.draw.rect(screen, (rColor, gColor, 0), (55, 55, (health * 25) -10, 40), 0, 0)
    pygame.draw.rect(screen, (255, 255, 255), (45, 45, 260, 60), 10, 100)

    pygame.display.flip()

pygame.quit()
sys.exit()