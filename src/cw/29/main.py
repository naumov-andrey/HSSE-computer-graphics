from light import *
from truncated_tetrahedron import *
from surface import *
from cube import *
from utils import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt


tetrahedron = TruncatedTetrahedron(x=-1,
                                   y=TruncatedTetrahedron.INRADIUS,
                                   z=2 * sqrt(3) / 3,
                                   angular_velocity=6,
                                   color=(1.0, 1.0, 1.0))
surface = Surface(color=(1, 0.6, 0.5), a=5)
cube = Cube(a=1, x=0, y=0.5, z=0)


def handle_keyboard(key, *args):
    if key == b'\x1b':  # esc
        glutLeaveMainLoop()
    
    elif key == b' ':
        tetrahedron.change_direction() 


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # в кадр попадет все, что внутри усеченной пирамиды от 0.5 до 30 по направлению камеры
    gluPerspective(40, 1, 0.5, 30)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*eye_pos, *center_pos, *up_direction)
    
    glPushMatrix()
    init_light()
    glPopMatrix()

    glPushMatrix()
    tetrahedron.display()
    glPopMatrix()
    
    glPushMatrix()
    cube.display()
    glPopMatrix()
    
    glPushMatrix()
    surface.display()
    glPopMatrix()
    
    glutSwapBuffers()


def set_callbacks():
    glutDisplayFunc(display)
    glutKeyboardFunc(handle_keyboard)
    glutSpecialFunc(handle_special_keys)
    frame_limit()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    width, height = 800, 800
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 50)
    glutCreateWindow("course work")

    glEnable(GL_NORMALIZE)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glViewport(0, 0, width, height)
    
    set_callbacks()
    cube.set_texture(read_texture('./resources/t5.jpg'))
    tetrahedron.set_texture(read_texture('./resources/t10.jpg'))
    surface.set_texture(read_texture('./resources/t11.jpg'))
    
    glutMainLoop()


if __name__ == '__main__':
    main()
