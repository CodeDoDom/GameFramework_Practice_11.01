from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode


def init():
    global image
    global logo_start_time

    image = load_image('title.png')
    logo_start_time = get_time()
    pass


def finish():
    global load_image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()