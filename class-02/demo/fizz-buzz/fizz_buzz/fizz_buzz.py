def fizz_buzz(num):
    """
    For number divisible by 3 return Fizz
    For number divisible by 5 return Buzz
    For number divisible by 5 and 3 return FizzBuzz
    All other numbers return the number as string
    """

    if not num % 15:
        return 'FizzBuzz'

    if not num % 3:
        return 'Fizz'

    if not num % 5:
        return 'Buzz'

    return str(num)


def fiz_buzz_alternate(num):
    word = ''

    if num % 3 == 0:
        word = 'Fizz'

    if num % 5 == 0:
        word += 'Buzz'

    return word or num


def fizz_buzz_sequence(nums):
    # sequence = []
    # for num in nums:
    #     converted = fizz_buzz(num)
    #     sequence.append(converted)

    # return sequence

    return [fizz_buzz(num) for num in nums]

def fizz_buzz_dict(nums):
    dict = {}
    for num in nums:
        dict[num] = fizz_buzz(num)
    return dict
