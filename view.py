import pygame
from abc import ABC, abstractmethod

class AbstractView(ABC):
    def __init__(self, width, height):
        pass

    @abstractmethod
    def run(self):
        pass

class Board(AbstractView):
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Game of life')

    def draw(self, *args):
        background = (255, 255, 255)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)
        pygame.display.update()

    def run(self):
        # Przykładowa implementacja metody run, jeżeli jest wymagana
        pass
