#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:24:16 2022

@author: spencerjordan
"""

import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp
from tqdm import tqdm
from numba import jit

its = int(1e6)
mp.dps = its

class Turtle():
    def __init__(self, base):
        self.base = base
        self.increment = np.pi*2/base
        self.pos_x = 0
        self.pos_y = 0
    
    def move(self,frac):
        self.x_old = self.pos_x
        self.y_old = self.pos_y
        angle = frac*self.increment
        self.pos_x += np.sin(angle)
        self.pos_y += np.cos(angle)
        
turtle = Turtle(base=10) 
pi = str(mp.pi)[2:]

print(np.pi)
#with plt.xkcd():
    
plt.figure(dpi=500)
plt.subplots()
plt.title('Turtle')

#for a in [1,2,3,4,5,6,7,8,9,10]:
@jit
def go_fast(nopython=True):
    for i in tqdm( range(its-3) ):
        
        a = int(pi[i])
        turtle.move(a)
        
        #with plt.xkcd():
        #    plt.plot([turtle.x_old,turtle.pos_x],[turtle.y_old,turtle.pos_y],
        #         linewidth=1.5,alpha=0.75)
    
     
        #plt.show()
        #plt.savefig('turtle_big.png',dpi=500)
    
go_fast() 
    

 