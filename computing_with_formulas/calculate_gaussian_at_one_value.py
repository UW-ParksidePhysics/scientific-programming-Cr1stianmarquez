from math import sqrt, pi, exp

mean = m = 0
standard_deviation = s = 2
input_value = x = 1
gaussian_function = (1 / sqrt(2 * pi)) * exp((-1 / 2) * ((input_value - mean) / standard_deviation) ** 2)
print(f"Gaussian function value = {gaussian_function}")
print(f" Mean: {mean}")
print(f" Standard deviation: {standard_deviation}")
print(f" Input value: {input_value}")