def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return 10 / x
    except ZeroDivisionError:
        return float('inf')  # Or handle the error in a more appropriate way for your application
        # For instance, you might raise a custom exception or log the error and return a default value.