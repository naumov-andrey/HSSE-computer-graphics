from OpenGL.GL import *
from OpenGL.GLUT import *


w, h = 1000, 1000

scale = 1.5
alpha = 90

start_outer_radius, start_inner_radius = 0.10, 0.05
start_rotation_angle = (0, 0., 0., 0.)

torus_outer_radius, torus_inner_radius = start_outer_radius, start_inner_radius
torus_x, torus_y = 0.4, 0.4

cylinder_radius, cylinder_height = 0.05, 0.2
cylinder_x, cylinder_y = 0.05, 0.15
cylinder_rotation_angle = start_rotation_angle

x_rotation_angle = 0.
y_rotation_angle = 0.
rotation_angle_delta = 2.


def handle_special_keys(key, *args):
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


def handle_char_keys(key, *args):
    global torus_outer_radius, torus_inner_radius
    global start_rotation_angle
    global cylinder_rotation_angle
    global start_outer_radius, start_inner_radius
    global alpha, scale

    if key == b' ':
        torus_outer_radius, torus_inner_radius = (torus_outer_radius * scale, torus_inner_radius * scale)\
            if (torus_outer_radius, torus_inner_radius) == (start_outer_radius, start_inner_radius)\
            else (start_outer_radius, start_inner_radius)

        cylinder_rotation_angle = start_rotation_angle\
            if cylinder_rotation_angle != (start_rotation_angle)\
            else (alpha, 0., 0., 1.)

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
    global cylinder_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    draw_axes()

    glColor3f(1., 1., 1.)

    glLoadIdentity()
    glRotatef(x_rotation_angle, 1., 0., 0.)
    glRotatef(y_rotation_angle, 0., 1., 0.)
    glTranslatef(torus_x, torus_y, 0.)
    glutWireTorus(torus_inner_radius, torus_outer_radius, 16, 16)

    glLoadIdentity()
    glRotatef(x_rotation_angle, 1., 0., 0.)
    glRotatef(y_rotation_angle, 0., 1., 0.)
    glRotatef(*cylinder_rotation_angle)
    glTranslatef(cylinder_x, cylinder_y, 0.)
    glutWireCylinder(cylinder_radius, cylinder_height, 16, 16)

    glutSwapBuffers()


def main():
    global w, h

    glutInit()
    # двойная буферизация и цвета в формате RGB
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(w, h)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Torus & Cylinder")

    glClearColor(0., 0., 0., 0.)

    # определяем процедуру, отвечающую за перерисовку
    glutDisplayFunc(draw)
    # определям процедуры, обрабатывающие нажатия клавиш
    glutSpecialFunc(handle_special_keys)
    glutKeyboardFunc(handle_char_keys)

    glutMainLoop()


if __name__ == '__main__':
    main()
