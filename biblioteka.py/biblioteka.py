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
        filmy = [i for i in self.full_list if str(type(i)) == "<class '__main__.Movie'>"]

        for i in self.full_list:
            if isinstance(i, Series):
                self.series_list.append(i)
                self.text_series_list.append(str(i))
            else:
                self.movie_list.append(i)
                self.text_movie_list.append(str(i))

        self.text_series_list.sort()
        self.text_movie_list.sort()
        print(self.text_series_list)
        print(self.text_movie_list)

    def search(self, title):
        return f"FilmSeriesList(title={self.title})"
    
    print(search)

class Movies: 
    def __init__ (self, title, year, species, plays):
        self.title = title
        self.year = year
        self.species = species
        self.plays = 0

    def __str__ (self):
        return f"{self.title} ({self.year})"

    # def __repr__(self):
    #     return f"Movies(title={self.title}, year={self.year}, species={self.species}, plays={self.plays})"

    def play(self, step = 1):
        self.plays += step

film1 = Movies(title = "Szeregowiec Ryan", year = "1998", species = "war drama", plays=0)
film2 = Movies(title = "Pierwszy człowiek", year = "2018", species = "biographical", plays=0)


class Series(Movies):
    def __init__(self, serie, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serie = serie
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.serie}E{self.episode}"

    # def __repr__(self):
    #     return f"Series(serie={self.serie}, episode{self.episode})"

serie1 = (Series(title = "Greys Anatomy", year = "2005", species = "comedy-drama", serie = "01", episode = "15", plays=0))
serie2 = Series(title = "Breaking Bad", year = "2008", species = "comedy", serie = "05", episode = "17", plays=0)


addition=FilmSeriesList()
addition.add(film1)
addition.add(film2)
addition.add(serie1)
addition.add(serie2)




