#!/usr/bin/python3
#5-no_c.py

def no_c(my_string):
	"""function that removes all characters c and C from a string."""
	new_string = ""
	for item in my_string:
		if item == "c" or item == "C":
			continue
		new_string += item
	return new_string

