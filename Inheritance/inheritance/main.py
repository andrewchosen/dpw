#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'],['last_name', 'text', 'Last Name'],['Submit', 'submit']]
        self.response.write(p.print_out_form())

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

    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
