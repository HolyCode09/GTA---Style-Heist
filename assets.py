import pygame
from functions import load_img, load_sound
from values import screenWidth, screenHeight, vw, vh

#images
gameIcon = load_img("pics/gameIcon.png")
charactersPic = load_img("pics/characters.png", (screenWidth + 10, screenHeight + 10))
bgPic = load_img("pics/gameEnter.png", (screenWidth, screenHeight))
map1 = load_img("pics/maps/map1.png", (screenWidth + 10, screenHeight))
timeHolder = load_img("pics/screenAssets/timeHolder.png", (20 * vw, 10 * vh))

#sounds
opening_theme = load_sound("sounds/OpeningTheme.mp3")
opening_sound = load_sound("sounds/OpeningRead.mp3")
characters_sound = load_sound("sounds/Characters.mp3")
startSound = load_sound("sounds/startSound.mp3")
video_bg_music = load_sound("sounds/videoMusic.mp3")
missionMusic = load_sound("sounds/missionMusic.mp3")
clockTick = load_sound("sounds/clockTick.mp3")
carStops = load_sound("sounds/carStops.mp3")

