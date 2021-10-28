import src.lab3.control_points as ctrl_points
import src.lab3.light_motion as light_mtn
import src.lab3.mouse_motion as mouse_mtn

from OpenGL.GL import *
from OpenGL.GLUT import *


surface_color = (0.8, 0.1, 0.1, 0.9)

grid_size = 3

light_color = (1.0, 1.0, 1.0, 1.0)


def set_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.8)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.1)


def toggle_grid_size():
    global grid_size

    grid_size = 20 \
        if grid_size == ctrl_points.points_shape[0] - 1 \
        else ctrl_points.points_shape[0] - 1


def display_points(points):
    glEnable(GL_COLOR_MATERIAL)
    glPointSize(3)
    glColor3d(1, 1, 1)
    glBegin(GL_POINTS)
    for line in points:
        for point in line:
            glVertex3fv(point)
    glEnd()
    glDisable(GL_COLOR_MATERIAL)


def display_surface():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, surface_color)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)

    glMapGrid2f(grid_size, 0, 1, grid_size, 0, 1)
    glEvalMesh2(GL_FILL, 0, grid_size, 0, grid_size)
    glEnable(GL_AUTO_NORMAL)

    glDisable(GL_BLEND)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_ACCUM_BUFFER_BIT)

    glLightfv(GL_LIGHT0, GL_POSITION, light_mtn.light_pos)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glRotated(mouse_mtn.angle_x, 1, 0, 0)
    glRotated(mouse_mtn.angle_y, 0, 1, 0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    points = ctrl_points.calculate_points(ctrl_points.current_iteration / ctrl_points.max_iteration)
    glMap2f(target=GL_MAP2_VERTEX_3, u1=0, u2=1, v1=0, v2=1, points=points)

    display_points(points)
    display_surface()

    glutSwapBuffers()
