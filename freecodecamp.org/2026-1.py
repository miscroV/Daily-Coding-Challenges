# Started on Day 8
def testFunc(func, cases: list, results:list) -> bool:
    """
    @brief runs the function with the provided case and result set and returns a success/fail value
    
    @param func, the function for testing
    @param cases, a list of the cases for a simple function
    @param results, a list of the return values the function should return for the corresponding case
    
    @return boolean value if the function passed all test cases. 
    """
    print("// running tests")
    Passed = True
    for case, result in zip(cases, results):
        if func(case) != result:
            Passed = False
            print(f"{func.__name__}({case}) should return {result}")
    print("// tests complted")
    return Passed


def is_sorted(arr):
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
    

            
cases = [
    [1,2,3,4,5],
    [10,8,6,4,2],
    [1,3,2,4,5],
    [3.14, 2.71, 1.61, 0.57],
    [12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9],
    [0.4, 0.5, 0.3]
]
results =[
    "Ascending",
    "Descending",
    "Not sorted",
    "Descending",
    "Ascending",
    "Not sorted"
]

if testFunc(is_sorted, cases, results): print(f"{is_sorted.__name__} passed testing")