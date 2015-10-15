class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        pass
    #some way to add to array of movies
    def addMovie(self, m):
        self.__movie_list.append(m)
        print m.title

        #generate a list of movies
        #calculate time span between movies


class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 # check for valid year
        self.director = ''
    @property
    def year(self):
        pass

    @year.setter
    def year(self, y): #if date is invalid
        if y > 2015:
            print "Error: Invalid date!"
            self.__year = 2015
        else:
            self.__year = y