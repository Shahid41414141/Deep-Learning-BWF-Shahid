import time

start_time = time.time()

# Using range() 
for i in range(5): 
    print(i)  # Output: 0 1 2 3 4 
 
# Using enumerate() 
fruits = ['apple', 'banana', 'mango'] 
for i, fruit in enumerate(fruits): 
    print(f'{i}: {fruit}') 

end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time: ", elapsed_time, " seconds")
