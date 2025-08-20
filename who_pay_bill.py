import random

name_of_people = input("Enter the names of people (separated by spaces): ")

# Convert input into a list of names
name_of_people_list = name_of_people.split()

# Get a random index between 0 and (length of list - 1)
random_index = random.randint(0, len(name_of_people_list) - 1)

# Use that index to get the payer
payer = name_of_people_list[random_index]

print(f"{payer} will pay the bill!")


# or


name_of_people = input("Enter the names of people (separated by spaces): ")

# Convert the string into a list of names
name_of_people_list = name_of_people.split()  # Splits by spaces

# Pick a random person
payer = random.choice(name_of_people_list)

print(f"{payer} will pay the bill!")