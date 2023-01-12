import re

# 123-11-0033
# this is possibly a valid social security number
# but how can we validate this ssn?
# ! if it matches the format!


def validate(ssn):
    """
    Uses regex to validate a social security number.

    :param ssn: string of integers
    :return: boolean
    """

    # thank you https://www.geeksforgeeks.org/how-to-validate-ssn-social-security-number-using-regular-expression/
    pattern = r"^(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$"  # regex pattern

    # could be None or a match group
    match_obj = re.match(pattern, ssn)

    if match_obj:
        return True
    else:
        return False


# List of good ssns
goodies = ["111-22-3333", "856-45-0002"]

# List of bad ssns
baddies = ["666-22-1111", "000-22-1111", "900-44-5500"]


if __name__ == "__main__":
    for ssn in goodies:
        assert validate(ssn)

    for ssn in baddies:
        assert not validate(ssn)

    print("TESTS PASSED")
