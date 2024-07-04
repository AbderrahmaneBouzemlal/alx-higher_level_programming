#!/usr/bin/python3
"""This module have only one function find_peak"""

def find_peak(list_int):
	"""returns the biggest number"""
	maxi = 0
	if len(list_int) == 0:
		return None

	for i in list_int:
		dif = maxi - i
		if dif > 0:
			maxi = i
		else:
			continue
	return maxi
