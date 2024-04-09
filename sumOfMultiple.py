sum = 0;

for number in range(1,20001):
	if number % 10 == 0:
		sum+= number
print(f"The sum of multiple is {sum:,}")