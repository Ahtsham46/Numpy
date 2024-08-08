import numpy as np
def sort_list():
    num = int(input("How many number you want to enter: "))
    list = []
    for x in range(num):
        a = int(input(f"Enter {x+1} number: "))
        list.append(a)
    print(f'Numbers are = {list}')
    arr = np.array(list)
    sorted_number = np.sort(arr)
    print("Sort numbers in ascending order are following: ")
    print(sorted_number)
sort_list() 