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
lower_bound = -5.5
upper_bound = 5.5
hehe = True
population_list = []
my_list = []
count = 0
iteration = 5

# input error handling
while hehe: 
	population = int(input("Input the number of initial population: "))
	if population >= 4:
		hehe = False
	else:
		print("ERROR: Population must be at least 4!\n")
		
iteration = int(input("Input the number of iteration: "))

# generate random population
for i in range(population):
	population_list.append([round(random.uniform(lower_bound, upper_bound), 2), round(random.uniform(lower_bound, upper_bound), 2)])
print("Initial: ", population_list)

# action
while count < iteration:
	donor_vector = []
	trial_vector = []
	# every element in population undergoes mutation, recombination, and selection
	for i in range(population):
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
		trial_vector_cois = choice(["donor_vector", "target_vector"], 1, 0.7) # CR is 0.7		
		# print(trial_vector_cois)
		if trial_vector_cois == "donor_vector":
			trial_vector.append(donor_vector[i])
		else:
			trial_vector.append(population_list[i])

		# selection
		target_val = ackley(population_list[i][0], population_list[i][1])
		trial_val = ackley(trial_vector[i][0], trial_vector[i][0])

		if trial_val <= target_val:
			population_list[i] = trial_vector[i]
		# print(population_list)

	print("Generation ",count+1,":",population_list)
	count += 1
