from functools import wraps

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('emphasize')
        print('before calling original')
        orig_val =  f'{func(*args, **kwargs)}!!!'
        print('after calling orig')
        return orig_val

    return wrapper

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('sarcastic')
        orig_val = func(*args, **kwargs)
        return f'Sure, I\'d love to do "{orig_val}"'

    return wrapper


@emphasize
@sarcastic_decorator
def proclaim(txt):
    print('proclaim starting')
    return txt

if __name__ == "__main__":
    print(proclaim('spam is better than eggs'))
