
from time import sleep, time

from internal import Canvas as _Canvas, clear_screen


Canvas = _Canvas


def run(func, framerate=24):
    FRAME_TIME = 1/framerate

    while True:
        t1 = time()

        func()

        t2 = time()
        elapsed_time = t2-t1

        if elapsed_time < FRAME_TIME:
            sleep(FRAME_TIME-elapsed_time)


if __name__ == "__main__":
    # run()
    clear_screen()
    canvas = Canvas(12, 12)

    time_count = 0

    def draw():
        global time_count
        canvas.background((time_count, time_count, time_count))

        canvas.show()
        time_count += 1
    run(draw, 2)
