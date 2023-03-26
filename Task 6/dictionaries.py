my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Get a list of all the keys in the dictionary
print(my_dict.keys())  

# Get a list of all the values in the dictionary
print(my_dict.values())  

# Get a list of all the key-value pairs as tuples
print(my_dict.items())  

# Get the value for a given key, or a default value if the key does not exist
print(my_dict.get("banana", 0)) 
print(my_dict.get("orange", 0))  

# Remove and return the value for a given key, or a default value if the key does not exist
print(my_dict.pop("banana", 0)) 
print(my_dict.pop("orange", 0))  

# Update the dictionary with key-value pairs from another dictionary
my_dict2 = {"banana": 4, "orange": 5}
my_dict.update(my_dict2)
print(my_dict)  

# Remove all key-value pairs from the dictionary
my_dict.clear()
print(my_dict)  
