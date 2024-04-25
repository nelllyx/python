numbers = [8,4,9,2,5,7,3]



def minimum(min):

	min_number = min[0]
	
	for index in min:

		if  index < min_number:
		
			min_number = index

			return f"The minimum number is {min_number}"

print(minimum(numbers))
	