# INPUT : A collection of numbers, an amount of entries n=2
# OUTPUT : The product of the first n numbers that sum to 2020 

numbers = []
ENTRIES = 3
TARGET = 2020

def binary_search(arr, target):

    pivot = get_first_index_bigger_than(arr, target/2)

    for x in arr[:pivot]:
        for y in arr[pivot:]:
            if(x + y == 2020):
                return x*y


def get_first_index_bigger_than(arr, target):
    for index, val in enumerate(arr):
        if(val > target):
            return index
    return -1

# 1. Parse the data into an int array
with open('input') as input:
    numbers = [int(val) for val in input] 
# 2. Find the 2 numbers
numbers.sort()
# 3. Binary search
print(binary_search(numbers, TARGET))

# PART TWO
# For n = 3

def find3Numbers(arr, target):
    for i in range(0, len(arr) - 2):
        l = i + 1
        r = len(arr)-1
        while(l < r):

            summ = arr[i] + arr[l] + arr[r]

            if( summ == TARGET ):
                return arr[i] * arr[l] * arr[r]
            elif( summ < TARGET ):
                l += 1
            else: # summ > TARGET
                r -= 1
    return -1

print(find3Numbers(numbers, TARGET))