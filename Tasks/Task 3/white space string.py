# Store the person's name with whitespace characters
name = "\t\n  Eric\t\n "

# Print the name once, with the whitespace characters displayed
print(f"Name with whitespace: '{name}'")

# Strip the whitespace from the name using lstrip(), rstrip(), and strip()
name_lstrip = name.lstrip()
name_rstrip = name.rstrip()
name_strip = name.strip()

# Print the stripped names
print(f"Name stripped with lstrip(): '{name_lstrip}'")
print(f"Name stripped with rstrip(): '{name_rstrip}'")
print(f"Name stripped with strip(): '{name_strip}'")
