import control_points as ctrl_points
import mouse_motion as mouse_mtn
import light_motion as light_mth
import display as disp

from OpenGL.GL import *
from OpenGL.GLUT import *


w, h = 1000, 1000


def idle():
    ctrl_points.current_iteration = min(ctrl_points.max_iteration, ctrl_points.current_iteration + 1)

    glutPostRedisplay()


def handle_keyboard(key, *args):
    if key == b'\x1b':  # esc key
        glutLeaveMainLoop()

    elif key == b' ':
        ctrl_points.current_iteration = 0

    elif key in [b'w', b'a', b's', b'd']:
        light_mth.move_light(key)

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(w, h)
    glutInitWindowPosition(200, 40)
    glutCreateWindow("Lab 3")

    glEnable(GL_NORMALIZE)
    # glEnable(GL_AUTO_NORMAL)
    disp.set_light()

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_MAP2_VERTEX_3)

    glutDisplayFunc(disp.display)
    glutIdleFunc(idle)
    glutMotionFunc(mouse_mtn.motion)
    glutMouseFunc(mouse_mtn.handle_mouse)
    glutKeyboardFunc(handle_keyboard)

    glutMainLoop()


if __name__ == '__main__':
    main()
