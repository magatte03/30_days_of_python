# Importer un module
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) 

#Importer des fonctions à partir d'un module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])