names = ["Chadwick Boseman", "Daniel Radcliffe", "Robert Downey Jr"]

inv = ("\nI, Humaid Abdulmajid would like to invite you to dinner at my Abode tomorrow evening, \nlooking forward to meeting your acquaintance.\n")

print("Dear " + names[0] + "." + inv)
print("Dear " + names[1] + "." + inv)
print("Dear " + names[2] + "." + inv)


print(names[0] + " is unavailable and cannot make it to dinner.\n\n")

names.insert(1, "Jimmy Fallon")
del names[0]

print("Dear " + names[0] + "." + inv)
print("Dear " + names[1] + "." + inv)
print("Dear " + names[2] + "." + inv)
