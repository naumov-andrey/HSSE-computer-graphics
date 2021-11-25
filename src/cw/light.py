from OpenGL.GL import *


class Light:
    def __init__(self,
                 pos,
                 color=(1.0, 1.0, 1.0),
                 const_attenuation=0.8,
                 linear_attenuation=0.1):
        self.pos = pos
        self.color = color
        self.const_attenuation = const_attenuation
        self.linear_attenuation = linear_attenuation


    def init(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.color)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.color)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, self.const_attenuation)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, self.linear_attenuation)


    def display(self):
        glLightfv(GL_LIGHT0, GL_POSITION, self.pos)

