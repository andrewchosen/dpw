import webapp2
from data import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        d = Data()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
