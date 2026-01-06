# Smiley Emoji Drawing
# Author: Osmond
# Date: 5 January 2026

import math

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 204, 0)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Smiley Emoji")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # Emoji position
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2
    FACE_RADIUS = 150

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # ----- FACE -----
        pygame.draw.circle(screen, YELLOW, (CENTER_X, CENTER_Y), FACE_RADIUS)

        # ----- EYES -----
        EYE_RADIUS = 12
        EYE_OFFSET_X = 45
        EYE_OFFSET_Y = 30

        pygame.draw.circle(
            screen,
            BLACK,
            (CENTER_X - EYE_OFFSET_X, CENTER_Y - EYE_OFFSET_Y),
            EYE_RADIUS,
        )
        pygame.draw.circle(
            screen,
            BLACK,
            (CENTER_X + EYE_OFFSET_X, CENTER_Y - EYE_OFFSET_Y),
            EYE_RADIUS,
        )

        # ----- SMILE -----
        smile_rect = pygame.Rect(CENTER_X - 70, CENTER_Y - 10, 140, 100)

        pygame.draw.arc(screen, BLACK, smile_rect, math.pi * 0.1, math.pi * 0.9, 6)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
