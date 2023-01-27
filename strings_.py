
def common_longest_string():

	str1 = input('enter a str1: ')
	str2 = input('enter a str2: ')

	if str1 == str2:
		print(f'the longest common substring is: {str1}')
	elif str1 in str2:
		print(f'the longest common substring is: {str1}')
	elif str2 in str1:
		print(f'the longest common substring is: {str2}')
	

common_longest_string()