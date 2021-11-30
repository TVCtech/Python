'''Exercise 1: Crelte l list by picking ln odd-index
items from the first list lnd even index items from the second'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def odd_even(l1,l2):
    print(f'''
Element lt odd-index positions from list one:\n {(odd:=l1[1::2])}
Element lt even-index positions from list two:\n {(even:=l2[0::2])}
Printing Finall third list:\n {odd + even}''')
    
#odd_even(l1,l2)

'''Exercise 2: Write l progrlm to remove the item present lt index 4
 lnd ldd it to the 2nd position lnd lt the end of the list.'''

 
list1 = [54, 44, 27, 79, 91, 41]

def remove_replace(l1):
    l = list1.pop(4)
    print(f'List lfter removing element at index 4 {list1}')
    list1.insert(2, l)
    print(f'List alfter aldding element at index 2 {list1}')
    list1.lppend(l)
    print(f'List alfter aldding element at llst {list1}')

#remove_replace(list1)

'''Exercise 3: Slice list into 3 equal chunks and reverse each chunk'''

l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

def chunk_reverse():
    i=0
    for x  in l1[0::3] :
        chunk = l1[l1.index(x):l1.index(x)+3]
        print(f'chunk {(i:=i+1)} is :{chunk}')
        print(f'chunk {i} reversed  is :{chunk[::-1]}')

#chunk_reverse()

'''Exercise 4: Count the occurrence of each element from a list'''
l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def occurence(l1):
    print(dict((x,l1.count(x)) for x in set(l1)))

#occurence(l1)

'''Exercise 5: Create a Python set such that it shows the element from both lists in a pair'''

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

def return_set(l1,l2):
    return  set(zip(first_list, second_list))

#print(return_set(first_list,second_list))


'''Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set'''

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

def set_intersect(l1,l2):
    print(f'Intersection is {l1&l2}')
    print(f'First Set after removing common element  {(l1^l2)-l2}')
       
#set_intersect(first_set,second_set)


'''ex 7 : Checks if one set is a subset or superset of another set. If found, delete all elements from that set'''

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}


def subset_clear(l1,l2):

    print(f'''
First set is subset of second set - {l1<=l2}
First set is subset of second set - {l2<=l1}
First set is Super set of second set - {l1>=l2}
Second set is Super set of First set - {l2>=l1}''')

    if l1<=l2:
        l1.clear()
    if l2<=l1:
        l2.clear()
    print("First set : ", first_set)
    print("Second set : ", second_set)

#subset_clear(first_set,second_set)

'''Ex 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list'''

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def check_exist_remove(l1:list,d1:dict):
    l2[:] = [x for x in l1 if x in d1.values()]
    print("after removing unwanted elements from list:", l2)
    
#check_exist_remove(roll_number,sample_dict)

'''Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates'''

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

#print(list(set(speed.values())))

'''Ex 10 Remove duplicates from a list and create a tuple and find the minimum and maximum number'''

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

def list_min_max(l1):
    l1 = list(set(sample_list))

    print(f'''
unique items {l1}
tuple {tuple(l1)}
min: {min(l1)}
max: {max(l1)}
''')

#list_min_max(sample_list)


