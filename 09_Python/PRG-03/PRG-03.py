#Inject the code given to us from theGrounds
a = 'int'
b = 7
c = False
d = "18.5"
#Determine the data types of all four variables (a, b, c, d) using a built in function.
type_a = type(a)
type_b = type(b)
type_c = type(c)
type_d = type(d)
# Print the data types
print("Data type van 'a':", type_a)
print("Data type van 'b':", type_b)
print("Data type van 'c':", type_c)
print("Data type van 'd':", type_d)
#Make a new variable x and give it the value b + d. Print the value of x. This will raise an error. Fix it so that print(x) prints a float.
x = b + float(d) 
print(x)



