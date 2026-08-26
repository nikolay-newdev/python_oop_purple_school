def limit_args(max_value, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a, b = args
            if a <= max_value and b <= max_value:
                result = func(a, b)
                print(result)
                return result
            if a > max_value:
                if mode == "error":
                    raise ValueError('E')
                else:
                    a = max_value
            if b > max_value:
                if mode == "error":
                    raise ValueError('E')
                else:
                    b = max_value
            result = func(a, b)
            print(result)
            return result

            # x1 = a <= max_value
            # x2 = b <= max_value
            # if x1 and x2: 
            #     result = func(a, b)
            #     print(result)
            #     return result
            # elif not(x1 and x2) and mode == "error":
            #     raise ValueError('Error!')
            # else: 
            #     if (a <= max_value and b > max_value or a > max_value and b <= max_value) and mode == "clip":
            #         mn, mx = min(a, b), max(a, b)
            #         result = func(mn, max_value)
            #         print(result)
            #         return result
            #     else:
            #         result = func(max_value, max_value)
            #         print(result)
            #         return result

        return wrapper
    return decorator

@limit_args(max_value=10, mode="clip")
def multiply(a, b):
    return a * b

multiply(2, 3)
multiply(11, 11)
