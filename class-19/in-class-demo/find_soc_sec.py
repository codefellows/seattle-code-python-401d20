import re

# context manager
with open("./text_with_soc_nums.txt", "r") as f:
    # we logic and stuff with the file f
    text_from_file = f.read()

# print(text_from_file)

# Same pattern as before:
pattern = r"(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}"

# re.findall() returns a list of matches
soc_sec_nums = re.findall(pattern, text_from_file)

# re.search() searches the entire string, but stops after the first
# soc_sec_nums = re.search(pattern, text_from_file).group()

# re.match() only looks at the beginning of the string
# soc_sec_nums = re.match(pattern, text_from_file).group()

print(soc_sec_nums)
