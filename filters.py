# Date: 16-02-2015
# Name: Marten Folkertsma
'''
This is a helper file with filter codes for appartement scraper.py
'''

def word_filter(words, appartements_list):
	'''
	words is a list of words to filter everythin on.
	appartement_list: ['Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huur']
	'''
	output = []
	index = 0
	for appartement in appartements_list:
		for data in appart:
			if word not in data:
				output.append(appartements_list[index])
		index += 1

	return output

def size_filter(min_size, appartements_list):  #2 4
	'''

	appartement_list: ['Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huur']
	'''
	if size < min_size:
		return True
	return False 

def 
