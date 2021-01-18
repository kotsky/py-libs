"""Custom transformation

1. string_to_array_and_k(str) -> list(int), int
Example:
	string = '[10, 20, 30], 2' => array = [10, 20, 30] and k = 2


"""



def string_to_array_and_k(given_string):
    sl = len(given_string)
    array_string = given_string[1:sl-4]
    array_string_v2 = array_string.split(', ')
    k_string = given_string[sl-1:sl]
    array = list(map(int, array_string_v2))
    return array, int(k_string)

