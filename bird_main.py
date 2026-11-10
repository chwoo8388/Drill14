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
        self.birds = []

    def init(self):
        self.birds = [
            Bird(x=x, y=y, direction=1 if column % 2 == 0 else -1,
                 frame=(column + row * 5) % Bird.FRAME_COUNT)
            for row, y in enumerate((220, 420))
            for column, x in enumerate((150, 475, 800, 1125, 1450))
        ]

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                bird_game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                bird_game_framework.quit()

    def update(self):
        for bird in self.birds:
            bird.update()

    def render(self):
        clear_canvas()
        for bird in self.birds:
            bird.draw()
        update_canvas()

    def finish(self):
        self.birds.clear()


if __name__ == '__main__':
    open_canvas(1600, 600)
    try:
        bird_game_framework.run(BirdGame())
    finally:
        close_canvas()
