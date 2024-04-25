user_input = input('Enter a word ')

number = int(input("Enter a number "))

def string (word, numb):

	mult = word * numb

	if isinstance(numb,float): 

		return word 

	else: return mult 

print(string(user_input,number))



