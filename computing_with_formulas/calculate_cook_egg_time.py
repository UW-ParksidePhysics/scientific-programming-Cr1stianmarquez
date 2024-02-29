#Egg White above 63
#Yolk above 70
#Soft above 63
#Soft Yolk Not above 70
#Hard Yolk allowed to reach 70
#m,p,c, and K properties of egg
#m=mass
#p=density
#c=specific heat
#K=thermal conductivity
#m=47g small
#m=67g Large
#Tw= boiling water temp (C)
#To= Original temp of egg
import math
m_small = 47  # g
m_large = 67  # g
p = 1.038  # g/cm^3
c = 3.7  # J/(gK)
k = 0.0054  # W/(cm K)
tw = 100  # c boiling water temp
ty = 70  # c temperature of center of egg
to = 4  # c fridge temp
to2 = 20  # c outside temp

t_smal_fridge = (((m_small ** 0.66) * c * (p ** 0.33)) / k * (math.pi ** 2) * ((4 * math.pi / 3) ** 0.66)) 
t_small_fridge= (t_smal_fridge * (math.log(0.76 * (to - tw) / (ty - tw)))/60)
t_small_room= (t_smal_fridge * (math.log(0.76 * (to2 - tw) / (ty - tw)))/60)
t_larg_fridge = (((m_large ** 0.66) * c * (p ** 0.33)) / k * (math.pi ** 2) * ((4 * math.pi / 3) ** 0.66))
t_large_fridge= (t_larg_fridge * (math.log(0.76 * (to - tw) / (ty - tw)))/60)
t_large_room= (t_larg_fridge * (math.log(0.76 * (to2 - tw) / (ty - tw)))/60)

print(f' Cooking Time For A Small Egg in Fridge Temperatures: {t_small_fridge:.2f} minutes')
print(f' Cooking Time For A Small Egg at Room Temperature: {t_small_room:.2f} minutes')
print(f' Cooking Time For A Large Egg at Fridge Temperatures: {t_large_fridge:.2f} minutes')
print(f' Cooking Time For A Large Egg at Room Temperature: {t_large_room:.2f} minutes')

