# Definition
# Keys can be any immutable data type
_dict = {'name': 'Daniel', 'age': 25 , 'courses': ['Math', 'CompSci'], 'key': 'value'}

print("                                   _dict                                                                 = " + str(_dict))

# Access the dictionary
print("     Get Value bye Key           : _dict['key']                                                          = " + str(_dict['key']))
print("     Get Value bye Key           : _dict['courses']                                                      = " + str(_dict['courses']))
print("     Get Value method            : _dict.get('name')                                                     = " + str(_dict.get('name')))
print("     Get Value method            : _dict.get('phone')                                                    = " + str(_dict.get('phone')))
print("     Get Value method            : _dict.get('phone', 'Not found')                                       = " + str(_dict.get('phone', 'Not found')))
print("     Get Keys                    : _dict.keys()                                                          = " + str(_dict.keys()))
print("     Get Values                  : _dict.valaues()                                                       = " + str(_dict.values()))
print("     List of key,value tuples    : _dict.items()                                                         = " + str(_dict.items()))

_dict['phone'] = '555-555'
print("     Upsert value                : _dict['phone'] = 555-5555                                             = " + str(_dict))

# Takes in a dictionary as an argument
_dict.update({'name': 'Jane', 'age': 26, 'phone': '514-555-5555'})
print("     Update multple values       : _dict.update({'name': 'Jane', 'age': 26, 'phone': '514-555-5555'})    = " + str(_dict))

for k in ('age', 'courses'):
    del _dict[k]
print("     delete                      : for k in ('age', 'courses'): del _dict[k]                             = " + str(_dict))

name = _dict.pop('name')
print("     Pop & return val            : name = _dict.pop('name')                                              = " + str(_dict))

# Looping
# The default iterator uses the keys
print()
print("Iterate throught keys by default")
for default_iterator in _dict:
    print(default_iterator)
print()
print("Iterate throught items: for item in keys.items():  ")
for item in _dict.items():
    print(item)
print()