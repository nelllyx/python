numbers = [2,3,4,5,7]

def square(num):

	sum_square_numbers = 0

	for index in num:

		sum_square_numbers = sum([index ** 2 for index in num])

		return sum_square_numbers

print(square(numbers))

			