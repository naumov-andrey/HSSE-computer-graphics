from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, radians


eye_pos = [1.0, 0.1, 1.0]
center_pos = (0.0, 0.0, 0.0)
up_direction = (0.0, 1.0, 0.0)

delta = 0.1

fps = 25
ms_per_frame = 1000 // fps


def frame_limit(*args):
    glutTimerFunc(ms_per_frame, frame_limit, 0)
    glutPostRedisplay()


def handle_special_keys(key, *args):
    global eye_pos

    if key == GLUT_KEY_UP and glutGetModifiers() == 1:
        eye_pos[2] += delta
    elif key == GLUT_KEY_DOWN and glutGetModifiers() == 1:
        eye_pos[2] -= delta

    elif key == GLUT_KEY_RIGHT:
        eye_pos[0] += delta
    elif key == GLUT_KEY_LEFT:
        eye_pos[0] -= delta

    elif key == GLUT_KEY_UP:
        eye_pos[1] += delta
    elif key == GLUT_KEY_DOWN:
        eye_pos[1] -= delta

    glutPostRedisplay()



def display_axes():
    glBegin(GL_LINES)

    # x -- red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    # y -- green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    # z -- blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()


def R(theta, u):
    """ матрица поворота в трёхмерном пространстве """
    return [[cos(theta) + u[0] ** 2 * (1 - cos(theta)), 
             u[0] * u[1] * (1 - cos(theta)) - u[2] * sin(theta), 
             u[0] * u[2] * (1 - cos(theta)) + u[1] * sin(theta)],
            [u[0] * u[1] * (1 - cos(theta)) + u[2] * sin(theta),
             cos(theta) + u[1] ** 2 * (1 - cos(theta)),
             u[1] * u[2] * (1 - cos(theta)) - u[0] * sin(theta)],
            [u[0] * u[2] * (1 - cos(theta)) - u[1] * sin(theta),
             u[1] * u[2] * (1 - cos(theta)) + u[0] * sin(theta),
             cos(theta) + u[2] ** 2 * (1 - cos(theta))]]


def rotate(pointToRotate, u, theta):
    """ вращение точки относительно единичного вектора u на угол theta """
    theta = radians(theta)
    r = R(theta, u)
    rotated = []

    for i in range(3):
        rotated.append(sum([r[j][i] * pointToRotate[j] for j in range(3)]))

    return rotated
