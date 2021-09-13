from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


w, h = 1000, 1000

cone_height, cone_radius = 0.25, 0.05
cone_x, cone_y = 0.1, 0.1

sphere_radius = 0.05
sphere_x, sphere_y = 0.2, 0.2

x_rotation_angle = 0.
y_rotation_angle = 0.

rotation_angle_delta = 2.


def handle_special_keys(key, x, y):
    global x_rotation_angle, y_rotation_angle

    if key == GLUT_KEY_UP:
        x_rotation_angle -= rotation_angle_delta
    elif key == GLUT_KEY_DOWN:
        x_rotation_angle += rotation_angle_delta
    elif key == GLUT_KEY_LEFT:
        y_rotation_angle -= rotation_angle_delta
    elif key == GLUT_KEY_RIGHT:
        y_rotation_angle += rotation_angle_delta

    glutPostRedisplay()


def handle_char_keys(key, x, y):
    global cone_x, cone_y, sphere_x, sphere_y

    if key == b' ':
        sphere_x, sphere_y = (cone_x, cone_y)\
            if (sphere_x, sphere_y) != (cone_x, cone_y)\
            else (0.2, 0.2)

    glutPostRedisplay()


def draw_axes():
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    glRotatef(x_rotation_angle, 1., 0., 0.)
    glRotatef(y_rotation_angle, 0., 1., 0.)
    glBegin(GL_LINES)

    # x -- red
    glColor3f(1., 0., 0.)
    glVertex3f(0., 0., 0.)
    glVertex3f(1., 0., 0.)

    # y -- green
    glColor3f(0., 1., 0.)
    glVertex3f(0., 0., 0.)
    glVertex3f(0., 1., 0.)

    # z -- blue
    glColor3f(0., 0., 1.)
    glVertex3f(0., 0., 0.)
    glVertex3f(0., 0., 1.)

    glEnd()


def draw():
    global x_rotation_angle, y_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    draw_axes()

    glLoadIdentity()
    glRotatef(x_rotation_angle, 1., 0., 0.)
    glRotatef(y_rotation_angle, 0., 1., 0.)

    glColor3f(0.2, 0.8, 0.2)
    glTranslatef(cone_x, cone_y, 0.)
    glutWireCone(cone_radius, cone_height, 16, 16)

    glColor3f(0.8, 0.2, 0.2)
    glTranslatef(sphere_x - cone_x, sphere_y - cone_y, 0.)
    glutWireSphere(sphere_radius, 16, 16)

    glutSwapBuffers()


def main():
    global w, h

    glutInit()
    # двойная буферизация и цвета в формате RGB
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(w, h)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Lab 1")

    glClearColor(0., 0., 0., 0.)

    # определяем процедуру, отвечающую за перерисовку
    glutDisplayFunc(draw)
    # определям процедуры, обрабатывающие нажатия клавиш
    glutSpecialFunc(handle_special_keys)
    glutKeyboardFunc(handle_char_keys)

    glutMainLoop()


if __name__ == '__main__':
    main()
