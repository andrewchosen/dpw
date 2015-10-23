# Abstract class for pages
class Page(object):
    def __init__(self):
        self._title = "My Favorite Marvel Characters"
        self._css = "css/styles.css"
        self._js = "js/script.js"
        self._head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self._title}</title>
        <link href="{self._css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <header>
            <div class="container">
                <h1>{self._title}</h1>
            </div>
        </header>
        <section>
            <div class="container">
        """
        self._body = ""
        self._close = """
            </div>
        </section>
        <script language="javascript" type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script language="javascript" type="text/javascript" src="{self._js}"></script>
    </body>
</html>
        """
    # Function to combine all elements and print out page
    def print_out(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all

# Home page calculations and output
class HomePage(Page):
    def __init__(self):
        super(HomePage, self).__init__()

        # Navigation attributes
        self._nav_open = "<nav><ul>"
        self._nav_close = "</ul></nav>"
        self._nav_items = ""
        self.__items = []

    @property
    def items(self):
        pass

    # Create setter for pulling in navigation items from data
    @items.setter
    def items(self, arr):
        self.__items = arr
        # loop through data objects and use their .name attributes as links
        for item in arr:
            self._nav_items += "<li><a href='?character=" + item.url_code + "'>" + item.name + "</a></li>"

    # Override print_out function from super
    def print_out(self):
        all = self._head + self._body + self._nav_open + self._nav_items + self._nav_close + self._close
        all = all.format(**locals())
        return all
