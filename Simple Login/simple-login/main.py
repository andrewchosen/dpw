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

        # if URL parameters exist
        if self.request.GET:
            # create NewUser with form info
            user = NewUser()
            user.first_name =  self.request.GET['first_name']
            user.last_name =  self.request.GET['last_name']
            user.gender = self.request.GET['gender']
            user.age = self.request.GET['age']
            user.status = self.request.GET['status']
            user.location = self.request.GET['location']

            # run render behavior from NewUser class to output HTML
            p.body = user.render()
        # if URL parameters do not exist(default page)
        else:
            # output form HTML into Page.body attribute
            p.body = """
        <form method="GET">
                <fieldset id="name">
                    <label for="first_name">First Name</label><input type="text" name="first_name" />
                    <label for="last_name">Last Name</label><input type="text" name="last_name" />
                </fieldset>
                <fieldset id="gender">
                    <label for="male">Male</label><input type="radio" name="gender" value="Male" />
                    <label for="female">Female</label><input type="radio" name="gender" value="Female" />
                </fieldset>
                <fieldset id="age">
                    <label for="age">Age</label><input type="number" name="age" min="13" max="150" />
                </fieldset>
                <fieldset id="status">
                    <label for="status">Relationship Status</label>
                    <select name="status">
                        <option value="Undisclosed">Undisclosed</option>
                        <option value="Single">Single</option>
                        <option value="Married">Married</option>
                        <option value="Divorced">Divorced</option>
                        <option value="Complicated">It's Complicated</option>
                    </select>
                </fieldset>
                <fieldset id="location">
                    <label for="location">Location</label><input type="text" name="location" />
                </fieldset>
                <input type="submit" value="Submit" />
        </form>
            """
        # print the HTML using print_out behavior from Page class
        self.response.write(p.print_out())

# Page class that stores sections of HTML to create a full page
class Page(object):
    def __init__(self):
        self.title = "Simple Form"
        self.main_css = "css/styles.css"
        self.reset_css = "css/reset.css"
        self.head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.reset_css}" rel="stylesheet" type="text/css" />
        <link href="{self.main_css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <section>
            <h1>{self.title}</h1>
        """
        self.body = ""
        self.close = """
        </section>
</body>
</html>
        """
    # function that prints out above html and formats it to take in **locals elements
    def print_out(self):
        all =  self.head + self.body + self.close
        all = all.format(**locals())
        return all

# class for creating a new user from form submissions
class NewUser(object):
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.gender = "N/A"
        self.age = 0
        self.status = "Undisclosed"
        self.location = "Everywhere"

    # render the html and return it to be called later
    def render(self):
        content = """
            <h2>{self.first_name} {self.last_name}</h2>
            <p><strong>Gender:</strong> {self.gender}</p>
            <p><strong>Age:</strong> {self.age} years old</p>
            <p><strong>Relationship Status:</strong> {self.status}</p>
            <p><strong>Location:</strong> {self.location}</p>
        """
        content = content.format(**locals())
        return content

#don't touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
