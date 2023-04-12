set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add an element to set1
set1.add(5)
print(set1)  

# Remove an element from set2
set2.remove(6)
print(set2)  

# Clear all elements from set1
set1.clear()
print(set1) 

# Copy set2 to a new set
set3 = set2.copy()
print(set3)  

# Check if set3 is a subset of set2
print(set3.issubset(set2))  

# Check if set2 is a superset of set3
print(set2.issuperset(set3))  
