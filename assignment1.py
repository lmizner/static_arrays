# Course: CS261 - Data Structures
# Student Name: Lauren Mizner
# Assignment: Assignment 1
# Description: 

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():

    for i in range(0, arr.size()):
        if i == 0:
            min = arr.get(0)
            max = arr.get(0)
        elif arr.get(i) <= min:
            min = arr.get(i)
        elif arr.get(i) >= max:
            max = arr.get(i)
    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    
    # Create a new array
    new_arr = StaticArray(arr.size())
    array = []

    for i in range(0, arr.size()):
        # If the value is divisible by 3 and 5
        if arr.get(i) % 3 == 0 and arr.get(i) % 5 == 0:
            array.append("fizzbuzz")
        
        # If the value is divisible by 3 only
        elif arr.get(i) % 3 == 0:
            array.append("fizz")

        # If the value is divisible by 5 only
        elif arr.get(i) % 5 == 0:
            array.append("buzz")

        # If the value is doesn't fit into any of the above situations
        else:
            array.append(arr.get(i))
    
    # Update the new array
    for i in range(0, arr.size()):
        new_arr.set(i, array[i])

    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:

    #Set a new empty array
    array = []

    #Cycles through given StaticArray extracting items and adding to new array
    for i in range(0, arr.size()):
        array.append(arr.get(i))
    
    #Begins at the end and moves toward the start, one step at a time
    array = array[::-1]

    #Update new array
    for i in range(0, arr.size()):
        arr.set(i, array[i])


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:

    # Create a new array
    new_arr = StaticArray(arr.size())

    # Simplifying down rotations by cutting out additional cycles
    r_count = abs(steps) % arr.size() 

    # Set pointer value to current position
    j = 0

    # Rotate right
    if steps < 0:
        for i in range(r_count, arr.size()):
            new_arr.set(j, arr.get(i))
            j+=1
        for i in range(0, r_count):
            new_arr.set(j, arr.get(i))
            j+=1
    # Rotate left
    else:
        for i in range(arr.size()-r_count, arr.size()):
            new_arr.set(j, arr.get(i))
            j+=1
        for i in range(0, arr.size()-r_count):
            new_arr.set(j, arr.get(i))
            j+=1

    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    
    #Determine new array size
    size = abs(end - start) + 1

    #Create new array
    new_arr = StaticArray(size)

    # Determine direction (+1 or -1 each step)
    if end > start:
        for i in range(0, size):
            new_arr.set(i, start+i)
    else:
        for i in range(0, size):
            new_arr.set(i, start - i)

    return new_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    count_1 = 0
    count_2 = 0
    
    #If true add to respective count
    for i in range(0, arr.size()-1):
        #Ascending order
        if arr.get(i) < arr.get(i+1):
            count_1+=1
        #Descending order
        elif arr.get(i) > arr.get(i+1):
            count_2+=1

    #Ascending order
    if count_1 == (arr.size()-1):
        return 1
    #Descedingin order
    elif count_2 == (arr.size()-1):
        return 2
    #All else
    else:
        return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    
    #Set a new empty array
    array = []

    #Cycles through given StaticArray extracting items and adding to new array
    for i in range(0, arr.size()):
        array.append(arr.get(i))
    
    #Sorts array in ascending order using bubble sort method
    for i in range(0, arr.size()):
        for j in range(i+1, arr.size()):
            if (array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    #Update new array
    for i in range(0, arr.size()):
        arr.set(i, array[i])


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:

    #If array contains only 1 item
    if arr.size() == 1:
        return arr

    #Create a new array/list
    array = []

    #Cycles through given StaticArray extracting items and adding to new array
    for i in range(0, arr.size()):
        if arr.get(i) not in array:
            array.append(arr.get(i))

    #Update new array
    new_arr = StaticArray(len(array))
    for i in range(0, len(array)):
        new_arr.set(i, array[i])

    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
   
    #Set a new empty array
    size = arr.size()
    new_arr = StaticArray(size)

    #Initialize count array
    #min_max function returns a tuple of the min and max values in a given integer list 
    min_and_max = min_max(arr)
    low = min_and_max[0]
    high = min_and_max[1]
    counter = abs(high - low) + 1

    count = [0] * counter
    for i in range(0, size):
        #To account for negative numbers in the count
        if low < 0:
            get = arr.get(i) + abs(low)
            count[get] += 1
        #Positive number only case
        else:
            count[arr.get(i) - low] += 1

    #Store the cumulative count
    length = len(count)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    #Find the index of each element of the original array in the count array
    #Place the elements in the output array
    i = size - 1

    #Uploading sorted array into new array
    while i >= 0:
        if low <= 0:
            num = arr.get(i) + abs(low)
            new_arr.set(size - (count[num]), arr.get(i))
            count[num] -= 1
            i -= 1
        else:
            num = count[arr.get(i) - low]
            new_arr.set(size - (num), arr.get(i))
            count[arr.get(i) - low] -= 1
            i -= 1
        
    return new_arr


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    
    #Set up a new array
    array = []

    #Initialize starting index for each array
    a = 0 
    b = 0 
    c = 0

    size_1 = arr1.size()
    size_2 = arr2.size()
    size_3 = arr3.size()

    #Iterate through all three arrays from 0 to the size of each array
    while (a < size_1 and b < size_2 and c < size_3):
        #If a = b and b = c then add the value to the new array
        if (arr1.get(a) == arr2.get(b) and arr2.get(b) == arr3.get(c)):
            array.append(arr1.get(a))
            a += 1
            b += 1
            c += 1
        
        #If x < y (array1 value < array2 value)
        elif (arr1.get(a) < arr2.get(b)):
            a += 1
        
        #If y < z (array2 value < array3 value)
        elif (arr2.get(b) < arr3.get(c)):
            b += 1
        
        #If z < x and z < y (array3 value < array1/array2)
        else:
            c += 1
    
    #If there are no matching values
    if len(array) == 0:
        new_arr = StaticArray(1)
        new_arr.set(0, None)
    else:
        new_arr = StaticArray(len(array))
        for i in range(0, len(array)):
            new_arr.set(i, array[i])

    return new_arr


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    
    #Implements a two pointer method sorting algorithm
    #Set up a new array
    size = arr.size()
    array = StaticArray(size)

    #Set pointers and count(keeps track of index) values
    count = size - 1
    j = size - 1
    i = 0 

    #Sort in ascending order and square values
    while count >= 0:
        if abs(arr.get(i)) < abs(arr.get(j)):
            array.set(count, arr.get(j) ** 2)
            count -= 1
            j -= 1

        elif abs(arr.get(i)) == abs(arr.get(j)):
            array.set(count, arr.get(j) ** 2)
            count -= 1
            j -= 1

        elif abs(arr.get(i)) > abs(arr.get(j)):
            array.set(count, arr.get(i) ** 2)
            count -= 1
            i += 1
    
    return array
    

# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    
    #Set initial variables
    num_1 = 0 
    num_2 = 0 
    size_1 = arr1.size()
    size_2 = arr2.size()

    #Convert each array to integer value to obtain sum
    for i in range(0, size_1):
        num_1 = (num_1 * 10) + arr1.get(i)
    
    for i in range(0, size_2):
        num_2 = (num_2 * 10) + arr2.get(i)

    sum = num_1 + num_2

    #If the sum is equal to zero...
    if sum == 0:
        new_array = StaticArray(1)
        new_array.set(0, 0)
        return new_array

    #Set up a new array and index value
    array = []

    while sum > 0:
        value = sum % 10
        array.append(value)
        sum = sum//10

    #Update new static array
    new_array = StaticArray(len(array))
    for i in range(0, len(array)):
        new_array.set(i, array[i])

    reverse(new_array)

    return new_array


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:

    #if rows and cols equal one
    if rows == 1 and cols == 1:
        array = StaticArray(1)
        array.set(0, StaticArray(1))
        array.get(0).set(0, start)
        return array
    
    row = StaticArray(rows)
    for i in range(0, row.size()):
        row.set(i, StaticArray(cols))

    #Set initial variables
    turn = 0
    place = 0

    #If the start value is negative...
    if start < 0:
        size = start - rows * cols
        static_row = rows
        static_col = cols
        first_row = rows - 1

        while start != size:
            if turn == 0:
                #Start in lower left corner going counter clockwise
                if start != size:
                    for i in range(place, static_col):
                        row.get(first_row).set(i, start)
                        cols = i
                        start -= 1

                #Increment the row
                static_row -= 1

                if start != size:
                    for i in range(static_row - 1, place - 1, -1):
                        row.get(i).set(cols, start)
                        rows = i
                        start -= 1
                turn += 1
            
            #For moving on to the horizontal portion of the matrix
            elif turn == 1:
                #Increment the column
                static_col -= 1
                
                if start != size:
                    for i in range(static_col - 1, place - 1, -1):
                        row.get(rows).set(i, start)
                        cols = i
                        start -= 1
                
                place += 1

                if start != size:
                    for i in range(place, static_row):
                        row.get(i).set(cols, start)
                        rows = i
                        first_row = i
                        start -= 1
                turn -= 1

    #If the start value is positive...
    else:
        size = start + rows * cols
        static_row = rows
        static_col = cols
        first_cols = cols - 1

        while start < size:
            if turn == 0:
                #Start with the upper right corner going clockwise
                if start != size:
                    for i in range(place, static_row):
                        row.get(i).set(first_cols, start)
                        rows = i
                        start += 1
                
                #Increment the column
                static_col -= 1

                if start != size:
                    for i in range(static_col - 1, place - 1, -1):
                        row.get(rows).set(i, start)
                        cols = i
                        start += 1
            
                turn += 1

            elif turn == 1:
                if start != size:
                    for i in range(rows - 1, place - 1, -1):
                        row.get(i).set(cols, start)
                        rows = i
                        start += 1

                place += 1

                if start != size:
                    for i in range(place, static_col):
                        row.get(rows).set(i, start)
                        cols = i
                        first_cols = i
                        start += 1
                
                #Increment the row
                static_row -= 1
                turn -= 1
    
    return row


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "1234567890"
    converted = list(source)

    for i in range(0, len(converted)):
        if converted[i] in s1:
            for j in range(0, len(s1)):
                if converted[i] == s1[j]:
                    converted[i] = s2[j]
                    break
        elif converted[i] in upper:
            converted[i] = ' '
        elif converted[i] in lower:
            converted[i] = '#'
        elif converted[i] in number:
            converted[i] = '!'
        else:
            converted[i] = '='
        
    source = "".join(converted)
    return source



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)
    print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)


    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')
    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = (
        (4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
        (4, 4, -1), (3, 4, -3), (2, 3, -12), (1, 2, -42),
    )
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
