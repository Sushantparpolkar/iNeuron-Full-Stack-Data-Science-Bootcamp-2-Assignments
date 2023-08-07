#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Rectangle:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def rectangle_area(self):
        return self.width*self.height

class Circle:
    
    def __init__(self,radius):
        self.radius=radius
        
    def circle_area(self):
        return 3.142*self.radius**2


# In[ ]:




