_list = ['History', 'Math', 'Physics', 'CompScience']
_list2 = ['Telepathy', 'Chess']

print("                                _list                          = " + str(_list))
print("                                _list2                         = " + str(_list2))
print()
print("     Get items [0:2[          : _list[0:2]                     = " + str(_list[0:2]))
print("     Get items [beggining:2[  : _list[:2]                      = " + str(_list[:2]))
print("     Get items [2:end[        : _list[2:]                      = " + str(_list[2:]))
print("     Get First Item           : _list[0]                       = " + _list[0])
print("     Get Last Item            : _list[-1]                      = " + _list[-1])
_list.append('Art')
print("     Append to end of _list    : _list.append('Art')            = " + str(_list))
_list.insert(0, 'Phyolosophy')
print("     Insert to beggining      : _list.insert(0, 'Phylosophy')  = " + str(_list))
_list.insert(0, _list2)
print("     Insert _list inside _list  : _list.insert(0, _list2)         = " + str(_list))
print("     Get Item by Index        : _list[0]                       = " + str(_list[0]))
_list.pop(0)
# Removes last item by default
# Returns the removed value
print("     Delete item by index     : _list.pop(0)                   = " + str(_list))
_list.extend(_list2)
print("     Concat 2 _lists           : _list.extend(_list2)            = " + str(_list))
_list.remove('Math')
print("     Delete item y index      : _list.remove('Math')           = " + str(_list))
_list.reverse()
print("     Reverse items            : _list.reverse()                = " + str(_list))
# Sorting
_list.sort()
print("     Sort _list by reference   : _list.sort()                   = " + str(_list))
_list.sort(reverse=True)
print("     Sort items reverse order : _list.sort(reverse=True)       = " + str(_list))
# Sort func to create Copy of Object vs sort method to change object by reference
sorted__list = sorted(_list)
print("     Copy sorted _list         : sorted__list = sorted(_list)    = " + str(sorted__list))
print("     Other Functions          : min(_list), max(_list), sum(_list)")
print("     Find index from value    : _list.index('Math')            = " + str(_list.index('Chess')))
print("     CHeck existance          : 'Art' in _list                 = " + str('Math' in _list))
# Joining string separated by specified value
joint_str = ', '.join(_list)
print("     Joining strings          : joint_str = ', '.join(_list)   = " + joint_str)
new__list  = joint_str.split(', ')
print("     Turn string into _list    : new__list  = joint_str.split(', ')   = " + str(new__list))

#For loop without index
print("Looping : ")
for item in _list2:
    print(item)
for index, course in enumerate(_list2):
    print(index, course)
for index, course in enumerate(_list2, start=100):
    print(index, course)

#IMMUTABLE _list (Read Only) : Tuple
# Does not support remove, append, [], or any other kind of modification to it's elements
tuple1 = tuple(_list)
print ("Tuple: " + str(tuple1) + "  - Cannot be modified")

#UNORDERED _list without DUPLICATES : Set
# Removes duplicates automatically
# More efficient membership tests
set1 = set(_list)
set2 = set(_list2)
set2.add('Boy')
print ("Set1:   " + str(set1))
print ("Set2:   " + str(set2))

empty__list = []
empty__list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_dictionnary = {}
empty_set = set()
