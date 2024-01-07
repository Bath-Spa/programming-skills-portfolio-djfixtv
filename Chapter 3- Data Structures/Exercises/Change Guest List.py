names = ["Chadwick Boseman", "Daniel Radcliffe", "Robert Downey Jr"]

inv = ("\nI, Humaid Abdulmajid, would like to invite you to dinner at my Abode tomorrow evening, \nlooking forward to meeting your acquaintance.\n")

for name in names:
    print("Dear " + name + "." + inv)


unavailable_guest = names[0]
print(unavailable_guest + " is unavailable and cannot make it to dinner.\n\n")

names[0] = "Jimmy Fallon"

for name in names:
    print("Dear " + name + "." + inv)