#For Initial Velocity of 10m/s:
#Planet = Europa = .134g of Earth g
#gravity = 1.31 # m/s^2
def projectile_position(initial_velocity, time, gravity):
y(t) = v0*t - .5*g*t^2
#For Initial Velocity of 10m/s:
v0 = 10 #m/s
g = 1.31 #m/s^2
time_range = (0,n+1)
for time in time_range:
position_t = projectile_position(v0, time, g)
print 'time_range  position_t'