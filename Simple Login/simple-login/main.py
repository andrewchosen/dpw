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

        if self.request.GET:
            # store form info
            user =  self.request.GET['user']
            email =  self.request.GET['email']
            p.body = "<p>" + user + " " + email + "</p>"
        else:
            p.body = """
        <form method="GET">
                    <fieldset id="name">
                        <label for="first_name">First Name</label><input type="text" name="first_name" />
                        <label for="last_name">Last Name</label><input type="text" name="last_name" />
                    </fieldset>
                    <fieldset id="gender">
                        <label for="male">Male</label><input type="radio" name="gender" value="male" />
                        <label for="female">Female</label><input type="radio" name="gender" value="female" />
                    </fieldset>
                    <fieldset id="age">
                        <label for="age">Age</label><input type="number" name="age" min="13" max="150" />
                    </fieldset>
                    <fieldset id="status">
                        <label for="status">Relationship Status</label>
                        <select name="status">
                            <option value="undisclosed">Undisclosed</option>
                            <option value="single">Single</option>
                            <option value="married">Married</option>
                            <option value="divorced">Divorced</option>
                            <option value="complicated">It's Complicated</option>
                        </select>
                    </fieldset>
                    <fieldset id="location">
                        <label for="location">Location</label><input type="text" name="location" />
                    </fieldset>
                    <input type="submit" value="Submit" />
        </form>
        """

        self.response.write(p.print_out())

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
        self.body = ""
        self.close = """
</body>
</html>
        """
    def print_out(self):
        all =  self.head + self.body + self.close
        all = all.format(**locals())
        return all

class NewUser(object):
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.gender = "N/A"
        self.age = 0
        self.status = "Undisclosed"
        self.location = "Everywhere"

#don't touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
