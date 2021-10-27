# Write a function called describe_city() that accepts the name of a city 
# and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.


def describe_city(city,country):
    print(f'{city} is located in the country of {country}')
describe_city('hadera','israel')