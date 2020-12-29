""" Bit manipulation functions

	1. COnvert 0.72 to its binary representation in 32 bits.
	float_number_from_0_to_1_convert_to_binary_str(number, 32)
	
	

"""


def float_number_from_0_to_1_convert_to_binary_str(float_number, number_of_bits):
	lsb = pow(2, -number_of_bits)
	
	number_in_bits = number / lsb
	
	# to check, if number cannot be 
	# represented by only bits
	# if number_in_bits % 1 != 0:
		#print("ERROR")
		
	array_of_bits = []
	
	while number_in_bits > 0:
		remained = int(number_in_bits % 2)
		number_in_bits //= 2
		array_of_bits.append(str(remained))
		
	array_of_bits = list(reversed(array_of_bits))
	return ''.join(array_of_bits)