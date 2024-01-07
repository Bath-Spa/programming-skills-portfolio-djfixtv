# Dream destinations to visit
ptv = ["Tokyo", "Paris", "Canada", "New York City", "Italy"]

# Share the original order of places
print("Before any changes:", ptv)

# Print the list in alphabetical order without changing the original list
print("In Alphabetical Order:", sorted(ptv))

# Prove that the original order remains unchanged
print("Original Order is still:", ptv)

# Print the list in reverse alphabetical order without changing the original list
print("In Reverse Alphabetical Order:", sorted(ptv, reverse=True))

# Show that the original order is still intact
print("Original Order is still:", ptv)

# Reverse the order of the list and print
ptv.reverse()
print("Reversed Order:", ptv)

# Reverse the order again to get back to the original order
ptv.reverse()
print("Back to Original Order:", ptv)

# Sort the list in alphabetical order and print
ptv.sort()
print("In Alphabetical Order:", ptv)

# Sort the list in reverse alphabetical order and print
ptv.sort(reverse=True)
print("In Reverse Alphabetical Order:", ptv)
