# create dictionary using expression
# replace for loops and lambda functions

# basic syntax to write dictionaries:- 
# ditionary={key: expression for (key, value) in iterable}

citiesInF={"New York":32, "Boston":75, "Chicago":50}                                # city and their temp in F

cities_in_C={key: round((value-32)*(5/9)) for (key, value) in citiesInF.items()}    # new dictionary for converted in C

print(cities_in_C)


weather={"Mumbai":"humid", "Delhi":"Polluted", "Vishakhapatnam":"Sunny"}
sunnyWeather={key:value for (key, value) in weather.items() if value=="Sunny"}      # this stores only SUNNY ones

print(sunnyWeather)