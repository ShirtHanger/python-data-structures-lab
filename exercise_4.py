# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: 
# “I was born in <city>, <state> - population of <population>”

home_town = {
    'city': 'Morioh',
    'prefecture': 'Momoji',
    'country': 'japan',
    'population': 58713,
}

def hometown_info(home_town):
    home_town_message = f"My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of {home_town['city']}, within the {home_town['prefecture']} prefecture. I am one of {home_town['population']} citizens"
    return home_town_message
# Call the function and print the result
print('Exercise 4:', hometown_info(home_town))
