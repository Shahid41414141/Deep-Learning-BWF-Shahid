letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(letters[0::3])

numbers = list(range(0, 20))
# print(numbers[::-1])

nestlist = [numbers, letters]
print("\n",nestlist)

newlist = list(range(0, 100, 5))
print("\n",newlist)

combined = [newlist, nestlist]
print("\n",combined)