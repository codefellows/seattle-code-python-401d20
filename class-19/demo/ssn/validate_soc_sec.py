import re

# 665-06-4021
# that's a valid social security number
# but how can we verify that with code?

# while it is possible to do this the long way
# Regular Expressions were made for just such a task.

def validate(ssn):
    pattern = r"111-22-3333"
    pattern = r"\d\d\d-\d\d-\d\d\d\d"
    pattern = r"\d{3}-\d{2}-\d{4}"

    # https://www.geeksforgeeks.org/how-to-validate-ssn-social-security-number-using-regular-expression/
    pattern = r"^(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$"

    match_obj = re.match(pattern, ssn)

    return match_obj.group() if match_obj else None


goodies = ['111-22-3333']
baddies = ['666-22-3333', '000-22-3333', '900-22-3333', '555-00-3333', '111-222-3333']
questionables = ['1111-22-3333', '111-22-33333']  # extra leading or trailing number

for ssn in goodies:
    assert validate(ssn)

for ssn in baddies:
    assert not validate(ssn)

for ssn in questionables:
    assert not validate(ssn)

print("TESTS PASSED")
