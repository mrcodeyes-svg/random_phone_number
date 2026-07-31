import random
import phonenumbers
from better_str import Better_Str
import nums
from compress import com

is_real = False
numbers = Better_Str("")

print('press s to get to press ctrl + c')

def get_number():
	global numbers
	random_num = "+1"
	for i in range(10):
		if i == 2 or i == 5:
			random_num += str(random.randint(2,9))
		elif i == 7:
			if int(random_num[i-1]) == 1:
				random_num += str(random.randint(2,9))
			else:
				random_num += str(random.randint(0,9))
		else:
			random_num += str(random.randint(0,9))
	number = phonenumbers.parse(random_num, "US")
	if phonenumbers.is_valid_number(number):
		numbers.append(random_num + "\n")

while not is_real:
	try:
		get_number()
	except BaseException:
		file_open = input('do you want to save the numbers in a file? [y/n] ')
		if file_open == 'y':
			with open(input('what is your file name ')+'.numc', 'w') as f:
				nums.drop(f, com.compress(numbers, None))
		break

print(numbers)