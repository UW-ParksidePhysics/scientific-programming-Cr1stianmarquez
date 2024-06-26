from annotate_plot import annotate_plot
from plot_data_with_fit import plot_data_with_fit
from read_two_columns_text import read_two_columns_text
from calculate_quadratic_fit import compute_quadratic_coefficients
from calculate_bivariate_statistics import compute_bivariate_statistics
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from equations_of_state import fit_eos
from generate_matrix import generate_matrix
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from convert_units import convert_units


__author__ = 'Cristian Marquez'
#Divid File Name Step 1
def parse_file_name(file):
  parse = file.split(".")
  return parse[0], parse[1], parse[2]

# 3 Parse (Chem Symbol, Crystal, Symbol, and Acron) DIVID BY 2 HAs FD-3M
if __name__ == '__main__':
  display_graph = True
  filename = 'C.Fd-3m.GGA-PBEsol.volumes_energies.dat'
  chemical_symbol, crystal_symbol, acronym = parse_file_name(filename)
  #import data DOES NOT WORK KEEP GETTING MODULE ERROR 
  array = read_two_columns_text(filename) / 2

  #STEP 5 
  quad_coefficients_temp = compute_quadratic_coefficients(array)
  quadratic_coefficients = quad_coefficients_temp[::-1]

  eos_fit_curve, eos_parameters = fit_eos(array[0], array[1],     quadratic_coefficients, eos='murnaghan')
#UNITS CONVERTIONS
  converted_units = [convert_units(eos_parameters[0],   'rydberg/atom'),
                  convert_units(eos_parameters[1], 'rydberg/cubic bohr'),
                   eos_parameters[2], convert_units(eos_parameters[3], 'cubic bohr/atom')
                   ]

  data_array = np.array([convert_units(array[0], 'cubic bohr/atom'),
                       convert_units(array[1], 'rydberg/atom')])
#STEP 4 Bivariate Statistics
  statistics = compute_bivariate_statistics(data_array)
  min_x = statistics[2]
  max_x = statistics[3]
  min_y = statistics[4]
  max_y = statistics[5]
#STEP 8 Plot using ARRAY from above 
  fit_array = np.array([np.linspace(min_x, max_x, len(eos_fit_curve)),
                      convert_units(eos_fit_curve, 'rydberg/atom')])
  plot_miny = min(fit_array[1])
  plot_minx = min(fit_array[0])
  plot_maxy = max(fit_array[1])
  plot_maxx = max(fit_array[0])

#STEP 9 ANIMATE 
  annotations_chemical = {'string': f"{chemical_symbol}",
    'position': np.array([min_x - 0.3 * (max_x - min_x), max_y - .00005]),
    'alignment': ['left', 'center'], 'fontsize': 10}

  annotations_crystal = {
    'string': rf"${crystal_symbol[:2]}" + r"\overline{" + crystal_symbol[-2] + r"}" + crystal_symbol[-1] + r" $",
    'position': np.array([(max_x * 1.1 - min_x / 1.1) / 2 + min_x / 1.1, max_y - 0.005]),
    'alignment': ['center', 'center'], 'fontsize': 10}

  annotations_bulk = {'string': rf'$K_0= ${converted_units[1]:.1f} GPa',
    'position': np.array([(max_x * 1.1 - min_x / 1.1) / 2 + min_x / 1.1, max_y]),
    'alignment': ['center', 'center'], 'fontsize': 10}

  annotations_V0 = {'string': rf'$V_0$ = {converted_units[3]:.2f} $\AA^3/$atom',
    'position': np.array([converted_units[3] + (max_x - min_x) * .05, max_y - .14]),
    'alignment': ['left', 'bottom'], 'fontsize': 10}
# State name to refer {name} USE DATETIME Module
  name = 'Cristian Marquez'
  annotations_sign = {'string': f"Created by {name} {date.today().isoformat()}",
    'position': np.array([min_x - 0.3 * (max_x - min_x), min_y - 0.004]),
    'alignment': ['left', 'bottom'],
    'fontsize': 10}

  plt.figure(figsize=(10, 6))

  plot = (plot_data_with_fit(data_array, fit_array, data_format="o", fit_format=""))
  plt.xlim(min_x / 1.1, max_x * 1.1)
  plt.plot(np.linspace(converted_units[3], converted_units[3], 70),
  np.linspace(np.amin(fit_array[1]), (np.amin(fit_array[1]) + min_y * 1.00005 / 2)), 'k--')
  plt.ylim(min_y * 1.00002, max_y / 1.00002)
  plt.ylabel(r'$E$' + ' ' + r"[eV/atom]")
  plt.xlabel(r'$V$' + ' ' + r"[$\AA^3/$atom]")
  annotate_plot(annotations_chemical)
  annotate_plot(annotations_V0)
  annotate_plot(annotations_crystal)
  annotate_plot(annotations_bulk)
  annotate_plot(annotations_sign)
  plt.title(f'Murnaghan Equation of State for {chemical_symbol} in DFT {acronym}')

if display_graph: TRUE #MAKE FALSE TO GET PNG
    plt.show()
else:
    plt.savefig('Murnaghan.png')

# PART 2 VISUALIZE VECTORS IN SPACE
number_of_eigenvalues = 3
#(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter)
matrix = generate_matrix(-10, 10, 110, 'harmonic', 3)
eigenvalue, eigenvector = calculate_lowest_eigenvectors(matrix, number_of_eigenvalues)
eigenvalues = eigenvalue[:number_of_eigenvalues]
eigenvectors = eigenvector[:number_of_eigenvalues]
x = np.linspace(-10, 10, 110)
labels = []
for i in range(number_of_eigenvalues):
    labels.append(rf'$\psi_' + r'{' + rf'{i}' + r'},' + rf'E_{i} $ = {eigenvalue[i]:.3f}a.u.')
plt.figure(figsize=(12, 8))
for eigenvector in eigenvectors:
    plt.plot(x, eigenvector)
plt.xlabel(r'$x$ [a.u.]')
plt.ylabel(r'$\psi_n (x)$ [a.u.]')
plt.legend(labels=labels, loc='upper right')
plt.ylim(-2 * np.amax(eigenvectors), 2 * np.amax(eigenvectors))
plt.plot(x, np.linspace(0, 0, 110), color='black')
plt.title(f"Select Wavefuctions for a {'harmonic'} Potential\n"
          f"on a Spatial Grid of 110 Points")
name = 'Made By Cristian Marquez'
plt.annotate(f'Created by {name} {date.today().isoformat()}', (.02, .054), (-7.5, .25),
             xycoords='axes fraction', textcoords='offset points', va='top')

if display_graph:
    plt.show(): True
else:
    plt.savefig('Harmonic.png')
