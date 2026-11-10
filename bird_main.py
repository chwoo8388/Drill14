from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    close_canvas,
    clear_canvas,
    get_events,
    open_canvas,
    update_canvas,
)

import bird_game_framework
from bird import Bird


class BirdGame:
    def __init__(self):
        self.bird = None

    def init(self):
        self.bird = Bird()

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                bird_game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                bird_game_framework.quit()

    def update(self):
        self.bird.update()

    def render(self):
        clear_canvas()
        self.bird.draw()
        update_canvas()

    def finish(self):
        self.bird = None


if __name__ == '__main__':
    open_canvas(1600, 600)
    try:
        bird_game_framework.run(BirdGame())
    finally:
        close_canvas()
