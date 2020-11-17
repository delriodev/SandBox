import Module_To_Import
import Module_To_Import as IndexFinder
from Module_To_Import import find_index
from Module_To_Import import find_index as fi, test
from Module_To_Import import *
import sys

_list = ['History', 'Math', 'Physics', 'CompScience']

print(IndexFinder.find_index(_list, 'Math'))
print(Module_To_Import.find_index(_list, 'CompScience'))
print(find_index(_list, 'Physics'))
print(fi(_list, 'History'))
print(Module_To_Import.test)
print(test)

print(sys.path)