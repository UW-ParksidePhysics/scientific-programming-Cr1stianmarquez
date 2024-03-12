#For Initial Velocity of 10m/s:
#Planet = Europa = .134g of Earth g
import numpy as np
from numpy import linspace
import math
g = .134
v0 = 10
def ForLoop(v0):
  t = linspace(0, 2*v0/g,20)
  y = v0*t - 1/2*g*t*t
  print("%-20s%s"%("Time(t)","y(t)"))
  for i in range(len(t)):
    print("%-20.2f%.2f"%(t[i],y[i]))

def WhileLoop(v0):
  t = linspace(0, 2*v0/g,20)
  y = v0*t - 1/2*g*t*t
  print("%-20s%s"%("Time(t)","y(t)"))
  i=0
  while i <len(t):
    print("%-20.2f%.2f"%(t[i],y[i]))
    i+=1;

  if __name__ == '__main__':
    print("For loop")
ForLoop(v0)
print("While loop")
WhileLoop(v0)