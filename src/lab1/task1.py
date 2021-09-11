from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.3, 0.8, 0.3)
    glMatrixMode(GL_MODELVIEW)

    #
    glLoadIdentity()
    # сдвигаемся по осям
    glTranslatef(0., 0., 0.)
    # вращаемся по осям
    glRotatef(-120, 1., 0., 0.)
    glutWireCone(1., 1., 16, 16)

    glutSwapBuffers()


def main():
    # инициализация OpenGl
    glutInit()
    # двойная буферизация и цвета в формате RGB
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(1000, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Lab 1")

    glClearColor(0., 0., 0., 0.)

    # определяем процедуру, отвечающую за перерисовку
    glutDisplayFunc(draw)

    glutMainLoop()


if __name__ == '__main__':
    main()
