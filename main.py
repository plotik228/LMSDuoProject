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
        draw(screen, width, height)
        font = pygame.font.Font(None, 70)
        text = font.render("PLAY", True, (255, 255, 255))
        tw = width // 2 - text.get_width() // 2
        th = height // 2 - text.get_height() // 2
        screen.blit(text, (tw, th))

        if (pygame.mouse.get_pos()[0] >= tw and pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2 and
                pygame.mouse.get_pos()[1] >= th and pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
                text = font.render("PLAY", True, (128, 128, 128))
                screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        else:
            text = font.render("PLAY", True, (255, 255, 255))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= width // 2 - text.get_width() // 2 and
                        pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2 and
                        pygame.mouse.get_pos()[1] >= height // 2 - text.get_height() // 2 and
                        pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
                            screen.fill((0, 0, 0))
                            running = False

            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()

y = 0

def one_night_text(screen):
    global y
    font = pygame.font.SysFont('Consolas', 60)
    text = font.render('12:00 AM', True, (255, 255, 255))
    alpha = pygame.Surface(text.get_size(), pygame.SRCALPHA)
    alpha.fill((255, 255, 255, y))
    text.blit(alpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(text, (600 - text.get_width() // 2, 475 - text.get_height() // 2))
    if y != 255:
        y = y + 1

clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 950
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    running = True
    while running:
        one_night_text(screen)
        pygame.display.flip()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
