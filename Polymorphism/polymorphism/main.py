import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'],['last_name', 'text', 'Last Name'],['Submit', 'submit']]
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        '''

        self._body = 'My Page'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor function for super class
        #Page.__init__() <- one way to do it
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<label>First Name: </label><input type="text" value="" name="first_name" />
        #<label>Last Name: </label><input type="text" value="" name="last_name" />
        #<input type="submit" value="Submit" />

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change private inputs variable
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on info
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item..
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #otherwise.. end the tag
            except:
                self._form_inputs += '" />'
    #Polymorphism is here (overriding)
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
