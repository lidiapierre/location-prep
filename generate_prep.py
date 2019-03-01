# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

with_in_prep = "à"
with_of_prep = "de"


with open("location_data/countries") as myfile:
    countries = myfile.read().decode('utf8').lower().split('\n')

with open("location_data/departements") as myfile:
    depts = myfile.read().decode('utf8').lower().split('\n')


vowel = ["a","e","i","o","u"]

exception_islands = ["cuba", "madagascar", "malte", "taïwan"]
exception_masculine = ["mexique", "cambodge", "mozambique", "zimbabwe", "belize"]


class Place(object):
    def __init__(self, value):
        self.value = value.title()
        self.with_the_article = self.value
        self.with_in_prep = self.value
        self.with_of_prep = self.value


class Country(Place):

    def __init__(self, value):
        super(Country, self).__init__(value)
        self.populate()

    def populate(self):
        if self.value.lower() in exception_islands:
            self.with_in_prep = "à " + self.value
            self.with_of_prep = "de " + self.value
        if self.value.lower() in exception_masculine:
            self.with_in_prep = "au " + self.value
            self.with_the_article = "le " + self.value
            self.with_of_prep = "du " + self.value
        if self.value[0].lower() in vowel:
            self.with_the_article = "l'" + self.value
            self.with_of_prep = "de l'" + self.value
            if self.with_in_prep == self.value:
                self.with_in_prep = "en " + self.value
        elif self.value.endswith("e") and self.value.lower() not in exception_masculine:
            self.with_the_article = "la " + self.value
            self.with_of_prep = "de la " + self.value
            self.with_in_prep = "en " + self.value
        elif self.value.endswith("s"):
            self.with_the_article = "les " + self.value
            self.with_of_prep = "des " + self.value
            self.with_in_prep = "aux " + self.value
        elif self.with_in_prep == self.value:
                self.with_in_prep = "au " + self.value
                self.with_the_article = "le " + self.value
                self.with_of_prep = "du " + self.value


class Depts(Place):

    def __init__(self, value):
        super(Depts, self).__init__(value)

        self.with_in_prep = "en " + self.value
        self.with_of_prep = "de " + self.value

        if self.value.endswith("e"):
            self.with_the_article = "la " + self.value
        if self.value[0].lower() in vowel:
            self.with_the_article = "l'" + self.value
            self.with_of_prep = "de l'" + self.value


class City(Place):

    def __init__(self, value):
        super(City, self).__init__(value)

        self.with_in_prep = "à " + self.value
        self.with_of_prep = "de " + self.value

        if self.value.startswith("Le "):
            self.value = self.value[2:]
            self.with_in_prep = "au " + self.value
            self.with_of_prep = "du " + self.value


def process_fr_grammar(x, y):
    if len(y.split()) > 1 and y.split()[0] == "le":
        if x == with_in_prep:
            return "au {}".format(y.split[1])
        elif x == with_of_prep:
            return "du {}".format(y.split[1])
        else:
            return y
    
    

def generate_place_with_prep(input):
    # todo fuzzy matching
    # todo accept multiple entries
    if input.lower() in countries:
        place = Country(input)
    elif input.lower() in depts:
        place = Depts(input)
    else:
        place = City(input)

    return ", ".join([x for x in [place.with_in_prep, place.with_the_article, place.with_of_prep]])


if __name__ == '__main__':

    while True:
        place = raw_input("Où ça ? ").decode('utf8')
        print generate_place_with_prep(place)
