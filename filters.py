# Date: 16-02-2015
# Name: Marten Folkertsma
'''
This is a helper file with filter codes for appartement scraper.py
'''
import re

def word_filter(words_list, appartement_list):
	'''
	words_list is a list of words to filter everythin on.
	appartement_list is a list of data sorted like this: ['Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link']
	'''
	output = []
	index = 0
	for appartement in appartement_list:
		add_appartement = True
		
		for data in appartement:
			for word in words_list:
				if word in data:
					add_appartement = False
		
		if add_appartement:
			output.append(appartement_list[index])
		
		index += 1

	return output

def size_filter(min_size, appartement_list):  #2 4
	'''
	min_size is the minimum square meters of the house
	appartement_list is a list of data sorted like this: ['Straat', 'Soort', 'Kamers', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link']
	'''
	output = []
	index = 0
	for appartement in appartement_list:
		try:
			size_int = int(re.findall('\d+', appartement[3])[0])
		except Exception as inst:
			print type(inst)
			print inst
			output.append(appartement_list[index])
			continue
		if size_int >= min_size:
			output.append(appartement_list[index])
		index += 1
	return output

def room_filter(min_rooms, appartement_list):  #2 4
	'''
	appartement_list is a list of data sorted like this: ['Straat', 'Soort', 'Kamers', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link']
	'''
	output = []
	index = 0
	for appartement in appartement_list:
		try:
			size_int = int(re.findall('\d+', appartement[2])[0])
		except Exception as inst:
			print type(inst)
			print inst
			output.append(appartement_list[index])
			continue
		if size_int >= min_rooms:
			output.append(appartement_list[index])
		index += 1
	return output

# test function foor the codes
if __name__ == '__main__':
	appartement1 = ['Straat', 'Soort', '4', '60m', 'Makelaar', 'Huurprijs', 'Link']
	appartement2 = ['Straat', 'Soort', '2', '70m', 'Makelaar', 'Huurprijs', 'Link']
	appartement3 = ['Straat']
	appartement_list = [appartement1, appartement2, appartement3]
	word_list = ['job']
	print word_filter(word_list, appartement_list)
	print size_filter(65, appartement_list)
	print room_filter(3, appartement_list)