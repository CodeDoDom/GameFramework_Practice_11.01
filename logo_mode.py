from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
import game_framework


def init():
    global image
    global logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()
    pass


def finish():
    global load_image


def handle_events():
    events = get_events()
    pass


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        game_framework.quit()


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()