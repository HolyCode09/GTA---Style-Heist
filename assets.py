import pygame
from functions import load_img, load_sound

#images
gameIcon = load_img("pics/gameIcon.png")
charactersPic = load_img("pics/characters.png", (1610,910))
bgPic = load_img("pics/gameEnter.png", (1600, 900))
map1 = load_img("pics/maps/map1.png", (1610, 900))
timeHolder = load_img("pics/screenAssets/timeHolder.png", (300, 100))

#sounds
opening_theme = load_sound("sounds/OpeningTheme.mp3")
opening_sound = load_sound("sounds/OpeningRead.mp3")
characters_sound = load_sound("sounds/Characters.mp3")
startSound = load_sound("sounds/startSound.mp3")
video_bg_music = load_sound("sounds/videoMusic.mp3")
missionMusic = load_sound("sounds/missionMusic.mp3")
clockTick = load_sound("sounds/clockTick.mp3")
carStops = load_sound("sounds/carStops.mp3")