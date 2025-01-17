import pygame
import sys
import random

def draw(screen, width, height):
    for i in range(2222):
        screen.fill(pygame.Color((160, 160, 160)),
                    (random.random() * width,
                     random.random() * height, 1, 1))
def zastavka(screen, width, height):
    global font
    font = pygame.font.Font(None, 70)
    global text
    text = font.render("PLAY", True, (255, 255, 255))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 950
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        screen.fill((0, 0, 0))
        zastavka(screen, width, height)
        draw(screen, width, height)
        pygame.display.flip()

        if (pygame.mouse.get_pos()[0] >= width // 2 - text.get_width() // 2 and
                pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2):
            if (pygame.mouse.get_pos()[1] >= height // 2 - text.get_height() // 2 and
                pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
                text = font.render("PLAY", True, (128, 128, 128))
                screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        else:
            text = font.render("PLAY", True, (255, 255, 255))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
