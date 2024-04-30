### My project is based on Newtons Law of Cooling. It compares my experimental value of the coefficent of cooling with the actual value for 16 oz of water at room temperature (28.6 degrees Celsius) at an inital temperature of 81 degrees celsius. I thought of this project due to issues I face when heating my coffee in the morning and having to drink it cold because of my schedule. This program is designed to plot my experimental data as well as show it in a table and state all conditions. The graph plots my data from the experiment and gives a regression line. Now I will be able to determine when to heat up my coffee and how hot it should be to be luke warm when I drink it.

import math
import matplotlib.pyplot as plt
import numpy as np

def k_estimate(initial_temperature, environment_temperature, median_temperature, time_of_experiment):
    return -(1 / time_of_experiment) * np.log(5.84 / 52.4)

if __name__ == "__main__":
    environment_temperature = 28.6  # ambient temperature (78 deg F)
    initial_temperature = 81.0  # initial water temperature (177.8 deg F)
    median_temperature = 50  # Median Water Temp From Data
    time_of_experiment = 60  # Time of y(t)
    actual_cooling_constant = 0.056  # Actual Coefficient of Cooling

    time = [0, .08, .16, .25, .30, .41, .50, .58, .60, .75, .83, .91, 1]
    temperature = [66.67, 60.56, 55.00, 52.22, 51.1, 47.22, 44.44, 41.11, 40.00, 38.88, 36.66, 35.55, 34.44]

    k_estimate_result = k_estimate(initial_temperature, environment_temperature, median_temperature, time_of_experiment)
    percent_error = abs((actual_cooling_constant - k_estimate_result) / actual_cooling_constant) * 100

    print('K Estimate from our experiment is:', k_estimate_result)
    print("\n" * 1)
    print(f'The initial temperature of the water is: {initial_temperature} degrees Celsius')
    print("\n" * 1)
    print(f'The final temperature of the water is: {median_temperature} degrees Celsius')
    print("\n" * 1)
    print(f'The ambient temperature is: {environment_temperature} degrees Celsius')
    print("\n" * 1)
    print("Time (hours)\tTemperature (°C)")  # Inserts Table with my experiment data
    for time_of_experiment, environment_temperature in zip(time, temperature):
        print(f"{time_of_experiment:^14}{environment_temperature:^14}")

    print("The actual Cooling Coefficient (k) for water with similar temperatures is:", actual_cooling_constant)
    print("The percent error is:", f'{percent_error:.1f}', "%")

    m, b = np.polyfit(time, temperature, 1)
    coef = np.polyfit(time, temperature, 1)
    poly1d_fn = np.poly1d(coef)
    plt.plot(time, temperature, 'yo', time, poly1d_fn(time), '--k')

    # Plot the data and the regression line
    plt.scatter(time, temperature, label='Data')

    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Newton\'s Law of Cooling')

    plt.legend()
    plt.grid(True)
    plt.show()
