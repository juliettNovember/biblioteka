full_list = []

class Movies: 
    def __init__ (self, title, year, species, plays):
        self.title = title
        self.year = year
        self.species = species
        self.plays = 0

    def __str__ (self):
        return f"{title} ({year})"

    def __repr__(self):
        return f"Movies(title={self.title}, year={self.year}, species={self.species}, plays={self.plays})"

film1 = Movies(title = "Szeregowiec Ryan", year = "1998", species = "war drama", plays=0)
full_list.append(film1)

class Series(Movies):
    def __init__(self, serie, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serie = serie
        self.episode = episode

    def __str__(self):
        return f"{title} S{serie}E{episode}"

    def __repr__(self):
        return f"Series(serie={self.serie}, episode{self.episode})"

serie1 = Series(title = "Greys Anatomy", year = "2005", species = "comedy-drama", serie = "01", episode = "15", plays=0)
full_list.append(serie1)

def play(self, step = 1):
    self.plays += step


print(full_list)

    