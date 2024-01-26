# 1. Decorator function syntax
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        # Some actions before execution of the original_fn
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        # Some actions after execution of the original_fn
        print("Function result:", result)
        print("Executed after function")

        return result

    return wrapper_function


@decorator_function
def my_function(a, b):
    print("This is my function!")
    return (a, b)


result = my_function(100, 50)
print(result)

# 2. Logging decorator function


def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result: {result}")
        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2))

print('')


@log_function_call
def sum(a, b):
    return a + b


print(sum(a=40.3, b=20.7))


# 3. Validate function arguments
def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float!")

        return fn(*args, **kwargs)

    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums([1, 2, 3], '2.0'))
    print(sum_nums(a=10.5, b='2.0'))
except ValueError as e:
    print(e)


# 4. Check User Authentication
def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Do some tasks only if user is authenticated
    print("Results of some sensitive tasks")


try:
    do_sensitive_job()
except Exception as e:
    print(e)
