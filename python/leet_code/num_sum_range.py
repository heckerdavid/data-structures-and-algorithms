def sum_digits(num_x, num_y):
	count = 0

	for i in range(1, num_x + 1):
		if adds_to_y(i, num_y):
			count += 1

	return count

def adds_to_y(number, num_y):
	if number == num_y:
		return True

	total = 0
	for num in str(number):
		total += int(num)

	if total == num_y:
		return True

	return False
