import random
import operator
from dataclasses import dataclass


full_list = []


class FilmSeriesList:
    def __init__(self):
        self.full_list = []
        self.movie_list = []
        self.series_list = []
        self.text_series_list=[]
        self.text_movie_list = []

    def add(self, movie):
        self.full_list.append(movie)

    def show_all(self):
        for i in self.full_list:
            print(i)

    def get_movies(self):
        output_list = []
        for i in self.full_list:
            if isinstance(i, Serial):
                pass
            else:
                output_list.append(i)
        output_list.sort(key=operator.attrgetter('title'))
        for i in output_list:
            print(i)


    def get_series(self):
        output_list = []
        for i in self.full_list:
            if isinstance(i, Serial):
                output_list.append(i)
        output_list.sort(key=operator.attrgetter('title'))
        for i in output_list:
            print(i)


    def search(self, title):
        movies = []
        for movie in self.full_list:
            if movie.title == title:
                print(str(movie))
        return movies


    def generate_views(self):
        full_list_item = random.choice(self.full_list)
        full_list_item.plays=random.randint(0, 100)
        return f"{full_list_item.title} {full_list_item.plays}"

    def generate_multiple(self):
        for i in range (10):
            FilmSeriesList.generate_views(self)

    def top_titles(self, quantity):

        self.full_list.sort(key=operator.attrgetter('plays'), reverse=True)
        for i in range (int(quantity)):
                    print (self.full_list[i])

class Movie:
    def __init__ (self, title: str, year: int, species: str, plays: int):
        self.title = title
        self.year = year
        self.species = species
        self.plays = plays

    def __str__ (self):
        return f"{self.title} {self.year} plays: {self.plays}"

    def play(self, step = 1):
        self.plays += step

film1 = Movie(title = "Saving Private Ryan", year = "1998", species = "war drama", plays=6)
film2 = Movie(title = "First Man", year = "2018", species = "biographical", plays=400)
film3 = Movie(title = "The Green Mile", year = "1999", species = "drama", plays = 0)

@dataclass
class Movie:
    title: str
    year: int
    species: str
    plays: int


class Serial(Movie):
    def __init__(self, serie: int, episode: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.title} S{self.serie}E{self.episode} plays: {self.plays}"

serie1 = Serial(title = "Greys Anatomy", year = "2005", species = "comedy-drama", serie = "1", episode = "15", plays = 0)
serie2 = Serial(title = "Breaking Bad", year = "2008", species = "comedy", serie = "5", episode = "17", plays = 0)
serie3 = Serial(title = "La Casa Del Papel", year = "2017", species = "thriller", serie = "3", episode = "7", plays = 0)

@dataclass
class Serial:
    title: str
    year: int
    species: str
    serie: str
    episode: int
    plays: int

library=FilmSeriesList()
library.add(film1)
library.add(film)
library.add(film3)
library.add(serie1)
library.add(serie2)
library.add(serie3)

# Dodatkowa funkcja w celu zwiększenia przejrzystości przeglądania i odnajdywania funkcji Biblioteki 
while True:
    print("available commands:\n\n1:show_all\n2:add\n3:get_movies\n4:get_series\n5:search\n6:generate_views\n7:top_titles\n8:run 10x generate_views\n")
    command = input("what would you like to do?")
    if command == "1":
        library.show_all()
        continue
    elif command =="2":
        library.add()
        continue
    elif command =="3":
        library.get_movies()
        continue
    elif command =="4":
        library.get_series()
        continue
    elif command =="5":
        command=input("what title to look for?")
        library.search(command)
        continue
    elif command =="6":
        print(library.generate_views())
        continue
    elif command =="7":
        command=input("how many top titles to return?")
        library.top_titles(command)
        continue
    elif command =="8":
        library.generate_multiple()
        continue

    else:
        print("invalid command!")

#print(library.search("Greys Anatomy"))
#print(library.generate_views(full_list_item))
