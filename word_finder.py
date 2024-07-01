import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Finder")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.Font(None, 36)

GRID_SIZE = 10
CELL_SIZE = 50
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
WORDS = ["PYTHON", "CODE", "GAME", "DEBUG", "COMPILE", "SYNTAX", "FUNCTION", "VARIABLE", "LOOP", "ARRAY","salik","abdul"]

grid = [[random.choice(LETTERS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def place_words():
    for word in WORDS:
        direction = random.choice(['H', 'V'])  
        word_len = len(word)
        placed = False

        while not placed:
            if direction == 'H':
                row = random.randint(0, GRID_SIZE - 1)
                col = random.randint(0, GRID_SIZE - word_len)
                if all(grid[row][col + i] == ' ' or grid[row][col + i] == word[i] for i in range(word_len)):
                    for i in range(word_len):
                        grid[row][col + i] = word[i]
                    placed = True
            else: 
                row = random.randint(0, GRID_SIZE - word_len)
                col = random.randint(0, GRID_SIZE - 1)
                if all(grid[row + i][col] == ' ' or grid[row + i][col] == word[i] for i in range(word_len)):
                    for i in range(word_len):
                        grid[row + i][col] = word[i]
                    placed = True

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        grid[row][col] = ' '

place_words()

selected_cells = []
found_words = []

def check_word(selected):
    word = ''.join([grid[row][col] for row, col in selected])
    if word in WORDS:
        found_words.append(word)
        for row, col in selected:
            grid[row][col] = grid[row][col].lower() 
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if (row, col) not in selected_cells:
                selected_cells.append((row, col))
            else:
                selected_cells.remove((row, col))
            if check_word(selected_cells):
                selected_cells = []

    screen.fill(WHITE)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = YELLOW if (row, col) in selected_cells else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            letter = font.render(grid[row][col], True, color)
            screen.blit(letter, (col * CELL_SIZE + 15, row * CELL_SIZE + 10))

    y_offset = GRID_SIZE * CELL_SIZE + 10
    for word in WORDS:
        color = RED if word in found_words else BLUE
        word_text = font.render(word, True, color)
        screen.blit(word_text, (10, y_offset))
        y_offset += 30

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
