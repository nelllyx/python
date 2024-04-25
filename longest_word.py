words = ['welcome','out','weather','mobile','breakfast','journey']



def length(string):

	word_check = ''

	for index in string:

		if len(index) > len(word_check):

			word_check = index

	string_check = len(word_check)

	return f"The longest word in the list is {word_check} and the length is {string_check}"

print(length(words))	

	
