class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        pass
    #some way to add to array of movies
    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title

    #generate a list of movies
    def compile_list(self):
        output = ''
        for movie in self.__movie_list:
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ')<br />'
        return output

    #calculate time span between movies
    def calc_time_span(self):
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        #sort years from low to high
        years.sort()

        #subtract low year from high
        num = len(years) - 1
        span = years[num] - years[0]
        return 'The span of films entered is ' + str(span) + ' years.'



class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 # check for valid year
        self.director = ''
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y): #if date is invalid
        if y > 2015:
            print "Error: Invalid date!"
            self.__year = 2015
        else:
            self.__year = y