def limit_args(max_value, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            numbers = []
            for arg in args:
                if arg > max_value and mode == "error":
                    raise ValueError('Error!')
                elif arg > max_value:
                    numbers.append(max_value)
                else:
                    numbers.append(arg)
            result = func(*numbers)
            print(result)
            return(result)               
        
            # a, b = args
            # if a <= max_value and b <= max_value:
            #     result = func(a, b)
            #     print(result)
            #     return result
            # if a > max_value:
            #     if mode == "error":
            #         raise ValueError('E')
            #     else:
            #         a = max_value
            # if b > max_value:
            #     if mode == "error":
            #         raise ValueError('E')
            #     else:
            #         b = max_value
            # result = func(a, b)
            # print(result)
            # return result

        return wrapper
    return decorator

@limit_args(max_value=10, mode="clip")
def multiply(a, b):
    return a * b

multiply(2, 3)
multiply(11, 11)
