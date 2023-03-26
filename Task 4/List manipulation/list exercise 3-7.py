guest_list = ['Albert Einstein', 'Isaac Newton', 'Marie Curie',
              'Charles Darwin', 'Nikola Tesla', 'Stephen Hawking']

print("Bad news! The dinner table won't arrive in time.")

while len(guest_list) > 2:
    cannot_attend = guest_list.pop()
    print(f"Sorry {cannot_attend}, I cannot invite you to the dinner.")

for guest in guest_list:

    print(f"Dear {guest}, you are still invited to the dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)
