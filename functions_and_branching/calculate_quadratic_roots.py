#Write a function for solving ax**2+bx+c=0.
import unittest
import numpy as np
import numpy.lib.scimath 

def calculate_quadratic_roots(a, b, c):
    """Calculate the roots of a quadratic equation."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("The roots are complex.")
    else:
        root1 = (-b + np.lib.scimath.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.lib.scimath.sqrt(discriminant)) / (2*a)
        print("Roots:", root1, root2)

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))
calculate_quadratic_roots(a, b, c)



def test_single_root():
    a, b, c = 1, -2, 1
    expected_roots = (1.0, None)
    roots = calculate_quadratic_roots(a, b, c)
    assert roots == expected_roots, f"Test failed for coefficients {a}, {b}, {c}. Expected {expected_roots}, but got {roots}."
  
test_single_root()

def test_roots_float():
  a, b, c = 1, -3, 2
  expected_roots = (2.0, 1.0)
  roots = calculate_quadratic_roots(a, b, c)
  assert roots == expected_roots, f"Test failed for coefficients {a}, {b}, {c}. Expected {expected_roots}, but got {roots}."

def test_roots_complex():
  a, b, c = 1, 2, 5
  roots = calculate_quadratic_roots(a, b, c)
  assert roots == (None, None), f"Test failed for coefficients {a}, {b}, {c}. Expected ({None}, {None}), but got {roots}."

def run_tests():
  print("Running tests...")
  test_single_root()
  test_roots_float()
  test_roots_complex()
  print("All tests passed!")

if __name__ == '__main__':
    run_tests()