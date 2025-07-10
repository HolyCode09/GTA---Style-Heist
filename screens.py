import pygame
import sys
from pyvidplayer import Video
from assets import (
    opening_theme,
    gameIcon,
    charactersPic,
    bgPic,
    opening_sound,
    characters_sound,
    startSound,
<<<<<<< HEAD
    video_bg_music,
    missionMusic,
    map1,
    clockTick,
    carStops, 
    timeHolder
=======
    video_bg_music
>>>>>>> 3be00e6599a540745c4798d9648949c91ff347b2
)
from functions import font_size, playVid

screenWidth, screenHeight = 1600,900
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("GTA - Style Heist")
pygame.display.set_icon(gameIcon)

def StartScreen():

    pygame.time.delay(500)

    opening_theme.set_volume(1)
    opening_theme.play(-1)
    opening_sound.set_volume(0.3)
    opening_sound.play()

    screen.blit(bgPic, (0,0))

    startBtn = pygame.Surface((400,200), pygame.SRCALPHA)

    startBtnRect = startBtn.get_rect(topleft=(600, 320))

    screen.blit(startBtn, startBtnRect.topleft)



    fade_out = False

    while True:
        mouse_pos = pygame.mouse.get_pos()
        if startBtnRect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startBtnRect.collidepoint(mouse_pos):
                    fade_out = True

        if fade_out:
            for alpha in range(0, 256, 10):
                fade_surface = pygame.Surface((screenWidth, screenHeight))
                fade_surface.fill((0, 0, 0))
                fade_surface.set_alpha(alpha)
                screen.blit(fade_surface, (0, 0))
                pygame.display.flip()
                pygame.time.delay(20)
            CharactersScreen()
            return
            



        pygame.display.flip()

        pygame.time.Clock().tick(60)


def CharactersScreen():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    for alpha in range(255, -1, -10):
        fade_surface = pygame.Surface((screenWidth, screenHeight))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(charactersPic, (-5, -5))
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)
    screen.blit(charactersPic, (-5,-5))
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    characters_sound.set_volume(0.3)
    characters_sound.play()

    pygame.time.delay(1000)

    start_btn_width, start_btn_height = 200, 80
    start_btn = pygame.Surface((start_btn_width, start_btn_height), pygame.SRCALPHA)

    # Draw text on the button
    
    text = font_size(60).render("Start", True, "white")
    text_rect = text.get_rect(center=(start_btn_width // 2, start_btn_height // 2))
    start_btn_rect = start_btn.get_rect(topright=(screenWidth - 20, 20))

    start_btn.blit(text, text_rect)
    for alpha in range(0, 151, 10):
        screen.blit(charactersPic, (-5, -5))
        start_btn.fill((234, 173, 58, alpha))
        screen.blit(start_btn, start_btn_rect.topleft)
        pygame.display.flip()
        pygame.time.delay(20)

    start_btn.blit(text, text_rect)
    screen.blit(start_btn, start_btn_rect.topleft)

    onStartBtn = False
    while True:
        mouse_pos = pygame.mouse.get_pos()
        if start_btn_rect.collidepoint(mouse_pos):
            onStartBtn = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            onStartBtn = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onStartBtn:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    startSound.set_volume(0.3)
                    startSound.play()
                    for alpha in range(0, 256, 5):
                        fade_surface = pygame.Surface((screenWidth, screenHeight))
                        fade_surface.fill((0,0,0))
                        fade_surface.set_alpha(alpha)
                        screen.blit(fade_surface, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(50)
                    opening_theme.stop()
                    preGameVideo()
                    return
            pygame.display.flip()


def preGameVideo():
    global video_bg_music
<<<<<<< HEAD
    pygame.mouse.set_visible(False)
=======
>>>>>>> 3be00e6599a540745c4798d9648949c91ff347b2
    pygame.time.delay(1000)
    video_bg_music.set_volume(0)
    video_bg_music.play(-1)
    for i in range(11):
        video_bg_music.set_volume(0.05 * i / 10)
        pygame.time.delay(100)
    pygame.time.delay(1000)
    playVid("video/gameVideo.mp4", screen, screenWidth, screenHeight)
    video_bg_music.stop()
<<<<<<< HEAD
    gameStart()
    return


def gameStart():
    missionMusic.set_volume(1)
    missionMusic.play(-1)

    clock = pygame.time.Clock()

    minuteChange = 0

    screen.fill((0, 0, 0))

    # pygame.time.delay(1000)

    # for alpha in range(0, 256, 1):
    #     startText = font_size(200).render("You have until 9PM", True, (alpha, alpha, alpha))
    #     screen.blit(startText, (screenWidth // 2 - startText.get_width() // 2, screenHeight // 2 - startText.get_height() // 2))
    #     pygame.display.flip()
    #     pygame.time.delay(10)

    # pygame.time.delay(4000)

    # for alpha in range(0, 256, 1):
    #     fade_surface = pygame.Surface((screenWidth, screenHeight))
    #     fade_surface.fill((0, 0, 0))
    #     fade_surface.set_alpha(alpha)
    #     screen.blit(fade_surface, (0, 0))
    #     pygame.display.flip()
    #     pygame.time.delay(20)

    # carStops.set_volume(0.8)
    # carStops.play()

    clock_text = font_size(70).render("8:00PM", True, (255, 255, 255))
    for alpha in range(255, -1, -1):
        fade_surface = pygame.Surface((screenWidth, screenHeight))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(map1, (-10, 0))
        screen.blit(timeHolder, (screenWidth // 2 - timeHolder.get_width() // 2, -20))
        screen.blit(clock_text, (screenWidth // 2 - clock_text.get_width() // 2, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

    start_ticks = pygame.time.get_ticks()
    while True:
        screen.blit(map1, (-10, 0))

        current_ticks = pygame.time.get_ticks()
        elapsed_time = current_ticks - start_ticks
        in_game_minutes = elapsed_time // 20000
        in_game_hour = 8 + (in_game_minutes // 60)
        in_game_minutes = in_game_minutes % 60

        clock_text = font_size(70).render(f"{in_game_hour}:{in_game_minutes:02}PM", True, (255, 255, 255))
        screen.blit(timeHolder, (screenWidth // 2 - timeHolder.get_width() // 2, -20))
        screen.blit(clock_text, (screenWidth // 2 - clock_text.get_width() // 2, 0))
        if minuteChange != in_game_minutes:
            clockTick.play()
            minuteChange = in_game_minutes

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(60)
=======
    return
>>>>>>> 3be00e6599a540745c4798d9648949c91ff347b2
