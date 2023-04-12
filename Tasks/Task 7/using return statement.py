num = 0

def increment():
    global num
    num += 1

increment()
print(num)  

def multiply(num1, num2):
    return num1 * num2

result = multiply(3, 4)
print(result)  
