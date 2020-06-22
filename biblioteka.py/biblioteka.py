class Movies: 
    def __init__ (self, title, year, species, plays):
        self.title = title
        self.year = year
        self.type = species
        self.plays = plays

class Series(Movies):
    def __init__(self, serie, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serie = serie
        self.episode = episode

