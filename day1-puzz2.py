"""extra fuel required to cover the mass of the fuel

uses the same formula: fuel_needed = int(module_mass/3) - 2
but needs to be recursive until we've added enough fuel to carry all the fuel we've added

mass that needs negative fuel is treated as though it requires 0 fuel

for each module mass, calculate its fuel and add it to the total.
Then, treat the fuel amount you just calculated as the input mass
and repeat the process, continuing until a fuel requirement is zero or negative. 

we need a 'while' loop

we only need to add results that are >= 0 to the module total

we need to stop the loop when we get to 0 or below

puzzle answer = sum(fuel needed for each module)

"""


totalfuel = 0
modulefuel = 0

file = open('day1-input.txt', 'r')

for line in file.readlines():
  mass = int(line)
  modulefuel = 0
  
  while mass > 0:
    fuel = int(mass/3) - 2
    if fuel > 0:
      modulefuel += fuel
    mass = fuel
    
  totalfuel += modulefuel


print("total fuel required is " + str(totalfuel))

