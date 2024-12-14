def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError: division by zero
    else:
        return 10 / x