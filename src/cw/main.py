from light import Light
from icosahedron import Icosahedron
from utils import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


w, h = 1000, 1000

icosahedron = Icosahedron(color=(0.4, 1.0, 0.6),
                          a=0.2, 
                          y=Icosahedron.MIDRADIUS * 0.2)
light = Light(pos=(0.0, 4.0, 0.0, 1.0))


def handle_keyboard(key, *args):
    if key == b'\x1b':  # esc key
        glutLeaveMainLoop()

    elif key in b'wasd':
        icosahedron.roll(direction=key.decode('UTF-8'))

    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # в кадр попадет все, что внутри усеченной пирамиды от 0.5 до 20 по направлению камеры
    gluPerspective(40., 1., 0.5, 20)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*eye_pos, *center_pos, *up_direction)

    display_axes()
    light.display()
    
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.7, 0.7)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 0, 10)
    glEnd()
    
    icosahedron.display()
    
    glutSwapBuffers()


def set_callbacks():
    glutDisplayFunc(display)
    glutKeyboardFunc(handle_keyboard)
    glutSpecialFunc(handle_special_keys)
    frame_limit()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    glutInitWindowSize(w, h)
    glutInitWindowPosition(200, 40)
    glutCreateWindow("CW")

    glEnable(GL_NORMALIZE)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)

    glViewport(0, 0, w, h)
    light.init()

    set_callbacks()
    glutMainLoop()


if __name__ == '__main__':
    main()
