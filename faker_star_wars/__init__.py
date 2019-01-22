
from faker.providers import BaseProvider

from faker_star_wars.resources.films import FILMS
from faker_star_wars.resources.people import PEOPLE
from faker_star_wars.resources.planets import PLANETS
from faker_star_wars.resources.species import SPECIES
from faker_star_wars.resources.starships import STARSHIPS
from faker_star_wars.resources.vehicles import VEHICLES


class StarWars(BaseProvider):
    """
    A Faker provider for various entities from the Star Wars universe.
    """

    def planet(self):
        return self.random_element(PLANETS)

    def film(self):
        return self.random_element(FILMS)

    def person(self):
        return self.random_element(PEOPLE)

    def species(self):
        return self.random_element(SPECIES)

    def starship(self):
        return self.random_element(STARSHIPS)

    def vehicle(self):
        return self.random_element(VEHICLES)
