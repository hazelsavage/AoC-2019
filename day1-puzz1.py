# fuel_needed = int(module_mass/3) - 2

# puzzle answer = sum(fuel needed for each module)

#read a line of the file
#do the maths on it
#save the result somewhere
#add it onto the total

totalfuel = 0

file = open('day1-input.txt', 'r')

for line in file.readlines():
  mass = int(line)
  fuel = int(mass/3) - 2
  totalfuel += fuel

print("total fuel required is " + str(totalfuel))


