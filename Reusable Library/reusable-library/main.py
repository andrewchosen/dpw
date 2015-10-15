import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        lib = FavoriteMovies()

        #movie title
        #year movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989 # calling function
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Teenage Mutant Ninja Turtles"
        md2.year = 1990 # calling function
        md2.director = "Some Guy"
        lib.add_movie(md2)


        p.body = lib.compile_list()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
