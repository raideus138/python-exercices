
'''
Create a list by picking an odd-index items from the first list and even index items from the second
'''
list_one = [1,2,3,4,5,6,7,8,9,10]
list_two = [1,2,3,4,5,6,7,8,9,10]

def even_index(list):
    new_list = []
    for i in range(1,len(list)+1):
        if i % 2 == 0:
            new_list.append(i)
    return new_list
def odd_index(list):
    new_list = []
    for i in range(1,len(list)+1):
        if i % 2 != 0:
            new_list.append(i)
    return new_list

print(f'Odd list is: {odd_index(list_one)}. Even list is: {even_index(list_two)}')