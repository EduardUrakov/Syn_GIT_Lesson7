import os

poets = [('Ptushkin', 1203, 1289), ('Cheburashkin', 1900, 1967), ('Piterski', 1750, 1820)]

print(poets)

poets[0] = ('Ptushkin', 1204, 1289) 
print(*poets)