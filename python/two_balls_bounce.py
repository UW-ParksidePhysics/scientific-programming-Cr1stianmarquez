Web VPython 3.2
import vpython as vp

# Define initial positions and velocities for the balls
initial_position_bottom = vp.vector(-10., -4.75, 0.)
initial_velocity_bottom = vp.vector(25., 10., 0.)
initial_position_top = vp.vector(-10., 4.75, 0.)
initial_velocity_top = vp.vector(25., -10., 0.)

# Create bottom and top balls
ball_bottom = vp.sphere(pos=initial_position_bottom, radius=0.5, color=vp.color.blue, make_trail=True)
ball_top = vp.sphere(pos=initial_position_top, radius=0.5, color=vp.color.green, make_trail=True)

# Create wall
wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

# Animation parameters
animation_time_step = 0.01 
rate_of_animation = 1 / animation_time_step
time_step = 0.005
stop_time = 1.
time = 0.

# Main loop
while time < stop_time:
    vp.rate(rate_of_animation)
    
    # Update position of bottom ball
    if (ball_bottom.pos.x + ball_bottom.radius) >= (wall.pos.x - 0.5 * wall_dimensions.x):
        initial_velocity_bottom.x = -initial_velocity_bottom.x 
    ball_bottom.pos.x += initial_velocity_bottom.x * time_step
    ball_bottom.pos.y += initial_velocity_bottom.y * time_step
    ball_bottom.pos.z += initial_velocity_bottom.z * time_step
    
    # Update position of top ball
    if (ball_top.pos.x + ball_top.radius) >= (wall.pos.x - 0.5 * wall_dimensions.x):
        initial_velocity_top.x = -initial_velocity_top.x  
    ball_top.pos.x += initial_velocity_top.x * time_step
    ball_top.pos.y += initial_velocity_top.y * time_step
    ball_top.pos.z += initial_velocity_top.z * time_step
    
    time += time_step
