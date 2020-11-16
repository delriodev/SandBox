# Functions

# Will write function body later.
def hello_func():
    pass

print(hello_func)
print(hello_func())

def hello():
    print("Hello World!")

hello()

def hi(greeting, name = 'Mathieu'):
    return f'{greeting}, {name} Function'

print(hi('Welcome'))

def student_info(*args, **kwargs):
    print(args) # Tuple 
    print(kwargs) # Dictionary
print()
student_info('Daniel', 'Mathieu', 'Alex', subjects=['Math', 'Arts', 'History'], age=23)
print()
names = ['Daniel', 'Mathieu', 'Alex']
info = {'subjects': ['Math', 'Arts', 'History'], 'age': 23}
print()
student_info(names, info)
print()
student_info(*names, **info)
print()
