#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
	"""Prints all integers in my_list in reverse order"""
	if my_list:
		my_list.reverse()
		for element in my_list:
			print("{:d}".format(element))
