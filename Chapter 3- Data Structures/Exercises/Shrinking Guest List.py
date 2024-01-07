names = ["Chadwick Boseman", "Daniel Radcliffe", "Robert Downey Jr"]

inv = ("\nI, Humaid Abdulmajid, would like to invite you to dinner at my Abode tomorrow evening, \nlooking forward to meeting your acquaintance.\n")

# Initial invitations
for name in names:
    print("Dear " + name + "." + inv)

# Handle unavailable guest
unavailable_guest = names.pop(0)
print(unavailable_guest + " is unavailable and cannot make it to dinner.\n\n")

# Insert replacement guest
names.insert(0, "Jimmy Fallon")

# Second round of invitations
for name in names:
    print("Dear " + name + "." + inv)

print("Sorry, I can only invite two people for dinner.\n")

# Handle uninvited guests
for _ in range(len(names) - 2):
    removed_guest = names.pop()
    print("Sorry, " + removed_guest + ", I can't invite you to dinner.")

# Congratulate remaining guests
for name in names:
    print("\nCongratulations, " + name + ", you're still invited to dinner!\n" if len(names) > 0 else "No one left to invite.")

# Clear the list
del names[:]

print("Empty guest list:", names)
