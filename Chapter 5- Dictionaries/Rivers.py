# Define a dictionary of major rivers and the countries they run through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} is a major river that runs through {country}.")

# Loop to print the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.capitalize())

# Loop to print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
