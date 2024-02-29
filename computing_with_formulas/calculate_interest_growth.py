#Let p be a bank’s interest rate in percent per year. An initial amount A has then grown to. after n years. Make a program for computing to what amount $1000 has grown after three years with an interest rate at the US government securities nominal 3-year rate Links to an external site. for today (be sure to put the date you pulled the interest rate for in a comment) and have the program print out the initial amount, the interest rate, and the the growth amount. Filename: calculate_interest_growth.py.
A = 1000 #initial investment
n = 3 #number of years
p = 4.36 #Feburary 15th 2024
banks_intrest_equation = A * (1 + p/100)**n
print (f'Initial Amount: {A}')
print (f'Interest Rate: {p}%')
print (f'Growth Amount: {banks_intrest_equation}')