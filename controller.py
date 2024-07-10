import pygame
from abc import ABC, abstractmethod
from model import Population
from view import Board

class AbstractController(ABC):
    def __init__(self,width,height, cell_size):
        pass

    @abstractmethod
    def run(self):
        pass

class GameOfLife(AbstractController):
    def __init__(self, width, height, cell_size=10):
        super().__init__(width, height, cell_size)
        pygame.init()
        self.board = Board(width * cell_size, height * cell_size)
        self.fps_clock = pygame.time.Clock()
        self.population = Population(width, height, cell_size)
        self.started = False

    def run(self):
        while not self._handle_events():
            self.board.draw(self.population)
            if self.started:
                self.population.cycle_generation()
            self.fps_clock.tick(5)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                self.population.handle_mouse()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.started = True
                elif event.key == pygame.K_SPACE:
                    self.started = not self.started
        return False
