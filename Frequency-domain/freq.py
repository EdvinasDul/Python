# Created by Edvinas Dulskas 19040186

import inspect
import matplotlib.pyplot as plt

# ------------ Functions -------------
def char_freq(string):

	chars = {}
	for s in string:
		if s in chars.keys():
			chars[s] += 1
		else:
			chars[s] = 1

	return chars

def char_freq_file(file):

	fd = open(file, 'r') # opens a file for reading
	data = fd.read() # reads data    
	# print("\nData from file: ", data)
	freq = char_freq(data)

	return freq

def histogram(dict_freq):

	plt.bar(list(dict_freq.keys()), dict_freq.values(), 0.05, color='g')
	plt.grid(True)
	plt.show()

	return

# ----------- Main code ----------------

str_freq = char_freq('aaabbbccc')
file_freq = char_freq_file('data.txt')

print(str_freq)
print(file_freq)
histogram(file_freq)
