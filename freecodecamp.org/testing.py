def testFunc(func, cases: list, results:list) -> bool:
    """
    @brief runs the function with the provided case and result set and returns a success/fail value

    @param func, the function for testing
    @param cases, a list of the cases for a simple function
    @param results, a list of the return values the function should return for the corresponding case
    
    @return boolean value if the function passed all test cases. 

    """
    print(f"// running tests: \"{func.__name__}\"")
    Passed = True
    for case, result in zip(cases, results):
        if func(case) != result:
            Passed = False
            print(f"{func.__name__}({case}) should return {result}")
    print("// tests completed\n")
    return Passed