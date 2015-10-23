import webapp2
from data import Data
from pages import HomePage, CharacterPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Create instance of Data object
        d = Data()
        if self.request.GET:
            if self.request.GET['character'] == "spiderman":
                p = CharacterPage(d.characters[0])
        else:
            p = HomePage()
        p.items = d.characters
        self.response.write(p.print_out())
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
