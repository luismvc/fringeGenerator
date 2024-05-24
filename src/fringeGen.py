import numpy as np


def fringe_generator(w=800, h=600, desired_period=50, flag_vert=True, phase=0):

    d_p = desired_period

    max_val = 127.0
    fringe_pattern = np.zeros((w, h, 3), dtype=np.uint8)

    pattern = np.zeros((w, h))
    if flag_vert:
        x = range(w)
        z = []

        for i in x:
            value = (255.0 - max_val) + max_val * np.cos(
                x[i] * 2.0 * np.pi / d_p + phase
            )
            z.append(value)

        for i in range(h):
            pattern[:, i] = z

    else:

        y = range(h)
        z = []

        for i in y:
            value = (255.0 - max_val) + max_val * np.sin(
                y[i] * 2.0 * np.pi / d_p + phase
            )
            z.append(value)

        for i in range(w):
            pattern[i, :] = z

    fringe_pattern[..., 0] = pattern
    fringe_pattern[..., 1] = pattern
    fringe_pattern[..., 2] = pattern

    return fringe_pattern
