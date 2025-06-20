import pygame
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