import sys

import numpy as np
import pygame
from pygame.locals import *
from src.fringeGen import *


def setup_screen(w, h):

    pygame.init()
    size = (w, h)

    # return pygame.display.set_mode(size, pygame.RESIZABLE, pygame.FULLSCREEN)
    return pygame.display.set_mode(size, pygame.FULLSCREEN)


def process(config_param):

    # getting parameters
    w = config_param["width"]
    h = config_param["height"]
    fps = config_param["fps"]

    flag_vert = config_param["vertical_fringe"]

    d_p = config_param["initial_period"]

    phase = config_param["initial_phase"]

    delta_ph = config_param["delta_phase_deg"]
    # ---------------------

    motion = False
    count = 0

    done_flag = False
    scene = setup_screen(w, h)
    clock = pygame.time.Clock()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Key handler

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done_flag = True
                    break  # break out of the for loop

                # --- Changing the Period ----
                # Click right arrow to increase the period
                elif event.key == pygame.K_RIGHT:
                    d_p += 2
                    break  # break out of the for loop

                # Click right arrow to increase the period
                elif event.key == pygame.K_LEFT:
                    d_p -= 2

                    d_p = max(d_p, 1)

                    print(d_p)

                    break  # break out of the for loop
                # -----------------------------------------

                # Prss 's' to move fringes automatically
                elif event.key == pygame.K_s:
                    motion = not motion

                    break  # break out of the for loop

                # Prss 'f' to move fringes three times. This is usefull for 4 phase shifting
                elif event.key == pygame.K_f:

                    if count == 3:
                        break

                    phase += delta_ph * np.pi / 180
                    count += 1

                    break  # break out of the for loop

        if done_flag:
            break  # to break out of the while loop

        # Creating the fringe pattern with the desired period and corresponding shift phase
        fringe_pattern = fringe_generator(w, h, d_p, flag_vert, phase)

        fg = pygame.surfarray.make_surface(fringe_pattern)
        scene.blit(fg, (0, 0))
        pygame.display.update()  # update the display

        if motion:
            phase += delta_ph * np.pi / 180.0

        clock.tick(fps)
