# p = density of the air
# v = velocity of the object
# A = cross-sectional area (normal to the velocity direction)
# C_d = drag coefficient
# m = mass
# a = radius
from math import pi

air_density = 1.2 # kg/m^3
radius = 11 # cm
cross_area = pi * 0.11**2 # m^2
ball_mass = 0.43 # kg
gravity = 9.8 # m/s^2
drag_coefficient = 0.2
soft_kick_velocity = 2.78 # m/s
hard_kick_velocity = 33.3 # m/s

drag_force_1 = 0.5 * drag_coefficient * air_density * cross_area * soft_kick_velocity**2
print(drag_force_1)

drag_force_2 = 0.5 * drag_coefficient * air_density * cross_area * hard_kick_velocity**2
print(drag_force_2)

gravitational_force = ball_mass * gravity
print(gravitational_force)

print(f" Drag force 1: The drag force of a soft kick is {drag_force_1:.3f} Newtons.")

print(f" Drag force 2: The drag force of a hard kick is {drag_force_2:.1f} Newtons.")

print(f" Gravitational force: The gravitational force of the ball is {gravitational_force:.1f} Newtons.")