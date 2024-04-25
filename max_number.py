numbers = [8,4,9,2,5,7,3]



def maximum(max):

	max_number = max[0]
	
	for index in max:

		if index > max_number:
		
			max_number = index

			return max_number

print(maximum(numbers))
	