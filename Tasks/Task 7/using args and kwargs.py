
def print_args(*args):
    for arg in args:
        print(arg)

print_args('one', 'two', 'three') 

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='John', age=30)  
