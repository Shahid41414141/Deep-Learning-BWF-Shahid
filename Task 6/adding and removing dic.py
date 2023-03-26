# Adding values in dictionary

# Create an empty dictionary
my_dict = {}

# Add a new key-value pair using assignment
my_dict['apple'] = 1
print(my_dict)  

# Add multiple key-value pairs using the update() method
my_dict.update({'banana': 2, 'cherry': 3})
print(my_dict)  

# Remoiving values in dictionary
# Remove a specific key-value pair using del
del my_dict['banana']
print(my_dict)  

# Remove a specific key-value pair using pop()
value = my_dict.pop('cherry')
print(my_dict)  
print(value)  

# Remove all key-value pairs using clear()
my_dict.clear()
print(my_dict)  
