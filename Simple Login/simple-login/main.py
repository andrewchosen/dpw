'''
Name: Andrew Lancaster
Date: 10/6/2015
Class: DPW
Assignment: Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Initializing
        page = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
            <label>Name</label><input type="text" name="user" />
            <label>Email</label><input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
        '''
        self.response.write(page) # Print

#don't touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
