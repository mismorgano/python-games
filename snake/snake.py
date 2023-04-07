from pyglet import shapes, text
from pyglet.window import key
from pyglet.window.key import KeyStateHandler
from configuration import SQUARE_SIZE, WIDTH, HEIGHT


class SnakeBody(shapes.Rectangle):
    pass


class Snake:
    def __init__(self, x, y, size, color, batch):
        self.body = []
        self.color = color
        self.batch = batch
        self.body.append(shapes.Rectangle(x, y, size, size, color=color, batch=batch))
        self.direction = None
        self.velocity = 100
        self.distance = 0
        self.alive = True
        self.game_over = None
        self.key_handler = KeyStateHandler()
        print(self.key_handler.data)

    def update(self, dt, food):
        self.distance += self.velocity * dt
        if self.distance > SQUARE_SIZE and self.alive:
            if self.out_of_bounds():
                self.alive = False
                self.game_over = text.Label('Game Over', font_name='Times New Roman', font_size=26, x=WIDTH / 2,
                                            y=HEIGHT / 2, batch=self.batch)
                return
            self.move()
            if self.has_eaten(food):
                food.random()
                self.growth()

            self.distance = 0

    def has_eaten(self, food):
        head = self.body[0]
        return head.x == food.x and head.y == food.y

    def move(self):

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].position = self.body[i - 1].position

        head = self.body[0]
        match self.direction:
            case key.LEFT:
                head.x -= SQUARE_SIZE
            case key.UP:
                head.y += SQUARE_SIZE
            case key.RIGHT:
                head.x += SQUARE_SIZE
            case key.DOWN:
                head.y -= SQUARE_SIZE

    def growth(self):
        last = self.body[-1]
        x = last.x
        y = last.y
        match opposite_direction(self.direction):
            case key.LEFT:
                x -= SQUARE_SIZE
            case key.RIGHT:
                x += SQUARE_SIZE
            case key.UP:
                y += SQUARE_SIZE
            case key.DOWN:
                y -= SQUARE_SIZE
        snake_body = shapes.Rectangle(x=x, y=y, width=SQUARE_SIZE, height=SQUARE_SIZE, color=self.color,
                                      batch=self.batch)
        self.body.append(snake_body)

    def out_of_bounds(self):
        head = self.body[0]
        return head.x < 0 or head.x > WIDTH or head.y < 0 or head.y > HEIGHT

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case key.LEFT | key.RIGHT | key.UP | key.DOWN:
                if self.direction != opposite_direction(symbol):
                    self.direction = symbol


def opposite_direction(direction):
    # directions = {key.LEFT: key.RIGHT, key.UP:key.DOWN}
    match direction:
        case key.LEFT:
            return key.RIGHT
        case key.UP:
            return key.DOWN
        case key.RIGHT:
            return key.LEFT
        case key.DOWN:
            return key.UP
