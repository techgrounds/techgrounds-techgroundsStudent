'''
The output should be:
['Dog', 'Cat', 'Fly']
'''
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
	#short_names = [] voorgaande in deze zin saboteert de boel. Dus de hele zin is nu een comment. 

print(short_names)