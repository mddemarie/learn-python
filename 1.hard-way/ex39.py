# create a mapping of state to abbreviation

states = {
	'Czech Republic' : 'CZ',
	'Germany' : 'GE',
	'Poland' : 'PL',
	'Slowakia' : 'SK',
	'Austria' : 'AT'
}

# create a basic set of states and some cities in them
cities = {
	'CZ' : 'Prague',
	'GE' : 'Berlin',
	'AT' : 'Vienna'
}

# add some more cities
cities['PL'] = 'Warsawa'
cities['SK'] = 'Bratislava'

# print out some cities
print('-' * 10)
print("CZ State has: ", cities['CZ'])
print("GE State has: ", cities['GE'])

# print some states
print('-' * 10)
print("Poland's abbreviation is: ", states['Poland'])
print("Slowakia's abbreviation is: ", states['Slowakia'])

# do it by using the state then cities dict
print('-' * 10)
print("Austria has: ", cities[states['Austria']])
print("Czech Republic has: ", cities[states['Czech Republic']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
	print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
	print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('United Kingdom')

if not state:
	print("Sorry, no UK.")

# get a city with a default value
city = cities.get('UK', 'Does Not Exist')
print("The city for the state 'UK' is: %s" % city)
