from pyglet import shapes

from random import randint

from configuration import WIDTH, HEIGHT, SQUARE_SIZE


class Food(shapes.Rectangle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def random(self):
        max_x = int(WIDTH / SQUARE_SIZE)
        x = randint(0, max_x - 1) * SQUARE_SIZE
        max_y = int(HEIGHT / SQUARE_SIZE)
        y = randint(0, max_y - 1) * SQUARE_SIZE
        print(max_x, max_y)
        self.position = x, y
