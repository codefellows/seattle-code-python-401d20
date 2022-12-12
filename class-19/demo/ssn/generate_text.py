from random import shuffle
from faker import Faker

fake = Faker()

texts = [fake.text() for _ in range(10)]

nums = [fake.ssn() for _ in range(10)]

bad_nums = ["666-01-1234","665-00-1234","901-01-1234"]

addresses = [fake.address() for _ in range(10)]

content = texts + nums + bad_nums + addresses

shuffle(content)

text_with_soc = " ".join(content)

with open("./text_with_soc_sec_nums.txt", "w") as f:
  f.write(text_with_soc)


