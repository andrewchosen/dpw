class Page(object):
    def __init__(self):
        self.__title = "Calorie Calculator"
        self.__css = "css/styles.css"
        self.__js = "js/script.js"
        self.__head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link href='https://fonts.googleapis.com/css?family=Roboto+Condensed:400,700,300' rel='stylesheet' type='text/css'>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <header>
            <div class="container">
                <h1>{self.title}</h1>
            </div>
        </header>
        <section>
            <div class="container">
            <div id="error" style="display:none;"></div>
        """
        self.__body = ""
        self.__close = """
            </div>
        </section>
        <script language="javascript" type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script language="javascript" type="text/javascript" src="{self.js}"></script>
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
    def js(self):
        return self.__js

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
