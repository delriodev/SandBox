print(''' 
    ==   !=  >   <   >=  <=  is  
    and or not
''')

condition = "a"

if condition == "c":
    print("What a surprise")
elif condition == "b":
    print("Got it!")
else:
    print('no match')
print()

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a = [1, 2, 3]")
print("b = [1, 2, 3]")
print("c = a")
print('id(a): ')
print(id(a))
print('id(b): ')
print(id(b))
print('id(c): ')
print(id(c))
print()
print("a is b: ") 
print(a is b)
print("a is c: ") 
print(a is c)
print("b is c: ") 
print(b is c)
print("a == b: ") 
print(a == b)
print("a == c: ") 
print(a == c)
print("b == c: ") 
print(b == c)

print()

#Evaluating False
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence: '', (), []
    # Any empty mapping: {}

condition = False
if not condition:
    print("False: f")
condition = None
if not condition:
    print("None: f")
condition = 0
if not condition:
    print("Zero of any numeric type: f")
condition = ()
if not condition:
    print("Any empty sequence: f")
condition = {}
if not condition:
    print("Any empty mapping: f")
