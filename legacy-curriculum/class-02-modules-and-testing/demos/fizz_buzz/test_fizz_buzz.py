from fizz_buzz import fizz_buzz, fizz_buzz_sequence, fizz_buzz_dict

def test_one():
    expected = 1
    actual = fizz_buzz(1)
    assert expected == actual

def test_two():
    expected = 2
    actual = fizz_buzz(2)
    assert expected == actual

def test_three():
    expected = 'Fizz'
    actual = fizz_buzz(3)
    assert expected == actual

def test_four():
    expected = 4
    actual = fizz_buzz(4)
    assert expected == actual

def test_five():
    expected = 'Buzz'
    actual = fizz_buzz(5)
    assert expected == actual

def test_fifteen():
    expected = 'FizzBuzz'
    actual = fizz_buzz(15)
    assert expected == actual

def test_fizz_buzz_range():
    expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
    actual = fizz_buzz_sequence(range(1,15 + 1))
    assert expected == actual

def test_fizz_buzz_list():
    expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
    actual = fizz_buzz_sequence([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    assert expected == actual

def test_fizz_buzz_dict():
    expected = {
        1:1,
        2:2,
        3:'Fizz',
        4:4,
        5:'Buzz',
        15:'FizzBuzz'
    }

    actual = fizz_buzz_dict([1,2,3,4,5,15])

    assert expected == actual