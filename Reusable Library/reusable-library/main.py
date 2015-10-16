import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        food_list = FoodList()

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

        md3 = MovieData()
        md3.title = "Teenage Mutant Ninja Turtles II"
        md3.year = 1991 # calling function
        md3.director = "Some Guy"
        lib.add_movie(md3)

        if self.request.GET:
            p.body = "We have parameters!"
        else:
            p.body = "No Parameters found."

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
