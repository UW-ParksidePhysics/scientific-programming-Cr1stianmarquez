#Make a program where you define the distance to your current living place from campus given in kilometers (use Google Maps Links to an external site. or similar tool) and then compute and write out the corresponding length measured in inches, in feet, in yards, and in miles. Use that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one mile is 1760 yards. For verification, make the same calculation for a length of 0.640 kilometers in your code and show that it corresponds to 25196.85 inches, 2099.74 feet, 699.91 yards, or 0.3977 miles. Filename: convert_length.py.

distance = 7.4  #km
cm = distance * 100_000
inches = cm / 2.54
feet = inches / 12
yards = feet / 3
miles = yards / 1760
print(f'Distance in km: {distance}')
print(f'Distance in cm: {cm}')
print(f'Distance in inches: {inches}')
print(f'Distance in feet: {feet}')
print(f'Distance in yards: {yards}')
print(f'Distance in miles: {miles}')
print()

distance = 0.64
cm = distance * 100_000
inches = cm / 2.54
feet = inches / 12
yards = feet / 3
miles = yards / 1760
print(f'Distance in km: {distance}')
print(f'Distance in cm: {cm}')
print(f'Distance in inches: {inches}')
print(f'Distance in feet: {feet}')
print(f'Distance in yards: {yards}')
print(f'Distance in miles: {miles}')
     