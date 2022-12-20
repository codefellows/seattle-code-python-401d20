def say_hi(n):
    # base case
    if n <= 0:
        return    
    n = n - 1

    # do a thing
    print('hi')

    # invoke itself
    say_hi(n)


say_hi(2)
