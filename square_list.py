numbers = [2,3,4,5,7]

def square(num):

	for index in num:

		sum = [index ** 2 for index in num]

		return sum

print(square(numbers))

			