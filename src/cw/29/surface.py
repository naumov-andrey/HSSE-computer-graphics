from OpenGL.GL import *


class Surface:
    def __init__(self, *, color, a):
        self.color = color
        self.a = a
    
  
    def set_texture(self, texture):
        self.texture = texture
  
  
    def display(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
    
        glScale(self.a, self.a, self.a)
        glBegin(GL_QUADS)
        
        glTexCoord(1, 1)
        glVertex3f(1, 0, 1)
        glTexCoord(1, 0)
        glVertex3f(1, 0, -1)
        glTexCoord(0, 0)
        glVertex3f(-1, 0, -1)
        glTexCoord(0, 1)
        glVertex3f(-1, 0, 1)
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
