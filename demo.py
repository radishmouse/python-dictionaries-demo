# demo code goes here
favorite_bars = [
    'Lloyds',
    'Manuels',
    'The Imperial'
]

best_item = [
    'Cheap bourbon',  # at Lloyd's
    'The Dogzilla',   # at Manuel's
    'Best staff ever' # The Imperial
]

day_least_crowded = [
    'Tuesday',
    'Wednesday',
]

print(f"At {favorite_bars[0]} they have a good {best_item[0]}")


# Dictionaries are collections of pairs of keys and values
# Keys are strings (99% of the time)
bars = {
    'Lloyds': 'Cheap bourbon',
    'Manuels': 'The Dogzilla',
    'The Imperial': 'Best staff ever!'
}

# Use the [] to look up information by the "key"
bars['Lloyds']
#'Cheap bourbon'
bars['Manuels']

# The .get() method will not raise an Exception if it can't find the key.
bars.get('Book House')
# You can pass the .get() method a second argument. This value will be 
# returned if it can't find the key.
bars.get('Book House', 'stuff')

##### How do I write useful dictionaries?
# How do I store multiple values for a single key?
bars = {
    'Lloyds': ['Cheap Bourbon', 'Tuesday']
    },
    'Manuels': ['The Dogzilla', 'Wednesday']
}
# Values can be lists! (Or numbers, or tuples, or anything)

# How do I store more complicated data for a single key?
# Nest your dictionaries!
bars = {
    'Lloyds': {
        'item': 'Cheap Bourbon',
        'day': 'Tuesday'
    },
    'Manuels': {
        'item': 'The Dogzilla',
        'day': 'Wednesday'
    },
    'The Imperial': {
        'item': 'Philly',
        'day': ['Tuesday', 'Friday']
        # Using a list because the days don't need individual labels
    }
}

places = {
    'US': {
        'Georgia': {
            'Atlanta': {
                'work': 'DigitalCrafts',
                'cats': ['Oakley', 'Milla']
            },
            'Nashville': {
                'lunch': 'Hattie B'
            },
            'Savannah': {
                'coffee': 'That place that time'
            }
        },
        'Tennessee': {
            'Nashville': {
                'lunch': 'Hattie B'
            }
        }
    },
    'Europe': {
        'Germany': {
            'Berlin': {
                'lunch': 'The Reichstag'
            },
            'Munich': {
                'snack': 'Hofbräuhaus'
            }
        }
    }
}


##### How do I access information in useful dictionaries?
# How do I access nested information?
# Use square brackets side by side (as you would with nested lists).
places['US']['Georgia']['Atlanta']['work']

# How do I access a list item in a nested dictionary?
places['US']['Georgia']['Atlanta']['cats'][0]

# How do I access an item in a dictionary in a list?
movies = [
    {
        'title': 'Avengers: End Game',
        'release date': '2019'
    },
    {
        'title': 'Avengers: Infinity dollars',
        'release date': '2018'
    }    
]

movies[1]['release date']

# How do I loop through lists of dictionaries?

charges = [
    {
        'vendor': 'Kula',
        'amount': 6.36
    },
    {
        'vendor': 'Kula',
        'amount': 9.11
    },
    {
        'vendor': 'Barnes and Noble',
        'amount': 16.49
    },
    {
        'vendor': 'Kula',
        'amount': 3.99
    },
    {
        'vendor': 'Lloyds',
        'amount': 50
    },            
]

# How do I loop through information in a dictionary?
# A for loop with a dictionary
# assigns the key string to the loop variable.
for city in ga_cities:
    print(ga_cities[city])

# Note: if you put quotes around `city`,
# python thinks you literally mean the key "city"
for city in ga_cities:
    print(ga_cities['city'])





# How do I find the highest charge?
highest = charges[0]
for charge in charges:
    if charge['amount'] > highest['amount']:
        highest = charge

# version #2
high_vendor = charges[0]['vendor']
highest = charges[0]['amount']
for charge in charges:
    if charge['amount'] > highest:
        highest = charge['amount']
        high_vendor = charge['vendor']





favorites = {}

##### How do I modify a dictionary?
# How do I store new values to an existing dictionary?
favorites['cat'] = 'Oakley'
favorites['ice cream'] = 'Butter Pecan'
favorites.update(bootcamp='DigitalCrafts')

# How do I update a value in an existing dictionary?
favorites['ice cream'] = 'Cookies and Cream'
favorites.update(cat='Milla')

# How do I remove value values from an existing dictionary?
del favorites['ice cream']

favorites['ice cream'] = ['Butter Pecan', 'Cookies and Cream']
del favorites['ice cream'][1]

favorites['cat'] = ''