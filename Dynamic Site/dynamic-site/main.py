import webapp2
from data import Data
from pages import HomePage, ContentPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Create instance of Data object
        d = Data()
        # if URL parameters exist, find the page
        if self.request.GET:
            # call Spider-Man page
            if self.request.GET['character'] == "spiderman":
                p = ContentPage(d.characters[0])
            # call Daredevil page
            if self.request.GET['character'] == "daredevil":
                p = ContentPage(d.characters[1])
            # call Iron Man page
            if self.request.GET['character'] == "iron-man":
                p = ContentPage(d.characters[2])
            # call Wolverine page
            if self.request.GET['character'] == "wolverine":
                p = ContentPage(d.characters[3])
            # call Magneto page
            if self.request.GET['character'] == "magneto":
                p = ContentPage(d.characters[4])
        # if no URL parameters exist, call HomePage class
        else:
            p = HomePage()

        p.items = d.characters

        # print HTML
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
