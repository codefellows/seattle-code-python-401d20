numerals = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1,
}

def to_arabic(roman_numeral):

    roman_numeral = roman_numeral.upper()

    value = 0

    for i in range(len(roman_numeral) - 1):
        current_char = roman_numeral[i]
        current_char_val = numerals[current_char]
        next_char = roman_numeral[i+1]
        next_char_val = numerals[next_char]

        if next_char_val > current_char_val:
            value -= current_char_val
        else:
            value += current_char_val

    last_char = roman_numeral[-1]
    last_char_val = numerals[last_char]

    value += last_char_val

    return value





