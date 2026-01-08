# Started on Day 8
from testing import testFunc

def is_sorted(arr):
    """ Jan-8
    Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

    If the given array is:

    In ascending order (lowest to highest), return "Ascending".
    In descending order (highest to lowest), return "Descending".
    Not sorted in ascending or descending order, return "Not sorted".
    """
    is_acc = True
    is_des = True
    for i in range(1, len(arr)):
        if not (arr[i] > arr[i-1]): is_acc = False
        if not (arr[i] < arr[i-1]): is_des = False

    if is_acc:
        return "Ascending"
    elif is_des:
        return "Descending"
    else:
        return "Not sorted"

# UNIT TESTING      
# cases = [
#     [1,2,3,4,5],[10,8,6,4,2],[1,3,2,4,5],[3.14, 2.71, 1.61, 0.57],
#     [12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9],[0.4, 0.5, 0.3]
# ]
# results =[
#     "Ascending","Descending","Not sorted","Descending",
#     "Ascending","Not sorted"
# ]
# if testFunc(is_sorted, cases, results): print(f"{is_sorted.__name__} passed testing")