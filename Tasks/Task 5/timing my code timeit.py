import timeit

code_to_time = """
# Using range() 
for i in range(5): 
    print(i)  # Output: 0 1 2 3 4 
 
# Using enumerate() 
fruits = ['apple', 'banana', 'mango'] 
for i, fruit in enumerate(fruits): 
    print(f'{i}: {fruit}')"""


num_runs = 1000

elapsed_time = timeit.timeit(code_to_time, number=num_runs)

print("Elapsed time: ", elapsed_time / num_runs, " seconds per run")
