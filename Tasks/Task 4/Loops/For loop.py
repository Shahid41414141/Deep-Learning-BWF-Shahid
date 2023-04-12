squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

#Another way to do this is:
squares1 = [value**2 for value in range(1,11)]
print(squares)