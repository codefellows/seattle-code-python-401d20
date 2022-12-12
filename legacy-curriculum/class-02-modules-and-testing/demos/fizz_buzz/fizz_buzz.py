def fizz_buzz(num):
    """
    For number divisible by 3 return Fizz
    For number divisible by 5 return Buzz
    For number divisible by 5 and 3 return FizzBuzz
    All other numbers return the number
    """

    # if num % 3 == 0 and num % 5 == 0:
    #     return 'FizzBuzz'

    # if num % 3 == 0:
    #     return 'Fizz'

    # if num % 5 == 0:
    #     return 'Buzz'

    # return num

    word = ''

    if num % 3 == 0:
        word = 'Fizz'

    if num % 5 == 0:
        word += 'Buzz'

    return word or num

def fizz_buzz_sequence(nums):
    return [fizz_buzz(num) for num in nums]

def fizz_buzz_dict(nums):
    dict = {}
    for num in nums:
        dict[num] = fizz_buzz(num)
    return dict