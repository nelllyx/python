pass_mark = 0

fail_mark = 0

for number in range (1,16):
	
	scores = int(input('Enter score for student ' + str(number) + ': ' ))
		
	if scores >= 45:
		
		pass_mark += 1

	else:
	
		fail_mark += 1


print(str(pass_mark) + ' student passed the test')


print(str(fail_mark) + ' student failed the test. Better luck next time!!')