from OpenGL.GLUT import *

angle_x, angle_y = 45, 45
old_x, old_y = 0, 0


def handle_mouse(button, state, x, y):
    global old_x, old_y
    old_x = x
    old_y = y

    glutPostRedisplay()


def motion(x, y):
    global angle_x, angle_y
    angle_y = x - old_x
    angle_x = y - old_y

    glutPostRedisplay()