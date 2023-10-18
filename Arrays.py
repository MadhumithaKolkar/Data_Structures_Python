expenses = [2200,2350,2600,2130,2190]

print(expenses[1]-expenses[0])
print(expenses[0]+expenses[1]+expenses[2])
print("Did I spend 2000?", 2000 in expenses)
expenses.append(1980)
print(expenses)
expenses[3] = expenses[3]-200
print("April expense is now :", expenses[3])

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('Black Panther')
heros.remove('Black Panther')
heros.insert(3,'Black Panther')
heros[1:3] = ['Doctor Strange']
heros.sort()
print(heros)