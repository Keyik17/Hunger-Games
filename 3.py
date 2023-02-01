#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk 
import time
import random

#Display the window using the Frame object.
#Use canvas to draw the graphical shapes.
root = tk.Tk()
Frame_Width = 800
Frame_Height = 600
root.geometry(f'{Frame_Width}x{Frame_Height}')
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width=Frame_Width, height=Frame_Height)
root.title("Hunger Games")\
    
#Define all attributes: x,y width, height, color, both velocities for x and y, shape, enemy.
class SHAPE:
    def __init__(self, x, y, width, height, color, velocity1, velocity2, shape, enemy):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 
        self.velocity1 = velocity1
        self.velocity2 = velocity2
        self.shape = shape
        self.enemy = enemy
     
        #Craete all neccessary shapes such as oval, circle, rectangle and the Square 
        if self.shape == 'Oval':
            self.item = canvas.create_oval([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        elif self.shape == 'Circle':
            self.item = canvas.create_oval([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        elif self.shape == 'Square':
            self.item = canvas.create_rectangle([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        else:
            self.item = canvas.create_rectangle([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
            
   #Create a fucntion to move the shapes around the window.
   #Set the velocities to be able to move the objects. 
    def move_item(self):
        self.x += self.velocity1
        self.y += self.velocity2
        
        if self.shape == 'Oval':
            self.item = canvas.create_oval([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        elif self.shape == 'Circle':
            self.item = canvas.create_oval([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        elif self.shape == 'Rectangle':
            self.item = canvas.create_rectangle([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
        else:
            self.item = canvas.create_rectangle([self.x, self.y, self.x + self.width, self.y + self.height],fill=self.color,width=0)
		
        #Make the objects bounce against the sides of the window by setting the velocities equal to negative.
        if self.y + self.height > Frame_Height:
            self.velocity2 = -self.velocity2
        if self.x + self.width > Frame_Width:
            self.velocity1 = - self.velocity1
        if self.y < 0:
            self.velocity2 = -self.velocity2
        if self.x < 0:
            self.velocity1 = -self.velocity1

def infection():
  for i in range(len(list_of_shapes)):
      for j in range(len(list_of_shapes)):
          if list_of_shapes[i].enemy == False and list_of_shapes[j].enemy == False:
              continue 
          if list_of_shapes[i].enemy == True and list_of_shapes[j].enemy == True:
              continue     
          if list_of_shapes[i].enemy == True or list_of_shapes[j].enemy == False:
                  color = 'black'
                  width = 80
                  height = 80
          if list_of_shapes[i].enemy == False or list_of_shapes[j].enemy == True:
                  color = 'black'
                  width = 80
                  height = 80
 
#Create the collision function. 
#Assign enemy with the first index in my list of shapes.   
def collide():
    enemy = list_of_shapes[0]
#Create an empty list for the remaining shapes the enemy collides with.
    if len(list_of_shapes) > 1:
        shape_remove = []
        for i in range(1, len(list_of_shapes)):
            shape = list_of_shapes[i]
            #Set collision equal to False to be able to use it later once the enemy collides.
            collide = False
            
            #p stands for point 
            p1_x = enemy.x
            p1_y = enemy.y
            p2_x = enemy.x + enemy.width
            p2_y = enemy.y 
            p3_x = enemy.x 
            p3_y = enemy.y + enemy.height
            p4_x = enemy.x + enemy.width
            p4_y = enemy.y + enemy.height
        
            #compare the coordinates of shape to ennemy to chack the collision.
            if p1_x > shape.x and p1_x < shape.x + shape.width and p1_y > shape.y and p1_y < shape.y + shape.height:
                collide = True
            
            if p2_x > shape.x and p2_x < shape.x + shape.width and p2_y > shape.y and p2_y < shape.y + shape.height:
                collide = True 
            
            if p3_x > shape.x and p3_x < shape.x + shape.width and p3_y > shape.y and p3_y < shape.y + shape.height:
                collide = True
            
            if p4_x > shape.x and p4_x < shape.x + shape.width and p4_y > shape.y and p4_y < shape.y + shape.height:
                collide = True
            
            if collide == True:
                shape_remove.append(shape)
        
        #Remove the eaten shapes completely.
        for shape in shape_remove:
            list_of_shapes.remove(shape)
    
#Create the set of colors for the shapes.        
colors = ['snow', 'blue violet', 'LavenderBlush3', 'gainsboro', 'floral white', 'sandy brown',
    'blue violet', 'antique white','medium aquamarine', 'blanched almond', 'cadet blue', 'peach puff',
    'light sea green', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender']

#Create a list of shapes to be able to use them later in the code.
diff_shapes = ['Oval', 'Circle', 'Rectangle', 'Square' ]

#Create an emepty list of shapes.
list_of_shapes = []

#Randomize the colors.
for i in range(10):
    for a in range(0,19):
        color = (random.sample(colors, 1)[0])
    
    #Randomize the width and height of my shapes.
    width = random.randint(25, 80)
    height = random.randint(30,80)
    
    #Enemy is number 0
    #set it equal to black
    #Make the enemy larger in the list of shapes so that when the collision happens, it touches the corners of all the other shapes.
    if i == 0:
        enemy = True
        color = 'black'
        width = 80
        height = 80
    else:
        enemy = False
        
    #Randomize the values for the x, y, and velocitities.
    x = random.randint(0, Frame_Width/2 - width)
    y = random.randint(0, Frame_Height/2 - height)
    velocity1 = random.randint(-10, 10)    
    velocity2 = random.randint(-5, 5)
    index_of_shape = random.randint(0,3)
    
    #Set index in three different shapes equal to a particular shape when randomized so that the values for both square and triangle are the same, with the same heigt and width.
    if diff_shapes[index_of_shape] == 'Circle' or diff_shapes[index_of_shape] == 'Square':
        width = height
    #Call the SHAPE class by assigning it to a variable called shape.
    shape = SHAPE(x, y, width, height, color, velocity1, velocity2, diff_shapes[index_of_shape], enemy)
    #Append to an empty list of shapes.
    list_of_shapes.append(shape)
    
#Call the remainig functions.
while True:
    canvas.delete('all')   
    for i in range(len(list_of_shapes)):
        list_of_shapes[i].move_item()
    collide()
    infection()
    canvas.update() 
    time.sleep(0.003)
