# A girl heads to a computer shop to buy some USB sticks.
# She loves USB sticks and wants as many as she can get for £50.
# They are £6 each.

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# Money = £50
# USB Sticks = £6

usb_sticks_bought=("The total amount of USB Sticks that were purchased are: ")
money_left="Total money that is left: "
print(usb_sticks_bought + str(int(50/6)))
print(money_left + str(50%6))   