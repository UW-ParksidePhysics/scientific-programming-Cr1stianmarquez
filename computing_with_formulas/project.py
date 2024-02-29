### coffee_cooling_Euler ###
# first-order differential equations by Euler method
from numpy import linspace, array, zeros, ones, arange, sqrt, sin, cos, pi, exp, log
import matplotlib.pyplot as mp
x=0.0
y=2.0
dx=0.1 # step size
xpoints=[]
ypoints=[]
xpoints.append(x)
ypoints.append(y)
def f(x,y):
    f=1-y # derivative dy/dx
    return f
while x<=5:
    y=y+f(x,y)*dx
    x=x+dx
    xpoints.append(x)
    ypoints.append(y)
mp.plot (xpoints,ypoints)
def ff(x):
    ff=1+exp(-x) # analytical solution from Eq.5 in lecture notes
    return ff
x = linspace(0,5,100)
print (x)
mp.plot()
mp.plot(x,ff(x))
mp.show()
### coffee_