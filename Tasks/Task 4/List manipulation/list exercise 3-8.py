# List of 5 places to visit
places_to_visit = ["Bali", "Santorini", "Cape Town", "Tokyo", "Rio de Janeiro"]

# Print the list in its original order
print("Original list:")
print(places_to_visit)

# Print the list in alphabetical order without modifying the actual list
print("\nSorted list:")
print(sorted(places_to_visit))

# Show that the list is still in its original order
print("\nOriginal list is still the same:")
print(places_to_visit)

# Print the list in reverse alphabetical order without changing the original order
print("\nReverse sorted list:")
print(sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order
print("\nOriginal list is still the same:")
print(places_to_visit)

# Reverse the order of the list
places_to_visit.reverse()

# Print the list to show that its order has changed
print("\nReversed list:")
print(places_to_visit)

# Reverse the order of the list again to show that it's back to its original order
places_to_visit.reverse()

# Print the list to show that it's back to its original order
print("\nOriginal list is back:")
print(places_to_visit)

# Sort the list in alphabetical order
places_to_visit.sort()

# Print the list to show that its order has been changed
print("\nSorted list:")
print(places_to_visit)

# Sort the list in reverse alphabetical order
places_to_visit.sort(reverse=True)

# Print the list to show that its order has changed
print("\nReverse sorted list:")
print(places_to_visit)

# Create a list of items and use each function introduced in this chapter at least once
items_list = ["mountains", "rivers", "countries", "cities", "languages"]

# Print the length of the list using len()
print("\nNumber of items in the list:", len(items_list))

# Append a new item to the list using append()
items_list.append("foods")

# Remove an item from the list using remove()
items_list.remove("languages")

# Sort the list using sort()
items_list.sort()

# Reverse the order of the list using reverse()
items_list.reverse()

# Print the list
print("\nItems list:")
print(items_list)
