from OpenGL.GL import *


class Surface:
  def __init__(self, *, color, a):
    self.color = color
    self.a = a
  
  
  def display(self):
    glEnable(GL_COLOR_MATERIAL)
    glBegin(GL_QUADS)
    glColor3fv(self.color)
    glVertex3f(self.a, 0, self.a)
    glVertex3f(self.a, 0, -self.a)
    glVertex3f(-self.a, 0, -self.a)
    glVertex3f(-self.a, 0, self.a)
    glEnd()
    glDisable(GL_COLOR_MATERIAL)
