# ID = {'4D':('0583',9083,1342,2650,4072,7454,9591,1069)}
# a = []
# for k in ID['4D']:
#     SID = int('80220'+str(k))
#     a.append(k)
#     print(SID)
    


''' Check if all elements in list are unique, returns true or false, change to != to return true if there are duplicates'''
def all_unique(lst):
    return len(lst) == len(set(lst))

y = [1,2,3,4,5]
#print(all_unique(y))

'''Check memory usage of an objet'''
import sys 
variable = 32 
#print(sys.getsizeof(variable))

'''The method shown below returns the length of the String in bytes'''
def byte_size(string):
    return(len(string.encode('utf-8')))
# print(byte_size('Hello World'))

'''This method splits the list into smaller lists of the specified size:'''
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
lstA = [1,2,3,4,5,6,7,8,9,10]

#print(chunk(lstA, 3))

'''Remove the false values (False, None, 0, and ‘’) from the list using filter() method
Empty strings but not whitespce:'''

def compact(lst):
    return list(filter(bool, lst))
#print(compact([0, 1, False, 2, '' , ' ', 3, 'a', 's', 34]))

#notsure what this does
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
#[print(i) for i in transposed]


'''Flatten out list of lists using recursion'''


def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list

#print(deep_flatten([1, [2], [[3], 4], 5]) )

'''This method finds the difference between the two iterations, keeping only the values that are in the first:'''
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
difference([1,2,3], [1,2,4]) # [3]


'''The following method returns the difference between the two lists after applying this function to each element of both lists'''
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]
from math import floor
#print(difference_by([2.1, 1.2], [2.3, 3.4],floor)) # [1.2]
#print(difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])) # [ { x: 2 } ]

''' Multile function calls on one line'''
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
a, b = 4, 5
#print((subtract if a > b else add)(a, b)) # 9'''


'''Combine to dictionaries'''
def merge_dictionaries(a, b):
    return {**a,**b}
a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
#print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}

''' Convert two lists to a dict'''
def to_dictionary(keys, values):
    return dict(zip(keys, values))
keys = ["a", "b", "c"]    
values = [2, 3, 4]
#print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}