light_pos = [0.0, 0.5, 0.0]
light_pos_delta = 0.005


def move_light(direction):
    global light_pos

    if direction == b'w':
        light_pos[1] += light_pos_delta
    elif direction == b's':
        light_pos[1] -= light_pos_delta
    elif direction == b'd':
        light_pos[0] += light_pos_delta
    elif direction == b'a':
        light_pos[0] -= light_pos_delta
