

"""
Was unclear the first time submitting
not 2 values next to eachother, but just a duplicate value first found
"""

"""
0, 1, 5, 4, 3, 2, 5, 4, 3, 3

answer = 5


lets use a set, 
as you go through each element in the array, insert the element into the set
if the value exists, return the value,
else, add the element into the set
if nothing else is returned, return -1

"""




# previous attempt
"""
an array of numbers
Find the first duplicate (two repeating values adjacent to eachother)
if no duplicates, return -1

4 5 3 2 2 5 3 4 4 0 5
0 1 2 3 4 5 6 7 8 9 10
answer = 2

1 2 3 4 5 6
answer = -1

10
answer = -1

# case 1
arrays with 0, or 1 element, will always be -1

# case 2
while iterating the list, since we're checking 1 ahead with the current,
you need to limit the iteration by 1 less to ensure you don't go out of
bound of the array

4 5 3 2 2 5 3 4 4 0 5
0 1 2 3 4 5 6 7 8 9 10

length = 11
for i in range(array_length -1)

9, 10
element_i == element_(i+1)

if you don't, then you'll have

10, 11
element_i == element_(i +1) 
-> error

"""


# def main(array):
    
#     if len(array) < 2:
#         return -1
    
#     for i in range(len(array) -1):
#         if array[i] == array[i +1]:
#             return array[i]
    
#     return -1


def main(array):

    array_set = set()

    for element in array:
        if element in array_set:
            return element
        else:
            array_set.add(element)
        
    return -1





if __name__=="__main__":

    test_values = [
        [5, 4, 3, 10, 3, 8, 0, 5, 6],
        [1, 2, 3, 4],
        [3, 4, 200, 4, 3],
        [],
        [5],
        [50000, 100, 300, 20],
        [10, 0, 5, 10, 5]
    ]

    test_answers = [
        3,
        -1,
        4,
        -1,
        -1,
        -1,
        10
    ]

    for value, answer in zip(test_values, test_answers):
        result = main(value)

        assert result == answer, f"Test case failed for {value}, expected {answer}, result was {result}"
        print(f'Test case sucessful for {value}')
