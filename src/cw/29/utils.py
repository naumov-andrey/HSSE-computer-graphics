from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, radians
from PIL.Image import open
import numpy as np


eye_pos = [5.5, 6.5, -3.5]
center_pos = (0.0, 0.0, 0.0)
up_direction = (0.0, 1.0, 0.0)


def read_texture(filename):
    img = open(filename)
    img_data = np.array(list(img.getdata()), np.int8)
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D,
                 0, 
                 GL_RGB, 
                 img.size[0], 
                 img.size[1], 
                 0, 
                 GL_RGB, 
                 GL_UNSIGNED_BYTE, 
                 img_data)
    
    return texture_id


def frame_limit(*args):
    # количество мс на кадр
    glutTimerFunc(1000 // 30, frame_limit, 0)
    glutPostRedisplay()


def handle_special_keys(key, *args):
    global eye_pos

    pos_delta = 0.1
    if key == GLUT_KEY_UP and glutGetModifiers() == 1:
        eye_pos[2] += pos_delta
    elif key == GLUT_KEY_DOWN and glutGetModifiers() == 1:
        eye_pos[2] -= pos_delta

    elif key == GLUT_KEY_RIGHT:
        eye_pos[0] += pos_delta
    elif key == GLUT_KEY_LEFT:
        eye_pos[0] -= pos_delta

    elif key == GLUT_KEY_UP:
        eye_pos[1] += pos_delta
    elif key == GLUT_KEY_DOWN:
        eye_pos[1] -= pos_delta


def R(theta, u):
    """ подсчет матрицы поворота """
    return [
        [cos(theta) + u[0] ** 2 * (1 - cos(theta)), 
         u[0] * u[1] * (1 - cos(theta)) - u[2] * sin(theta), 
         u[0] * u[2] * (1 - cos(theta)) + u[1] * sin(theta)],
        [u[0] * u[1] * (1 - cos(theta)) + u[2] * sin(theta),
         cos(theta) + u[1] ** 2 * (1 - cos(theta)),
         u[1] * u[2] * (1 - cos(theta)) - u[0] * sin(theta)],
        [u[0] * u[2] * (1 - cos(theta)) - u[1] * sin(theta),
         u[1] * u[2] * (1 - cos(theta)) + u[0] * sin(theta),
         cos(theta) + u[2] ** 2 * (1 - cos(theta))]]


def rotate(point_to_rotate, u, theta):
    """ вращение точки относительно u на theta """
    theta = radians(theta)
    r = R(theta, u)
    rotated = []

    for i in range(3):
        rotated.append(sum([r[j][i] * point_to_rotate[j] for j in range(3)]))

    return rotated


def calculate_unit_vector(angle):
    """ возвращает едининчый вектор в плоскости Oxz на основе угла поворота """
    return (cos(angle), 0, sin(angle))
    