# Defining a string variable
message = "Hello World"
# With inner '
m1 = 'Bobby\'s World'
# On multiple lines
m2 = ''' 
Hello
World
'''
mm = 'message : '
m3 = 'len(message) : '
m5 = 'message[1] : '
m7 = 'message[0:7] : '
m9 = 'message[:7] : '
m11 = 'message[7:] : '
m13 = 'message.lower() : '
m14 = 'message.upper() : '
m15 = 'message.count("l") : '
m16 = 'message.find("Sherb") : '
m17 = 'new message = message.replace("World", "Sherb") : '
m18 = 'f\'{message}, {new_message}. Welocome!\' : '
m20 = 'To get a list of all attributes and methods of a class. dir(message)'

# Casting int to str
m4 = str(len(message))
# Selecting a character from a string
m6 = message[1]
# Selecting a segment of characters from a string
m8 = message[0:7]
m10 = message[:7]
m12 = message[7:]
# Replace part of a string
new_message = message.replace("World", "Sherb")
# Formating string
m19 = f'{message}, {new_message.upper()}. Welcome!'

print()
print(mm + message)
print(m3 + m4)
print(m5 + m6)
print(m7 + m8)
print(m9 + m10)
print(m11 + m12)
# String methods
print(m13 + message.lower())
print(m14 + message.upper())
print(m15 + str(message.count('l')))
print(m16 + str(message.find('Sherb')))
print(m17 + new_message)
print(m18 + m19)
print()
print("List of methods of a class: dir(message) " + str(dir(message)))
print()
print(help(str.lower))
print()
print(help(str))

print()