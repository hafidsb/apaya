import random

# inisialisation
lower_bound = 1
upper_bound = 100
hehe = True

while hehe: 
	population = int(input("Input the number of initial population: "))
	if population >= 4:
		hehe = False
	else:
		print("ERROR: Population must be at least 4!\n")

population_list = []
my_list = []
choice = []
donor_vector = [[]]
trial_vector = [[]]

for i in range(population):
	population_list.append(round(random.uniform(lower_bound, upper_bound), 2))

# mutation
for i in range(1):
	# assign r1, r2, r3
	my_list = [x for x in population_list if x not in choice]
	del my_list[i]
	r1 =  random.choice(my_list)
	choice.append(r1)
	my_list = [x for x in population_list if x not in choice]
	del my_list[i]
	r2 =  random.choice(my_list)
	choice.append(r2)
	my_list = [x for x in population_list if x not in choice]
	del my_list[i]
	r3 =  random.choice(my_list)
	choice.append(r3)
	my_list = [x for x in population_list if x not in choice]
	del my_list[i]

	# calculate donor vector
	donor_vector[i] = round(r1 + (0.8 *(r2 - r3)),2) # mutation factor is 0.8

	# calculate trial vector