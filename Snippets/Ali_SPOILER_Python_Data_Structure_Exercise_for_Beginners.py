# 1

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


def make_third_list(l1, l2):
    new_l1 = []
    new_l2 = []
    l3 = []

    for x in range(len(l1)):
        if x == 0:
            new_l2.append(l2[x])
        if x != 0:
            if x % 2 != 0:
                new_l1.append(l1[x])
            elif x % 2 == 0:
                new_l2.append(l2[x])

    l3 = new_l1 + new_l2
    print(f"Element at odd-index positions from list one\n"
          f"{new_l1}\n"
          f"Element at even-index positions from list two\n"
          f"{new_l2}\n\n"
          f"Printing Final third list\n"
          f"{l3}")


# make_third_list(l1, l2)

# 2

list2 = [54, 44, 27, 79, 91, 41]


def remove_add_items(l1):
    index4 = l1[4]
    print(f"Original list {l1}")
    l1.pop(4)
    print(f"List after removing item at 4th index {l1}")
    l1.insert(1, index4)
    print(f"List after adding element to the second position {l1}")
    l1.append(index4)
    print(f"List after adding element to the last position {l1}")


# remove_add_items(list2)

# 3
import numpy as np

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def slice_3_pieces(l1):
    ls_master = [[], [], []]

    if len(l1) % 3 == 0:
        slice_length = int(len(l1) / 3)
        s = slice(0, slice_length)

        for x in range(3):
            s = slice(slice_length * x, slice_length + (x * 3))
            ls_master[x].append(l1[s])

    for x in range(3):
        # reverse_list = np.flip(ls_master[x])
        reverse_list = reversed(ls_master[x])
        print(f"Chunk {x + 1} {ls_master[x]}\n"
              f"After reversing it {list(reverse_list)}")


# slice_3_pieces(sample_list)


# 4

sample_list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]


def number_occurrence(number_list):
    number_dict = {}

    for number in number_list:
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1

    print(number_dict)


# number_occurrence(sample_list1)


# uber problem

def product_of_list(list1):
    result = []
    product_value = 1
    # Iterating through the given list
    for num1 in range(len(list1)):
        if list1[num1] == 0:
            result.append("NaN")
            continue
        for num2 in range(len(list1)):  # Iterating through every number on the list for product
            product_value = product_value * list1[num2]
        product_value = product_value / list1[num1]  # Dividing by the current index value
        result.append(int(product_value))
        product_value = 1

    return result


list20 = [1, 2, 3, 4, 5, 0]
# print(product_of_list(list20))


# 5

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]


def combine_list_tuple(l1, l2):
    print(list(zip(l1, l2)))


# combine_list_tuple(first_list, second_list)


# 6


first_set1 = {23, 42, 65, 57, 78, 83, 29}
second_set2 = {57, 83, 29, 67, 73, 43, 48}


def list_inter_final(set1, set2):
    inters = set1.intersection(set2)  # Take same elements from lists  (Can also use &)
    # inters = set1 & set2
    print(f"Intersection of the two sets are {inters}")
    for number in inters:
        set1.discard(number)  # remove crashed program if there is not that item to remove, discard does not

    print(f"First set after removing intersection numbers {set1}")


# list_inter_final(first_set1, second_set2)


# 7

first_set7 = {27, 43, 34}
second_set7 = {34, 93, 22, 27, 43, 53, 48}


def subset_superset(set1, set2):
    print(f"First set is subset of second set - {set1.issubset(set2)}")
    print(f"Second set is subset of First set - {set2.issubset(set1)}\n")
    print(f"First set is Super set of second set - {set1.issuperset(set2)}")
    print(f"Second set is Super set of First set - {set2.issuperset(set1)}")
    for numbers in set1.intersection(set2):
        set1.remove(numbers)

    print(f"First Set {set1}")
    print(f"Second Set {set2}")


# subset_superset(first_set7, second_set7)


# 8

roll_number = [47, 64, 65, 67, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}


def match_list_to_dict_values(l1, d1):
    remove_list = []
    for num in range(len(l1)):
        if l1[num] not in d1.values():
            remove_list.append(l1[num])

    # l1[:] = [num for num in l1 if num in d1.values()]
    print(l1)




# match_list_to_dict_values(roll_number, sample_dict)


#9

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}


def values_to_dict(d1):
    values = []
    # values = [num for num in d1.values() if num not in values]
    for num in d1.values():
        if num not in values:
            values.append(num)
    print(values)


# values_to_dict(speed)


#10

sample_list2 = [87, 45, 41, 65, 94, 41, 99, 94]

def tuple_func(l1):
    original_list = []

    for x in l1:
        if x not in original_list:
            original_list.append(x)

    print(f"unique items {original_list}")
    tuple_list = tuple(original_list)
    print(f"tuple {tuple_list}")
    print(f"min: {min(tuple_list)}")
    print(f"max: {max(tuple_list)}")



tuple_func(sample_list2)







