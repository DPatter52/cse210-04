import os
import random

from game.casting.actor import Actor
from game.casting.object import Object
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 20
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Gets Gems" 
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(580)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("\_/")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the objects
    
    for n in range(DEFAULT_OBJECTS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gems = Object()
        gems.set_text("*")
        gems.set_font_size(FONT_SIZE)
        gems.set_color(color)
        gems.set_position(position)
        cast.add_actor("gems", gems)

        rocks = Object()
        rocks.set_text("O")
        rocks.set_font_size(FONT_SIZE)
        rocks.set_color(color)
        rocks.set_position(position)
        cast.add_actor("rocks", rocks)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()