import pygame
from abc import ABC, abstractmethod

DEAD = 0
ALIVE = 1

class AbstractModel(ABC):
    def __init__(self, width, height, cell_size):
        pass

    @abstractmethod
    def cycle_generation(self):
        pass

    @abstractmethod
    def handle_mouse(self):
        pass

    @abstractmethod
    def draw_on(self, surface):
        pass

class Population(AbstractModel):
    def __init__(self, width, height, cell_size=10):
        super().__init__(width, height, cell_size)
        self.box_size = cell_size
        self.height = height
        self.width = width
        self.generation = self.reset_generation()

    def reset_generation(self):
        return [[DEAD for _ in range(self.height)] for _ in range(self.width)]

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if not any(buttons):
            return

        alive = True if buttons[0] else False

        x, y = pygame.mouse.get_pos()
        x //= self.box_size
        y //= self.box_size

        self.generation[int(x)][int(y)] = ALIVE if alive else DEAD

    def draw_on(self, surface):
        for x, y in self.alive_cells():
            size = (self.box_size, self.box_size)
            position = (x * self.box_size, y * self.box_size)
            color = (150, 255, 22)
            pygame.draw.rect(surface, color, pygame.Rect(position, size))

    def alive_cells(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.generation[x][y] == ALIVE:
                    yield x, y

    def neighbours(self, x, y):
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue
                if nx >= self.width:
                    nx = 0
                elif nx < 0:
                    nx = self.width - 1
                if ny >= self.height:
                    ny = 0
                elif ny < 0:
                    ny = self.height - 1

                yield self.generation[nx][ny]

    def cycle_generation(self):
        next_gen = self.reset_generation()
        for x in range(self.width):
            for y in range(self.height):
                count = sum(self.neighbours(x, y))
                if count == 3:
                    next_gen[x][y] = ALIVE
                elif count == 2:
                    next_gen[x][y] = self.generation[x][y]
                else:
                    next_gen[x][y] = DEAD

        self.generation = next_gen
