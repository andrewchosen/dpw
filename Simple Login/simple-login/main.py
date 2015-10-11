'''
Name: Andrew Lancaster
Date: 10/6/2015
Class: DPW
Assignment: Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Initializing
        p = Page()
        self.response.write(p.print_out())
        # if self.request.GET:
        #     # store form info
        #     user =  self.request.GET['user']
        #     email =  self.request.GET['email']
        #     pass
        # else:
        #     pass

class Page(object):
    def __init__(self):
        self.title = "Simple Form"
        self.css = "css/styles.css"
        self.head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = """
        <form method="GET">
                    <label>Name</label><input type="text" name="user" />
                    <label>Email</label><input type="text" name="email" />
                    <input type="submit" value="Submit" />
        </form>
        """
        self.close = """
</body>
</html>
        """
    def print_out(self):
        all =  self.head + self.body + self.close
        all = all.format(**locals())
        return all

#don't touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
