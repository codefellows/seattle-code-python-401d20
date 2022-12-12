import shutil

from faker import Faker

fake = Faker('en_US')

potential_contacts = ""

existing_contacts = ""

###########################
# [Optional] explain what range is doing under the hood
###########################

# range_gen = range(100)

# print(type(range_gen))

# iterator = iter(range_gen)

# print(type(iterator))

# while True:

#     try:
#         i = next(iterator)
#     except StopIteration:
#         break

###########################

for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()

    potential_contacts += fake.paragraph()
    potential_contacts += " " + email + " "
    potential_contacts += fake.paragraph()
    potential_contacts += fake.ssn()
    potential_contacts += fake.sentence()
    potential_contacts += phone_number
    potential_contacts += fake.paragraph()

    if i % 7 == 0: # every now and then throw in a duplicate email
        potential_contacts += " " + email + " "
        potential_contacts + fake.sentence()

    if i % 9 == 0: # every now and then throw in a duplicate phone number
        potential_contacts += phone_number
        potential_contacts += fake.paragraph()


    if i % 5 == 0: # keep track of some "existing contacts" for the stretch goal
        existing_contacts += email + "\n"
        existing_contacts += phone_number + "\n"


    potential_contacts += "\n"

with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)

shutil.copy('potential-contacts.txt', '../../lab/assets/potential-contacts.txt')

# for stretch goal
with open("existing-contacts.txt", "w+") as f:
    f.write(existing_contacts)

shutil.copy('existing-contacts.txt', '../../lab/assets/existing-contacts.txt')




