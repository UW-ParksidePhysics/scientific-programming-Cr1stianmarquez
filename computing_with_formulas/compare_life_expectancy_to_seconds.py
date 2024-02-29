seconds_to_years= (1000000000/60/60/24/365)
print ("A Billion Seconds is", seconds_to_years, "Years")
cdc_life= 76.4
print ("CDC life expectancy in years is", seconds_to_years)
if seconds_to_years <= cdc_life:
  print (f'The Baby Is Expected To Live Longer Than A Billion Seconds')
else: 
  print (f'The Baby Is Expected To Live Shorter Than A Billion Seconds')
