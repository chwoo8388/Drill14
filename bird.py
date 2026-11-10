import bird_game_framework as game_framework
from pico2d import get_canvas_width, load_image


class Bird:
    image = None
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAME_COUNT = 14
    FRAME_RATE = 12
    SPEED_KMPH = 10
    SCREEN_WIDTH_KM = 100
    DRAW_WIDTH = 150
    DRAW_HEIGHT = 138

    def __init__(self, x=None, y=300, direction=1, frame=0):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.image = Bird.image
        self.x = self.DRAW_WIDTH / 2 if x is None else x
        self.y = y
        self.direction = direction
        self.frame = frame % self.FRAME_COUNT
        self.frame_elapsed = 0.0

    def update(self):
        frame_time = game_framework.frame_time
        canvas_width = get_canvas_width()
        pixels_per_second = (
            canvas_width * self.SPEED_KMPH / self.SCREEN_WIDTH_KM / 3600
        )
        self.x += self.direction * pixels_per_second * frame_time

        edge = self.DRAW_WIDTH / 2
        if self.x >= canvas_width - edge:
            self.x = canvas_width - edge
            self.direction = -1
        elif self.x <= edge:
            self.x = edge
            self.direction = 1

        self.frame_elapsed += frame_time
        if self.frame_elapsed >= 1 / self.FRAME_RATE:
            frames_elapsed = int(self.frame_elapsed * self.FRAME_RATE)
            self.frame = (self.frame + frames_elapsed) % self.FRAME_COUNT
            self.frame_elapsed -= frames_elapsed / self.FRAME_RATE

    def draw(self):
        row, column = divmod(self.frame, 5)
        source_x = column * self.FRAME_WIDTH
        source_y = (2 - row) * self.FRAME_HEIGHT
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            source_x, source_y, self.FRAME_WIDTH, self.FRAME_HEIGHT,
            0, flip, self.x, self.y, self.DRAW_WIDTH, self.DRAW_HEIGHT
        )
