# Begin.
nums = [1, 2, 3, 4, 5]
x = 0
# For each
#break, continue
for i in nums:
    if i == 3:
        print("Found!")
        break
    print(i)
for i in nums:
    if i == 3:
        print("Found!")
        continue
    print(i)
# Nested loop
for i in nums:
    for letter in 'abc':
        print(i, letter)
# Iterate in a range: start at arg0 Up to but not included arg1
for i in range(1, 10):
    print(i)
# While loop
while x <= 5:
    print(x)
    x += 1
    if x == 4:
        break
# while True:

