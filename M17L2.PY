# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
union = set1.union(set2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)

# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
union = set1.intersection(set2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)

def prob_a_or_b(a, b, all_possible_outcomes):
	# probability of event a
	prob_a = len(a)/len(all_possible_outcomes)

	# probability of event b
	prob_b = len(b)/len(all_possible_outcomes)

	# intersection of events a and b
	inter = a.intersection(b)

	# probability of intersection of events a and b
	prob_inter = len(inter)/len(all_possible_outcomes)

	# add return statement here
	return (prob_a + prob_b - prob_inter)
  

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function for final result
print('Probability of Getting an even number or a number greater than 2')
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))

