from OpenGL.GL import *


light_diffuse_color = (1.0, 1.0, 1.0)
light_const_attenuation = 0.9
light_pos = (0.0, 5.0, -5.0, 1)


def init_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse_color)
    # If the light is positional, rather than directional, its intensity is attenuated by the reciprocal of the sum
    # of the constant factor, the linear factor times the distance between the light and the vertex being lighted,
    # and the quadratic factor times the square of the same distance
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, light_const_attenuation)
