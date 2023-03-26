# Using the difference() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  

# Using the - operator
difference_set = set1 - set2
print(difference_set)  

# Using the symmetric_difference() method

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) 

# Using the ^ operator
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set) 
