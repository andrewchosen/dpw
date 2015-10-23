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
            if self.request.GET['character'] == "daredevil":
                p = CharacterPage(d.characters[1])
            if self.request.GET['character'] == "iron-man":
                p = CharacterPage(d.characters[2])
            if self.request.GET['character'] == "wolverine":
                p = CharacterPage(d.characters[3])
            if self.request.GET['character'] == "magneto":
                p = CharacterPage(d.characters[4])
        else:
            p = HomePage()
        p.items = d.characters
        self.response.write(p.print_out())
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
