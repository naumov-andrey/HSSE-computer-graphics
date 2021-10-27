import src.lab2.camera_motion as camera
import src.lab2.load_texture as texture

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


torus_outer_radius, torus_inner_radius = 0.5, 0.3
torus_pos = (0., 0., -1.)
torus_color = (1., 1., 0., 1.)
torus_specular = (0., 0., 0., 0.)

cone_height, cone_radius = 1, 0.5
cone_pos = (0.9, 0.8, 0.8)
cone_color = (0.2, 0.2, 0.4, 0.7)

sphere_radius = 1
sphere_pos = (1.5, 0., -2.)
sphere_color = (1., 1., 1., 1.)
sphere_texture = None

cylinder_height, cylinder_radius = 2., 0.5
cylinder_pos = (-0.5, -1., 0.)
cylinder_color = (0.3, 0.6, 0.1, 1.)
cylinder_specular = (1., 1., 1., 1.)
cylinder_shininess = 100.

light_pos = [0., 0., 4., 1.]
light_const_attenuation = 0.8
light_color = [0.8, 0.8, 0.8]
light_angle = 0

polygon_number = 64


def draw_light():
    glRotatef(light_angle, 1., 0., 0.)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    # If the light is positional, rather than directional, its intensity is attenuated by the reciprocal of the sum
    # of the constant factor, the linear factor times the distance between the light and the vertex being lighted,
    # and the quadratic factor times the square of the same distance
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, light_const_attenuation)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.1)


# матовый тор
def draw_torus():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, torus_color)    # отраженный свет
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, torus_specular)
    glutSolidTorus(torus_inner_radius, torus_outer_radius, polygon_number, polygon_number)


# полупрозрачный конус
def draw_cone():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, cone_color)
    glutSolidCone(cone_radius, cone_height, polygon_number, polygon_number)


# текстурированная сфера
def draw_sphere():
    glEnable(GL_TEXTURE_2D)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, sphere_color)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    gluSphere(qobj, sphere_radius, polygon_number, polygon_number)
    gluDeleteQuadric(qobj)

    glDisable(GL_TEXTURE_2D)


# отполированный цилиндр
def draw_cylinder():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, cylinder_color)         # отраженный свет
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, cylinder_specular)     # коэффициент блеска
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, cylinder_shininess)

    glutSolidCylinder(cylinder_radius, cylinder_height, polygon_number, polygon_number)


def draw():
    global sphere_texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # в кадр попадет все, что внутри усеченной пирамиды от 0.5 до 20 по направлению камеры
    gluPerspective(40., 1., 0.5, 20)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*camera.eye_pos, *camera.center_pos, *camera.up_direction)

    glPushMatrix()
    draw_light()
    glPopMatrix()

    if not sphere_texture:
        sphere_texture = texture.read_texture('../../resources/sphere_texture.jpg')

    draw_objects = ((draw_torus, torus_pos),
                    (draw_sphere, sphere_pos),
                    (draw_cylinder, cylinder_pos),
                    (draw_cone, cone_pos),
                    )

    for draw_func, pos in draw_objects:
        glPushMatrix()
        glTranslatef(*pos)
        draw_func()
        glPopMatrix()

    glFlush()
