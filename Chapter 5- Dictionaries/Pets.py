# Define dictionaries representing different pets
pet1 = {'kind': 'cat', 'owner': 'Emily'}
pet2 = {'kind': 'ferret', 'owner': 'Jay'}
pet3 = {'kind': 'dog', 'owner': 'Shayne'}
pet4 = {'kind': 'parrot', 'owner': 'David'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"\nKind of animal: {pet['kind'].capitalize()}")
    print(f"Owner's name: {pet['owner'].capitalize()}")
