# faker_star_wars
Star Wars data for use with Python's [Faker](https://github.com/joke2k/faker) package.


## Install
Coming soon.

## Usage
```python
>>> from faker import faker
>>> from faker_star_wars import StarWars
>>> fake = Faker()
>>> fake.add_provider(StarWars)
>>>
>>> fake.planet()
'Geonosis'
>>> fake.vehicle()
'Sith Speeder'
>>> fake.person()
'Kit Fisto'
```

## Attributions
- Thank you to the [Faker](https://github.com/joke2k/faker) package for existing and making my life easier.
- Special thanks to the [SWAPI - The Star Wars API](https://github.com/phalt/swapi) for the information used in this package. Please consider [donating](https://swapi.co/) to this project.
- Thanks to [swapi-python](https://github.com/phalt/swapi-python) for making it easier to pull down the information from SWAPI that is used in this package.

# License
MIT
