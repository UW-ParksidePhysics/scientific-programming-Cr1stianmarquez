Web VPython 3.2
import vpython as vp

# Constants
G_EARTH = -9.81  # m/s^2
G_MARS = -3.71   # m/s^2
G_MOON = -1.625  # m/s^2

def calculate_range_time_of_flight(v0, theta, g):
    """Calculate range and time of flight."""
    t_flight = (2 * v0 * vp.sin(theta)) / abs(g)
    R = (v0 ** 2 * vp.sin(2 * theta)) / abs(g)
    return R, t_flight

def simulate_projectile_motion(v0, theta, g):
    """Simulate projectile motion."""
    scene = vp.canvas(background=vp.color.white)
    
    field_color = vp.vector(0, 1, 0) if g == G_EARTH else \
                  vp.vector(1, 0, 0) if g == G_MARS else \
                  vp.vector(0.5, 0.5, 0.5)
    field = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(20, 0.1, 20), color=field_color)
    
    ball_color = vp.vector(0, 0, 1) if g == G_EARTH else \
                 vp.vector(1, 0.5, 0.5) if g == G_MARS else \
                 vp.vector(1, 1, 1)
    ball = vp.sphere(pos=vp.vector(-10, 0, -10), radius=0.5, color=ball_color, make_trail=True)
    
    R, t_flight = calculate_range_time_of_flight(v0, vp.radians(theta), g)
    
    t = 0
    while t < t_flight:
        vp.rate(100)
        x = v0 * vp.cos(vp.radians(theta)) * t
        y = v0 * vp.sin(vp.radians(theta)) * t + 0.5 * g * t ** 2
        ball.pos = vp.vector(-10 + x, y, -10)
        t += 0.01
    
# Launch balls with different gravitational accelerations
simulate_projectile_motion(10, 30, G_EARTH)
simulate_projectile_motion(10, 30, G_MARS)
simulate_projectile_motion(10, 30, G_MOON)
