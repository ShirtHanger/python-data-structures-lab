from exercise_4 import home_town

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following 
# format to home_town_items: "<key> = <value>"

def list_home_town_items(home_town):
    home_town_items = []
    
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items(home_town))
