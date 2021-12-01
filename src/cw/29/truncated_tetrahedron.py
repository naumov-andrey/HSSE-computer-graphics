from math import sqrt, cos, sin, acos, atan, degrees, radians, pi
from OpenGL.GL import *
from OpenGL.GLUT import *
from utils import *


class TruncatedTetrahedron:
    INRADIUS = sqrt(6) / 12     # радиус вписанной сферы
    MIDRADIUS = sqrt(2) / 4     # расстояние от центра до середины стороны
    CIRCUMRADIUS = sqrt(6) / 4  # радиус описанной сферы
    HEIGHT = sqrt(6) / 3        # высота
    
    ROLLING_ANGLE = 2 * degrees(atan(sqrt(2)))  # угол поворота, приблизительно 109
    DIHEDRL_ANGLE = degrees(acos(1 / 3))        # двугранный угол, приблизительно 71
    
    # описание граней через вершины
    __TINDICES = ( 
        (0, 1, 2),
        (1, 4, 2),
        (4, 3, 2),
        (3, 0, 2),
        (0, 3, 4),
        (0, 1, 4)
    )
    
    TEXTURE_COORDS = ((0, 0), (1, 0), (0.5, 1))
    
    __FIRST_POSITION_DIRECTIONS = [[1 / 6 * pi + i * 2 / 3 * pi for i in range(3)],
                                   [7 / 6 * pi + i * 2 / 3 * pi for i in range(3)]]
    __FIRST_POSITION_ROTATIONS = [-1 / 3 * pi + i * 2 / 3 * pi for i in range(3)]
    __SECOND_POSITION_DIRECTIONS = [[1 / 2 * pi + i * 2 / 3 * pi for i in range(3)],
                                    [3 / 2 * pi + i * 2 / 3 * pi for i in range(3)]]
    __SECOND_POSITION_ROTATIONS = [i * 2 / 3 * pi for i in range(3)]
    
    PATH = (0, 2, 0, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0)
    
    
    def __init__(self, *, a=1, x=0, y=0, z=0, angular_velocity=1, texture=None, color=(1, 1, 1)):
        self.a = a
        self.x, self.y, self.z = x, y, z
        self.angular_velocity = angular_velocity
        self.texture = texture
        self.color = color
        
        self.__rotation = self.__FIRST_POSITION_ROTATIONS[0]
        self.__direction = self.__FIRST_POSITION_DIRECTIONS[0][0]
        self.__rotation_angle = 0
        self.__is_clockwise = True
        
        self.__current_pos = 0
        
        R = sqrt(3) / 3 # радиус описанной сферы вокруг правильного прямоугольника
        self.__vdata = [
            (R * cos(-5 / 6 * pi), -self.INRADIUS, R * sin(-5 / 6 * pi)),
            (R * cos(-1 / 6 * pi), -self.INRADIUS, R * sin(-1 / 6 * pi)),
            (0, self.CIRCUMRADIUS, 0),
            (0, -self.INRADIUS, R),
            (0, -self.INRADIUS, 0)
        ]
    
    
    def set_texture(self, texture):
        self.texture = texture
    
    
    def change_direction(self):
        if self.__is_clockwise and self.__direction in self.__FIRST_POSITION_DIRECTIONS[0]:
            self.__direction = self.__FIRST_POSITION_DIRECTIONS[1][self.PATH[self.__current_pos]]
        
        elif self.__is_clockwise and self.__direction in self.__SECOND_POSITION_DIRECTIONS[0]:
            self.__direction = self.__SECOND_POSITION_DIRECTIONS[1][self.PATH[self.__current_pos]]
        
        elif not self.__is_clockwise and self.__direction in self.__FIRST_POSITION_DIRECTIONS[1]:
            self.__direction = self.__FIRST_POSITION_DIRECTIONS[0][self.PATH[self.__current_pos]]
            
        elif not self.__is_clockwise and self.__direction in self.__SECOND_POSITION_DIRECTIONS[1]:
            self.__direction = self.__SECOND_POSITION_DIRECTIONS[0][self.PATH[self.__current_pos]]
        
        self.__is_clockwise = not self.__is_clockwise
    
    
    def display(self):
        angle_delta = self.__calculate_angle_delta()
        translation = self.__calculate_translation(angle_delta)
        direction_vector = calculate_unit_vector(self.__direction)
        
        self.x += direction_vector[0] * translation
        self.y += self.__calculate_rise(angle_delta)
        self.z += direction_vector[2] * translation
        glTranslate(self.x, self.y, self.z)
        
        self.__vdata = [rotate(v, calculate_unit_vector(self.__rotation), -angle_delta)
                        for v in self.__vdata]
        self.__rotation_angle += angle_delta
        if self.__is_rolled_over():
            self.__update_position()
            self.__update_rolling_properties()
        
        glScalef(self.a, self.a, self.a)
        self.__display_object()
    
    
    def __update_position(self):     
        if not self.__is_clockwise:
            self.__current_pos = (self.__current_pos - 1) % len(self.PATH)
        else:
            self.__current_pos = (self.__current_pos + 1) % len(self.PATH)
    
    
    def __is_rolled_over(self):
        if self.__is_clockwise:
            return self.__rotation_angle >= self.ROLLING_ANGLE
        return self.__rotation_angle <= 0
    
    
    def __display_object(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
        glBegin(GL_TRIANGLES)
        for i in range(6):
            glTexCoord2f(*self.TEXTURE_COORDS[0])
            glVertex3fv(self.__vdata[self.__TINDICES[i][0]])
            glTexCoord2f(*self.TEXTURE_COORDS[1])
            glVertex3fv(self.__vdata[self.__TINDICES[i][1]])
            glTexCoord2f(*self.TEXTURE_COORDS[2])
            glVertex3fv(self.__vdata[self.__TINDICES[i][2]])
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
    
    
    def __update_rolling_properties(self):
        self.__rotation_angle = 0 if self.__is_clockwise else self.ROLLING_ANGLE
        
        if self.__is_clockwise and self.__direction in self.__FIRST_POSITION_DIRECTIONS[0]:
            self.__rotation = self.__SECOND_POSITION_ROTATIONS[self.PATH[self.__current_pos]]
            self.__direction = self.__SECOND_POSITION_DIRECTIONS[0][self.PATH[self.__current_pos]]
        
        elif self.__is_clockwise and self.__direction in self.__SECOND_POSITION_DIRECTIONS[0]:
            self.__rotation = self.__FIRST_POSITION_ROTATIONS[self.PATH[self.__current_pos]]
            self.__direction = self.__FIRST_POSITION_DIRECTIONS[0][self.PATH[self.__current_pos]]
        
        elif not self.__is_clockwise and self.__direction in self.__FIRST_POSITION_DIRECTIONS[1]:
            self.__rotation = self.__SECOND_POSITION_ROTATIONS[self.PATH[self.__current_pos]]
            self.__direction = self.__SECOND_POSITION_DIRECTIONS[1][self.PATH[self.__current_pos]]
            
        elif not self.__is_clockwise and self.__direction in self.__SECOND_POSITION_DIRECTIONS[1]:
            self.__rotation = self.__FIRST_POSITION_ROTATIONS[self.PATH[self.__current_pos]]
            self.__direction = self.__FIRST_POSITION_DIRECTIONS[1][self.PATH[self.__current_pos]]
        
    
    def __calculate_angle_delta(self):
        if self.__is_clockwise:
            return min(self.ROLLING_ANGLE - self.__rotation_angle, self.angular_velocity)
        return -min(self.__rotation_angle, self.angular_velocity)
    
    
    def __calculate_translation(self, angle_delta):
        """ расчет перемещения в течение перекатывания """
        prev_angle = radians(180 - self.DIHEDRL_ANGLE / 2 - self.__rotation_angle)
        current_angle = prev_angle - radians(angle_delta)
        return self.__get_midradius() * abs(cos(current_angle) - cos(prev_angle))
        

    def __calculate_rise(self, angle_delta):
        """ расчет подъема в течение перекатывания"""
        prev_angle = radians(180 - self.DIHEDRL_ANGLE / 2 - self.__rotation_angle)
        current_angle = prev_angle - radians(angle_delta)
        return self.__get_midradius() * (sin(current_angle) - sin(prev_angle))
  
  
    def __get_midradius(self):
        return self.a * self.MIDRADIUS
