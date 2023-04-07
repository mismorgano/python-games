import pyglet
from pyglet import shapes

from configuration import WIDTH, HEIGHT, SQUARE_SIZE
from food import Food
from snake import Snake

window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption='snake')
batch = pyglet.graphics.Batch()

FPS = 30
colors = {'green': (135, 236, 298, 255), 'red': (240, 100, 90, 255)}
food = Food(20, 0, 20, 20, color=colors['green'], batch=batch)
snake = Snake(0, 0, SQUARE_SIZE, colors['red'], batch=batch)

board = []

window.push_handlers(snake)
window.push_handlers(snake.key_handler)


def configuration():
    pass


def init() -> None:
    configuration()
    create_board()
    food.random()


def create_board():
    for i in range(0, WIDTH, SQUARE_SIZE):
        line = shapes.Line(x=i, y=0, x2=i, width=1, y2=window.height, batch=batch)
        board.append(line)
    for j in range(0, HEIGHT, SQUARE_SIZE):
        line = shapes.Line(x=0, y=j, x2=window.width, y2=j, batch=batch)
        board.append(line)


def update(dt):
    snake.update(dt, food)


@window.event
def on_draw():
    window.clear()
    batch.draw()


init()
pyglet.clock.schedule_interval(update, 1 / FPS)

if __name__ == '__main__':
    pyglet.app.run()
    display = pyglet.canvas.get_display()
    screen = display.get_default_screen()
    print(screen.width, screen.height)
    print(window.get_pixel_ratio())
    print(window.get_size())
    print(window.get_framebuffer_size())
