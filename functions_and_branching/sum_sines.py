n = 10
counter = 0  # Initialize counter outside of the loop
for nx in range(1, n+1):
    for ny in range(1, n+1):
        for nz in range(1, n+1):
            sum_val = nx**2 + ny**2 + nz**2
            print(nx, ny, nz, '  ', sum_val)

            if sum_val == 230:
                counter = counter + 1

print('degree=', counter)  # Print the count after all combinations are checked