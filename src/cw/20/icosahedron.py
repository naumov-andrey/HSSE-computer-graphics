from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, pi, sqrt, acos, degrees, radians
from utils import *


class Icosahedron:
    MIDRADIUS = 0.25 * (1 + sqrt(5))
    ROLLING_ANGLE = degrees(acos(sqrt(5) / 3))  # approx 42 degrees
    DIHEDRL_ANGLE = degrees(acos(-sqrt(5) / 3)) # approx 138 degrees

    __TINDICES = (
        (0, 4, 1), (0, 9, 4), (9, 5, 4), (4, 5, 8), (4, 8, 1),
        (8, 10, 1), (8, 3, 10), (5, 3, 8), (5, 2, 3), (2, 7, 3),
        (7, 10, 3), (7, 6, 10), (7, 11, 6), (11, 0, 6), (0, 1, 6),
        (6, 1, 10), (9, 0, 11), (9, 11, 2), (9, 2, 5), (7, 2, 11) 
    )


    def __init__(self, *, color=(1, 1, 1), a=1, x=0, y=0, z=0, angular_velocity=1):
        self.color = color

        self.a = a
        self.x, self.y, self.z = x, y, z
        self.angular_velocity = angular_velocity

        self.__rotation_vector = None
        self.__direction_vector = None
        self.__rotation_angle = 0
        self.__is_rolling = False
        self.__is_up = False # расположение грани: либо треугольник, либо перевернутый треугольник
        
        X = 0.525731112119133606 
        Z = 0.850650808352039932
        
        self.__vdata = [
            (-X, 0.0, Z), (X, 0.0, Z), (-X, 0.0, -Z), (X, 0.0, -Z),
            (0.0, Z, X) , (0.0, Z, -X), (0.0, -Z, X), (0.0, -Z, -X),
            (Z, X, 0.0) , (-Z, X, 0.0), (Z, -X, 0.0), (-Z, -X, 0.0)
        ]
        # выравниваем фигуру
        self.__vdata = [rotate(v, (0, 0, 1), -self.ROLLING_ANGLE / 2) for v in self.__vdata]
        

    def display(self):
        glTranslate(self.x, self.y, self.z)
        
        if self.__is_rolling:
            # приращение равно угловой скорости пока не доходит почти до конца. 
            # В таком случае будет равно оставшемуся углу до финального
            angle_delta = min(self.ROLLING_ANGLE - self.__rotation_angle, self.angular_velocity)
            
            translation = self.__calculate_translation(angle_delta)
            glTranslate(self.__direction_vector[0] * translation, 
                        self.__calculate_rise(angle_delta), 
                        self.__direction_vector[2] * translation)
            
            self.__vdata = [rotate(v, self.__rotation_vector, -angle_delta) for v in self.__vdata]
            
            self.__rotation_angle += self.angular_velocity
            if self.__rotation_angle >= self.ROLLING_ANGLE:
                self.x += self.__direction_vector[0] * translation
                self.z += self.__direction_vector[2] * translation
                
                self.__rotation_angle = 0
                self.__is_rolling = False
                self.__is_up = not self.__is_up
        
        glScalef(self.a, self.a, self.a)
        self.__display_object()
    
    
    def roll(self, direction):
        """ 
        direction vector (вектор направления) перпендикулярен rotation vector (вектор вращения) 
        """
        if self.__is_rolling:
            return
        
        if direction == 'w':
            # если грань, на которой расположен икосэдр, перевернута на 180 градусов,
            # то существует смежная грань сверху, иначе -- игнорируем 
            if not self.__is_up:
                self.__rotation_vector = (0, 0, -1)
                self.__direction_vector = (1, 0, 0)
            else:
                return
        
        elif direction == 'a':
            if self.__is_up:
                self.__rotation_vector = (sin(4 / 3 * pi), 0, cos(4 / 3 * pi))
                self.__direction_vector = (sin(5 / 6 * pi), 0, cos(5 / 6 * pi))
            else:
                self.__rotation_vector = (sin(5 / 3 * pi), 0, cos(5 / 3 * pi))
                self.__direction_vector = (sin(7 / 6 * pi), 0, cos(7 / 6 * pi))
            
        
        elif direction == 's':
            # если грань, на которой расположен икосэдр, перевернута на 180 градусов,
            # то не существует смежной грани снизу
            if self.__is_up:
                self.__rotation_vector = (0, 0, 1)
                self.__direction_vector = (-1, 0, 0)
            else:
                return
        
        elif direction == 'd':
            if self.__is_up:
                self.__rotation_vector = (sin(2 / 3 * pi), 0, cos(2 / 3 * pi))
                self.__direction_vector = (sin(1 / 6 * pi), 0, cos(1 / 6 * pi))
            else:
                self.__rotation_vector = (sin(1 / 3 * pi), 0, cos(1 / 3 * pi))
                self.__direction_vector = (sin(-1 / 6 * pi), 0, cos(-1 / 6 * pi))
        
        else:
            raise ValueError(f'No such {direction=}')
        
        self.__is_rolling = True

    
    def __display_object(self):
        glBegin(GL_TRIANGLES)    
        for i in range(20):
            glColor3f(i * 0.04 + 0.1, i * 0.05, i * 0.02 + 0.5)  
            glVertex3fv(self.__vdata[self.__TINDICES[i][0]])
            glVertex3fv(self.__vdata[self.__TINDICES[i][1]])
            glVertex3fv(self.__vdata[self.__TINDICES[i][2]])
        glEnd()
    

    def __calculate_translation(self, angle_delta):
        prev_angle = radians(180 - self.DIHEDRL_ANGLE / 2)
        current_angle = prev_angle - radians(self.__rotation_angle + angle_delta)
        return self.__get_midradius() * abs(cos(current_angle) - cos(prev_angle))


    def __calculate_rise(self, angle_delta):
        prev_angle = radians(180 - self.DIHEDRL_ANGLE / 2)
        current_angle = prev_angle - radians(self.__rotation_angle + angle_delta)
        return self.__get_midradius() * (sin(current_angle) - sin(prev_angle))
  
  
    def __get_midradius(self):
        return self.a * self.MIDRADIUS
