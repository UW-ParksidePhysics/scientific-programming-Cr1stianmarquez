#The density of a substance is defined as ρ = m/V , where m is the mass of a volume V . Compute and print out the mass of one liter of each of the following substances whose densities in g/cm3: iron, air, gasoline, ice, the human body, silver, and platinum. For the elements and air, use the values in this table on the Wikipedia Links to an external site.. For the human body, use the value from this article's abstract Links to an external site.. For gasoline, use the European standard reference value of 0.755 g/cm3. Filename: calculate_liter_mass.py.
V = 1000 # mL
 # m = p * V
density_of_iron = 7870
mass_of_iron = 7870 * V
print(f'Mass of One Liter of Iron is {mass_of_iron}g/cm^3')

density_of_air = 1.2
mass_of_air = 1.2 * V
print(f'Mass of One Liter of Air is {mass_of_air}g/cm^3')

density_of_gasoline = 0.755 # g/cm^3
mass_of_gasoline = 0.755 * V
print(f'Mass of One Liter of Gasoline is {mass_of_gasoline}g/cm^3')

density_of_ice = 916.7
mass_of_ice = 916.7 * V
print(f'Mass of One Liter of Ice is {mass_of_ice}g/cm^3')

density_of_the_human_body = 0.86
mass_of_the_human_body = 0.86 * V
print(f'Mass of One Liter of the Human Body is {mass_of_the_human_body}g/cm^3')

density_of_silver = 10500
mass_of_silver = 10500 * V
print(f'Mass of One Liter of Silver is {mass_of_silver}g/cm^3')

density_of_platinum = 21450
mass_of_platinum = 21450 * V
print(f'Mass of One Liter of Platinum is {mass_of_platinum}g/cm^3')
