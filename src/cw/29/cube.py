from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cube:
    CORDS = (
        ((-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5)),   # back
        ((-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)),       # front
        ((-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5)),   # left
        ((0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)),       # right
        ((-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5)),       # top
        ((-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5))    # bottom
    )
    TEXTURE_CORDS = (
        ((1, 0), (1, 1), (0, 1), (0, 0)),   # back
        ((0, 0), (1, 0), (1, 1), (0, 1)),   # front
        ((0, 0), (1, 0), (1, 1), (0, 1)),   # left
        ((1, 0), (1, 1), (0, 1), (0, 0)),   # right
        ((0, 1), (0, 0), (1, 0), (1, 1)),   # top
        ((1, 1), (0, 1), (0, 0), (1, 0))    # bottom
    )
    
    def __init__(self, *, a=1, x=0, y=0, z=0):
        self.a = a
        self.x, self.y, self.z = x, y, z
    
    
    def set_texture(self, texture):
        self.texture = texture
        
        
    def display(self):
        glEnable(GL_TEXTURE_2D)
        
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
        glTranslate(self.x, self.y, self.z)
        glScale(self.a, self.a, self.a)
        
        glColor3f(1, 1, 1)
        
        for i in range(6):
            glBegin(GL_QUADS)
            for j in range(4):
                glTexCoord2fv(self.TEXTURE_CORDS[i][j])
                glVertex3fv(self.CORDS[i][j])
            glEnd()
        
        glDisable(GL_TEXTURE_2D)
