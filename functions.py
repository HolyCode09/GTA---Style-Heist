import pygame
from pyvidplayer import Video

pygame.mixer.init()

def load_sound(path):
    return pygame.mixer.Sound(path)

def font_size(size):
    return pygame.font.Font("gameFont.ttf", size)

def load_img(path, size=None):
    img = pygame.image.load(path)
    if size:
        img = pygame.transform.scale(img, size)
    return img

def playVid(path, screen, screenWidth, screenHeight):
    vid = Video(path)
    vid.set_size((screenWidth, screenHeight))
    
    clock = pygame.time.Clock()
    
    while True:
        done = not vid.draw(screen, (0, 0))
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        if done:
            break

    vid.close()

                
                