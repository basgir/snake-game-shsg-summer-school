import pygame
import random

# We initialize the game
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Bloc attributes
bloc_color = BLACK
bloc_width = 35
bloc_height = bloc_width






class Snake():
    def __init__(self, initial_position, length):
        self.past_moves = []
        self.length = 1

        self.xpos = xpos
        self.ypos = ypos
        self.length = length
        self.current_position = (self.xpos, self.ypos)
        self.initial_pos = (0,0)

    def grow(self):
        self.length += 1
        self.body.append(self.current_position)

    def update_pos(new_xp, new_xy):
        self.xpos = new_xp
        self.ypos = new_yp

    def record_move(self, cell_pos):
        self.past_moves.append(cell_pos)

class Apple():

    def __init__(self):
        self.xpos = 0
        self.ypos = 0

    def random_pos(current_snake_pos):

        while (self.xpos, self.ypos) in current_snake_pos:
            self.xpos = random.random(0,21)
            self.ypos = random.random(0,21)

class Game():
    def __init__(self, cell_size, number_of_cells, line_margin):
        self.number_of_cells = number_of_cells
        self.cell_size = cell_size
        self.line_margin = line_margin

        self.width = self.number_of_cells*(self.cell_size+self.line_margin)
        self.height = self.number_of_cells*(self.cell_size+self.line_margin)
        self.size = (self.height, self.width)
        self.screen = pygame.display.set_mode(self.size)
        self.grid_color = BLACK
        self.background_color = WHITE
        self.screen.fill(pygame.Color('WHITE'))
        self.show_grid()
        self.snake = Snake(initial_position = (1,1), length=1)
        self.game_on = True
        while self.game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        next_xpos = self.get_cell_coordinate(self.snake.cell_number)
                        self.snake.update_pos(self.snake.ypos, self.snake.xpos-) rect_xp =- rect_change_xp+rect_xp
                    if event.key == pygame.K_RIGHT:
                        rect_xp = rect_change_xp+rect_xp
                    if event.key == pygame.K_UP:
                        rect_yp =-rect_change_yp+rect_yp
                    if event.key == pygame.K_DOWN:
                        rect_yp = rect_change_yp+rect_yp

            pygame.display.update()

    def show_grid(self):
        for row in range(self.number_of_cells):
            # Go through each 
            for column in range(self.number_of_cells):

                # Print black cells
                pygame.draw.rect(self.screen,self.grid_color,[(self.line_margin + self.cell_size) * column + self.line_margin,(self.line_margin + self.cell_size) * row + self.line_margin,self.cell_size,self.cell_size])
    def get_cell_coordinate(self, cell_number):

        xpos = cell_number[0]*self.cell_size
        ypos = cell_number[1]*self.cell_size

            return xpos, ypos
    
    def check_if_apple_available(self):
        self.number_of_apple == 0:
            self.add_random_apple()

    def add_random_apple(self):
        apple = Apple()


game = Game(35,20,1)

snake = Snake()