import random
import math
from numpy.random import choice

# fitness function: ackley function
def ackley(x1, x2):
	dis = -(0.2 * (math.sqrt(0.5 * (x1**2 + x2**2))))
	dat = 0.5 * (math.cos(math.pi * 2 * x1) + math.cos(math.pi * 2 * x2))
	result  = round(20 + math.exp(1) - (20 * math.exp(dis)) - math.exp(dat),2)

	return result

# inisialization
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
donor_vector = []
trial_vector = []

for i in range(population):
	population_list.append([round(random.uniform(lower_bound, upper_bound), 2), round(random.uniform(lower_bound, upper_bound), 2)])

# every element in population undergoes mutation, recombination, and selection
for i in range(population):
	print(population_list)
	# mutation
	cois = []	
	self_val = population_list[i]

	# assign r1, r2, r3
	my_list = [x for x in population_list if x not in cois and x != self_val]
	r1 =  random.choice(my_list)
	cois.append(r1)
	my_list = [x for x in population_list if x not in cois and x != self_val]
	r2 =  random.choice(my_list)
	cois.append(r2)	
	my_list = [x for x in population_list if x not in cois and x != self_val]
	r3 =  random.choice(my_list)
	cois.append(r3)
	my_list = [x for x in population_list if x not in cois and x != self_val]

	# calculate donor vector
	donor_vector.append([round(r1[0] + (0.5 *(r2[0] - r3[0])),2), round(r1[1] + (0.5 *(r2[1] - r3[1])),2)]) # mutation factor(F) is 0.5

	# recombination
	# calculate trial vector
	
	trial_vector_cois = choice(["donor_vector", "target_vector"], 1, 0.1) # CR is 0.1
	if trial_vector_cois == "donor_vector":
		trial_vector.append(donor_vector[i])
	else:
		trial_vector.append(population_list[i])

	# selection
	target_val = ackley(population_list[i][0], population_list[i][1])
	trial_val = ackley(trial_vector[i][0], trial_vector[i][0])

	if trial_val <= target_val:
		population_list[i] = trial_vector[i]
