def retry_deco(retry_max_count=1, exception_list=[]):
    def deco(fn):
        def wrapper(*args, **kwargs):
            print(f'run "{fn.__name__}"')
            print(f'with positional args = {args}, keyword kwargs = {kwargs}')

            attempt = 1
            max_attempts = retry_max_count + 1

            while attempt <= max_attempts:
                try:
                    result = fn(*args, **kwargs)
                    print(f'attempt = {attempt}, result = {result}')
                    return result
                except Exception as e:
                    if isinstance(e, tuple(exception_list)):
                        print(f'attempt = {attempt}, exception = {type(e).__name__}')
                        raise
                    print(f'attempt = {attempt}, exception = {type(e).__name__}')
                    if attempt == max_attempts:
                        raise
                    attempt += 1
        return wrapper
    return deco
