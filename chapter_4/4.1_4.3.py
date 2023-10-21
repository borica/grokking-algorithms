from typing import List
def sum_list(list_to_sum: List) -> int:
    if not len(list_to_sum):
        return 0

    number = list_to_sum.pop(0)

    return number + sum_list(list_to_sum)

def count_list_items(list_to_count: List) -> int:
    if not len(list_to_count):
        return 0

    number = 1
    list_to_count.pop(0)

    return number + count_list_items(list_to_count)

def highest_number_in_list(list_to_rank: List) -> int:
    if not len(list_to_rank):
        return 0

    number = list_to_rank.pop()
    highest_number = highest_number_in_list(list_to_rank)

    if number > highest_number:
        return number

    return highest_number

print(f'Sum is: {sum_list([1, 2, 3, 4, 5])}')
print(f'Count is: {count_list_items([1, 2, 3, 4, 5])}')
print(f'Highest Number is: {highest_number_in_list([10, 55, 33, 44, 22])}')