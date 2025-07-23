import pygame
import sys
from pyvidplayer import Video

from functions import font_size, playVid
import values

values.screen = pygame.display.set_mode()
pygame.display.set_caption("GTA - Style Heist")
values.screenWidth, values.screenHeight = values.screen.get_size()

values.vw = values.screenWidth // 100
values.vh = values.screenHeight // 100

from assets import (
    opening_theme,
    gameIcon,
    charactersPic,
    bgPic,
    opening_sound,
    characters_sound,
    startSound,
    video_bg_music,
    missionMusic,
    map1,
    clockTick,
    carStops, 
    timeHolder,
    video_bg_music,
    missionMusic,
    map1,
    clockTick,
    carStops, 
    timeHolder,
    left,
    right,
    up,
    down,
    down_left,
    down_right,
    up_left,
    up_right
    )

from functions import font_size, playVid

pygame.display.set_caption("GTA - Style Heist")
pygame.display.set_icon(gameIcon)

screen = values.screen
screenWidth = values.screenWidth
screenHeight = values.screenHeight
vw = values.vw
vh = values.vh



def StartScreen():

    pygame.time.delay(500)

    opening_theme.set_volume(1)
    opening_theme.play(-1)
    opening_sound.set_volume(0.3)
    opening_sound.play()

    screen.blit(bgPic, (0,0))

    startBtn = pygame.Surface((27*vw,15*vh), pygame.SRCALPHA)
    startBtnRect = startBtn.get_rect(topleft=(38*vw, 44*vh))

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

    start_btn_width, start_btn_height = 12*vw, 8*vh
    start_btn = pygame.Surface((start_btn_width, start_btn_height), pygame.SRCALPHA)

    # Draw text on the button
    
    text = font_size(4*vw).render("Start", True, "white")
    text_rect = text.get_rect(center=(start_btn_width // 2, start_btn_height // 2))
    start_btn_rect = start_btn.get_rect(topright=(screenWidth - 1*vw, 1*vh))

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
    pygame.mouse.set_visible(False)

    pygame.time.delay(1000)
    video_bg_music.set_volume(0)
    video_bg_music.play(-1)
    for i in range(11):
        video_bg_music.set_volume(0.05 * i / 10)
        pygame.time.delay(100)
    pygame.time.delay(1000)
    playVid("video/gameVideo.mp4", screen, screenWidth, screenHeight)
    video_bg_music.stop()
    gameStart()
    return



missionsInOrder = [
    "Break into the underground-bank-hallway",
    "Knock the guard down",
    "Search for the Suit-Vault",
    "Find the key to the vault",
    "Open the vault and take the suit",
    "Escape the bank and get in the car",
    "Lose the police",
    "Feed Mitzi",
    "Go back to the car to get to the restaurant"
    ]

def gameStart():
    missionMusic.set_volume(1)
    missionMusic.play(-1)

    clock = pygame.time.Clock()
    minuteChange = 0
    screen.fill((0, 0, 0))
    pygame.time.delay(1000)

    for alpha in range(0, 256, 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        startText = font_size(10*vw).render("You have until 9PM", True, (alpha, alpha, alpha))
        screen.blit(startText, (screenWidth // 2 - startText.get_width() // 2, screenHeight // 2 - startText.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(10)

    pygame.time.delay(4000)

    for alpha in range(255, -1, -10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        startText = font_size(10*vw).render("You have until 9PM", True, (alpha, alpha, alpha))
        screen.blit(startText, (screenWidth // 2 - startText.get_width() // 2, screenHeight // 2 - startText.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(10)

    pygame.time.delay(1000)

    health = 10
    gColor = 150
    rColor = 0
    ammo = 0
    bulletSpace = 2*vw

    carStops.set_volume(0.8)
    carStops.play()

    Oria = left
    clock_text = font_size(4*vw).render("8:00PM", True, (255, 255, 255))

    for alpha in range(255, -1, -1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        fade_surface = pygame.Surface((screenWidth, screenHeight))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(map1, (-10, 0))
        screen.blit(timeHolder, (screenWidth // 2 - timeHolder.get_width() // 2, -2*vh))
        screen.blit(clock_text, (screenWidth // 2 - clock_text.get_width() // 2, -0.5*vh))
        pygame.draw.rect(screen, (0, 0, 0), (screenWidth // 2 - 30*vw, 2*vh, (10 * 2*vw) - 0.5*vw, 3.5*vh), 0, 100)
        pygame.draw.rect(screen, (rColor, gColor, 0), (screenWidth // 2 - 30*vw, 2*vh, (health * 2*vw) -0.5*vw, 3.5*vh), 0, 100)
        pygame.draw.rect(screen, (255, 255, 255), (screenWidth // 2 - 30.5*vw, 1.5*vh, 10 * 2*vw, 4.5*vh), 7%vw, 100)
        pygame.draw.rect(screen, (0, 0, 0), (screenWidth // 2 + 10*vw, 2*vh, (10 * 2*vw) - 0.5*vw, 3.5*vh), 0, 100)
        for bullets in range(ammo):
            pygame.draw.rect(screen, (193, 151, 87), (screenWidth // 2 + 10.5*vw + bullets*bulletSpace, 2*vh, 1.3*vw, 3.5*vh))
        pygame.draw.rect(screen, (255, 255, 255), (screenWidth // 2 + 10*vw, 1.5*vh, 10 * 2*vw, 4.5*vh), 7%vw, 100)
        screen.blit(Oria, (50 * vw, 50 * vh))
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

    start_ticks = pygame.time.get_ticks()
    OriaX = 50
    OriaY = 50
    Poses = [left, right, up, down, up_left, up_right, down_left, down_right]
    originalW, originalH = Oria.get_size()
    scaleAmount = 1.0

    no_go_barriers = [
        (pygame.Surface((40 * vw, screenHeight * 1.6), pygame.SRCALPHA), (screenWidth // 2 - 50*vw, -30 * vh), 32),
        (pygame.Surface((40 * vw, screenHeight * 2), pygame.SRCALPHA), (screenWidth // 2 + 45 * vw, -40 * vh), 40),
        (pygame.Surface((screenWidth * 1.6, 35 * vh), pygame.SRCALPHA), (-0.5 * vw, screenHeight // 2 - 80 * vh), 0),
    ]

    while True:
        screen.blit(map1, (-10, 0))
        current_ticks = pygame.time.get_ticks()
        elapsed_time = current_ticks - start_ticks
        in_game_minutes = elapsed_time // 20000
        in_game_hour = 8 + (in_game_minutes // 60)
        in_game_minutes %= 60

        clock_text = font_size(4*vw).render(f"{in_game_hour}:{in_game_minutes:02}PM", True, (255, 255, 255))
        screen.blit(timeHolder, (screenWidth // 2 - timeHolder.get_width() // 2, -2*vh))
        screen.blit(clock_text, (screenWidth // 2 - clock_text.get_width() // 2, -0.5*vh))
        if minuteChange != in_game_minutes:
            clockTick.play()
            minuteChange = in_game_minutes

        #comments# Clear barrier data list before each frame
        barrier_data = []

        for surface, pos, angle in no_go_barriers:
            surface.fill((0, 0, 0, 255))  # Fully opaque for mask
            rotated_surface = pygame.transform.rotate(surface, angle)
            original_rect = surface.get_rect(topleft=pos)
            rotated_rect = rotated_surface.get_rect(center=original_rect.center)

            #comments# Create mask for pixel-perfect collision
            mask = pygame.mask.from_surface(rotated_surface)

            #comments# Create almost invisible surface for drawing
            draw_surface = rotated_surface.copy()
            draw_surface.set_alpha(1)  # Almost invisible

            screen.blit(draw_surface, rotated_rect.topleft)

            barrier_data.append((mask, rotated_rect))

        # Draw HUD elements (health, ammo, etc.)
        pygame.draw.rect(screen, (0, 0, 0), (screenWidth // 2 - 30*vw, 2*vh, (10 * 2*vw) - 0.5*vw, 3.5*vh), 0, 100)
        pygame.draw.rect(screen, (rColor, gColor, 0), (screenWidth // 2 - 30*vw, 2*vh, (health * 2*vw) -0.5*vw, 3.5*vh), 0, 100)
        pygame.draw.rect(screen, (255, 255, 255), (screenWidth // 2 - 30.5*vw, 1.5*vh, 10 * 2*vw, 4.5*vh), 7%vw, 100)
        pygame.draw.rect(screen, (0, 0, 0), (screenWidth // 2 + 10*vw, 2*vh, (10 * 2*vw) - 0.5*vw, 3.5*vh), 0, 100)
        for bullets in range(ammo):
            pygame.draw.rect(screen, (193, 151, 87), (screenWidth // 2 + 10.5*vw + bullets*bulletSpace, 2*vh, 1.3*vw, 3.5*vh))
        pygame.draw.rect(screen, (255, 255, 255), (screenWidth // 2 + 10*vw, 1.5*vh, 10 * 2*vw, 4.5*vh), 7%vw, 100)

        #comments# Scale poses before using
        scaleW = int(originalW * scaleAmount)
        scaleH = int(originalH * scaleAmount)
        Poses = [pygame.transform.scale(p, (scaleW, scaleH)) for p in Poses]

        #comments# Make sure Oria is updated to scaled pose if needed
        # This assumes Oria was always from Poses
        # If Oria is not in Poses for some reason, fallback to first pose
        # if Oria in Poses:
        #     Oria = Poses[Poses.index(Oria)]
        # else:
        #     Oria = Poses[0]

        player_rect = Oria.get_rect(topleft=(OriaX * vw, OriaY * vh))

        #comments# Create player mask from scaled Oria
        player_mask = pygame.mask.from_surface(Oria)

        screen.blit(Oria, (OriaX * vw, OriaY * vh))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        movement_speed = 0.3 * 1.5  # 20% faster

        movement_keys = [
            (keys[pygame.K_s] and keys[pygame.K_d], Poses[7], (movement_speed, movement_speed), +0.002, [0, 1], True),
            (keys[pygame.K_s] and keys[pygame.K_a], Poses[6], (-movement_speed, movement_speed), +0.002, [0], True),
            (keys[pygame.K_w] and keys[pygame.K_a], Poses[4], (-movement_speed, -movement_speed), -0.002, [0, 2], False),
            (keys[pygame.K_w] and keys[pygame.K_d], Poses[5], (movement_speed, -movement_speed), -0.002, [1, 2], False),
            (keys[pygame.K_a], Poses[0], (-movement_speed, 0), 0, [0], False),
            (keys[pygame.K_d], Poses[1], (movement_speed, 0), 0, [1], False),
            (keys[pygame.K_w], Poses[2], (0, -movement_speed), -0.002, [1, 2], False),
            (keys[pygame.K_s], Poses[3], (0, movement_speed), +0.002, [0], True),
        ]

        for condition, pose, (dx, dy), scale_change, barriers_to_check, check_bottom in movement_keys:
            if condition:
                Oria = pose
                proposed_rect = player_rect.move(dx * vw, dy * vh)

                #comments# Pixel-perfect mask collision check
                blocked = False
                for i in barriers_to_check:
                    mask, barrier_rect = barrier_data[i]
                    offset = (int(proposed_rect.x - barrier_rect.x), int(proposed_rect.y - barrier_rect.y))
                    if mask.overlap(player_mask, offset):
                        blocked = True
                        break

                if not blocked and (not check_bottom or proposed_rect.bottom < screenHeight):
                    OriaX += dx
                    OriaY += dy
                    scaleAmount += scale_change
                break

        pygame.display.flip()
        clock.tick(60)



