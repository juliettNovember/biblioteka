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
        return output_list

    def get_series(self):
        output_list = []
        for i in self.full_list:
            if isinstance(i, Serial):
                output_list.append(i)
        return output_list      

    def search(self, title):
        movies = []
        for movie in self.full_list:
            if movie.title == title:
                movies.append(movie)
        return movies

class Movie: 
    def __init__ (self, title, year, species, plays):
        self.title = title
        self.year = year
        self.species = species
        self.plays = 0

    def __str__ (self):
        return f"{self.title} ({self.year})"

    def play(self, step = 1):
        self.plays += step

film1 = Movie(title = "Saving Private Ryan", year = "1998", species = "war drama", plays=0)
film2 = Movie(title = "First Man", year = "2018", species = "biographical", plays=0)
film3 = Movie(title = "The Green Mile", year = "1999", species = "drama", plays = 0)


class Serial(Movie):
    def __init__(self, serie, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serie = serie
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.serie}E{self.episode}"

serie1 = Serial(title = "Greys Anatomy", year = "2005", species = "comedy-drama", serie = "01", episode = "15", plays=0)
serie2 = Serial(title = "Breaking Bad", year = "2008", species = "comedy", serie = "05", episode = "17", plays=0)
serie3 = Serial(title = "La Casa Del Papel", year = "2017", species = "thriller", serie = "03", episode = "07", plays = 0)

addition=FilmSeriesList()
addition.add(film1)
addition.add(film2)
addition.add(film3)
addition.add(serie1)
addition.add(serie2)
addition.add(serie3)

print(addition.search("Greys Anatomy"))




