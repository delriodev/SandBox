'''
LEGB
Local - Enclosed - Global - Built-in
'''

x = 'Global x'

def f1():
    x = 'Local x'
    print(x)
f1()
print(x)

print()

# Notice the usage of the global keyword
def f2():
    global x # Sets a new global variable 
    x = 'Local x'
    print(x)
f2()
print(x)

print()

# Enclosing

def outer():
    x = 'Outer x'

    def inner():
        nonlocal x
        x = 'Inner x'
        print(x) # Has access to local, enclosing and global

    inner()
    print(x) # Has access to local and global

outer()


# Conclusion: Smaller scopes have access to Larger data