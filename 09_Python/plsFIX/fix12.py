'''
The output should be:
4
16129
'''
def square(x):
	return x**2

nr = square(2)
print(nr)

foo = 127 # De plaatsing van de variable foo is aangepast zodat de big variable vastgesteld kan worden. 
big = square(foo)
print(big)

