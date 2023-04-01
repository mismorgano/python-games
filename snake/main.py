import pyglet
from pyglet import shapes
from random import randint
from collections import deque
from pyglet.window import key
from types import SimpleNamespace

SQUARE_SIZE = 10, 10
BOARD_SIZE = 20, 10
GRID_WIDTH = 1

WIDTH = SQUARE_SIZE[0]*BOARD_SIZE[0]
HEIGHT = SQUARE_SIZE[1]*BOARD_SIZE[1]

window = pyglet.window.Window(width=WIDTH, height=HEIGHT,caption='Snake')
batch = pyglet.graphics.Batch()


colors = {'green': (135, 236, 298, 255), 'red': (240, 100, 90, 255)}
food = shapes.Rectangle(x=0, y=00, width=SQUARE_SIZE[0], height=SQUARE_SIZE[1], color=colors['green'], batch=batch)
snake = []

delay = 0.3

direction = None
time = 0

board = []
perro = SimpleNamespace(name='esta' )
# perro.name = "esta"

perro.bark = lambda: print(f'Hola a todos soy {perro.name}')
perro.bark()


def random_food():
    x = randint(0, BOARD_SIZE[0]-1)*SQUARE_SIZE[0]
    y = randint(0, BOARD_SIZE[1]-1)*SQUARE_SIZE[1]

    food.position = x, y


def configuration():
    pass

def init() -> None:
    configuration()
    create_board()
    x = randint(0, BOARD_SIZE[0]-1)*SQUARE_SIZE[0]
    y = randint(0, BOARD_SIZE[1]-1)*SQUARE_SIZE[1]
    snake.append(shapes.Rectangle(x=x, y=y, width=SQUARE_SIZE[0], height=SQUARE_SIZE[1], color=colors['red'], batch=batch))


def create_board():

    for i in range(BOARD_SIZE[0]):
        line = shapes.Line(x=i*SQUARE_SIZE[0] + 0.5, y=0, x2=i*SQUARE_SIZE[0]+0.5, y2=window.height, batch=batch)
        board.append(line)
    for j in range(BOARD_SIZE[1]):
        line = shapes.Line(x=0, y=j*SQUARE_SIZE[1]+0.5, x2=window.width, y2=j*SQUARE_SIZE[1]+0.5, batch=batch)
        board.append(line)


x = "Hola a todo el mundo"
print(x)

b = [1, 2, 3, 4, 5]

def update(dt):
    vx = 0
    vy = 0
    global time
    # food.x += dt*vx
    # food.y += dt*vy

    if time > delay:
        match direction:
            case 1:
                snake[0].x += SQUARE_SIZE[0]
            case 2:
                snake[0].y += SQUARE_SIZE[1]
            case 3:
                snake[0].y -= SQUARE_SIZE[1]
            case 4:
                snake[0].x -= SQUARE_SIZE[0]
        time = 0

    time += dt

@window.event
def on_key_press(symbol, modifiers):
    # global direction
    # direction = randint(1, 4)
    # random_food()

    global direction
    match symbol:
        case key.UP:
            direction = 2
        case key.RIGHT:
            direction = 1
        case key.LEFT:
            direction = 4
        case key.DOWN:
            direction = 3



@window.event
def on_draw():
    window.clear()
    batch.draw()



init()
pyglet.clock.schedule_interval(update, 1/120)

if __name__ == '__main__':
    pyglet.app.run()

# class HelloWorldWindow(pyglet.window.Window):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.label = pyglet.text.Label("Hello World", font_name='JetBrainsMono NF')


#     def on_draw(self):
#         self.clear()
#         self.label.draw()

# if __name__ == '__main__':
#     window = HelloWorldWindow()
#     pyglet.app.run()