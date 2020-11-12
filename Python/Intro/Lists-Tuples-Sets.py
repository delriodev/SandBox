courses = ['History', 'Math', 'Physics', 'CompScience']
courses2 = ['Telepathy', 'Chess']

print(courses)
print(courses2)
print()
print("     Get items [0:2[          : courses[0:2]                     = " + str(courses[0:2]))
print("     Get items [beggining:2[  : courses[:2]                      = " + str(courses[:2]))
print("     Get items [2:end[        : courses[2:]                      = " + str(courses[2:]))
print("     Get First Item           : courses[0]                       = " + courses[0])
print("     Get Last Item            : courses[-1]                      = " + courses[-1])
courses.append('Art')
print("     Append to end of list    : courses.append('Art')            = " + str(courses))
courses.insert(0, 'Phyolosophy')
print("     Insert to beggining      : courses.insert(0, 'Phylosophy')  = " + str(courses))
courses.insert(0, courses2)
print("     Insert List inside List  : courses.insert(0, courses2)      = " + str(courses))
print("     Get Item by Index        : courses[0]                       = " + str(courses[0]))
courses.pop(0)
# Removes last item by default
# Returns the removed value
print("     Delete item by index     : courses.pop(0)                   = " + str(courses))
courses.extend(courses2)
print("     Concat 2 lists           : courses.extend(courses2)         = " + str(courses))
courses.remove('Math')
print("     Delete item y index      : courses.remove('Math')           = " + str(courses))

