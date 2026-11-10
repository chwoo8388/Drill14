import time

from pico2d import delay


running = False
frame_time = 0.0
FRAME_INTERVAL = 1 / 60


def quit():
    global running
    running = False


def run(game):
    global running, frame_time
    running = True
    frame_time = FRAME_INTERVAL
    previous_time = time.perf_counter()
    game.init()

    try:
        while running:
            frame_start = time.perf_counter()
            frame_time = frame_start - previous_time
            previous_time = frame_start

            game.handle_events()
            if not running:
                break

            game.update()
            game.render()

            remaining_time = FRAME_INTERVAL - (time.perf_counter() - frame_start)
            if remaining_time > 0:
                delay(remaining_time)
    finally:
        running = False
        game.finish()
