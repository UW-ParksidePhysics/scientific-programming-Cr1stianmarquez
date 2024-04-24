Web VPython 3.2
import vpython as vp

# Define initial position and velocity for the first ball
initial_position = vp.vector(-1., 0., 0.)
initial_velocity = vp.vector(1., 3., 0.)
ball1 = vp.sphere(pos=initial_position, radius=0.1, color=vp.color.red, make_trail=True)

# Define initial position and velocity for the second ball
initial_position1 = vp.vector(-2., 0., 0.)
initial_velocity1 = vp.vector(3., 0., 0.)
ball2 = vp.sphere(pos=initial_position1, radius=0.1, color=vp.color.blue, make_trail=True)

# Animation parameters
animation_time_step = 0.1  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.05
stop_time = 10.

# Main loop
time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    
    # Update position of the first ball
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball1.pos = vp.vector(x, y, z)
    
    # Update position of the second ball
    x1 = initial_position1.x + initial_velocity1.x * time
    y1 = initial_position1.y + initial_velocity1.y * time
    z1 = initial_position1.z + initial_velocity1.z * time
    ball2.pos = vp.vector(x1, y1, z1)
    
    time += time_step
