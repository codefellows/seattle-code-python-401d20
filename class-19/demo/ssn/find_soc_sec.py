import re

# this file has been pre-generated with a bunch of text
# with 10 valid social security numbers spread throughout
with open("./text_with_soc_sec_nums.txt") as f:
    text_from_file = f.read()

pattern = r"(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}"

soc_sec_nums = re.findall(pattern, text_from_file)

print(soc_sec_nums)

assert len(soc_sec_nums) == 10

print(f"Found {len(soc_sec_nums)} social security numbers")
