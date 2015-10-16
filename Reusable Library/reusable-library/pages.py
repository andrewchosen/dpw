class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.__css = "css/styles.css"
        self.__head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.__body = ""
        self.__close = """
    </body>
</html>
        """

    @property
    def title(self):
        return self.__title

    @property
    def css(self):
        return self.__css

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, content):
        self.__body = content

    def print_out(self):
        all = self.__head + self.__body + self.__close
        all = all.format(**locals())
        return all
