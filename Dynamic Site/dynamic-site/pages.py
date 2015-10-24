# Abstract class for pages
class Page(object):
    def __init__(self):
        self._title = "My Top 5 Marvel Characters"
        self._page_title = self._title
        self._css = "css/styles.css"
        self._js = "js/script.js"
        self._head = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self._title}</title>
        <link href='https://fonts.googleapis.com/css?family=Arimo:400,700' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Fjalla+One' rel='stylesheet' type='text/css'>
        <link href="{self._css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <header>
            <div class="container">
                <h1><a href="/">{self._page_title}</a></h1>
            </div>
        </header>
        <section>
            <div class="container">
        """
        self._body = ""
        self._close = """
            </div>
        </section>
        <footer>
            <div class="container">
                <p>&copy; 2015</p>
            </div>
        </footer>
        <script language="javascript" type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script language="javascript" type="text/javascript" src="{self._js}"></script>
    </body>
</html>
        """
        # Navigation attributes
        self._nav_open = "<nav><ul>"
        self._nav_close = "</ul></nav>"
        self._nav_items = ""
        self.__items = []

    # getter for navigation items
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

    # Function to combine all elements and print out page
    def print_out(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all
        
    def image(self):
        return "<div id='img-col'><img src='images/placeholder.jpg' /></div>"

# Home page calculations and output
class HomePage(Page):
    def __init__(self):
        super(HomePage, self).__init__()
        self._body = """
                <article>Since my childhood, I, like most children, have followed and loved Marvel comics. From reading the comic books, watching the cartoons, and eventually freaking out over every real life action movie released, I have witnessed most of the characters that Stan Lee and his partners have created. I honestly can't think of a character I don't like, heroes or villains, which makes picking just five of my favorites very difficult. However, these are the ones I came up with so enjoy! Debate! Fight! Just don't hurt me, please.</article>
                """
    
    # Override print_out function from super
    def print_out(self):
        all = self._head + self._nav_open + self._nav_items + self._nav_close + self._body + self._close
        all = all.format(**locals())
        return all

# Character page class
class ContentPage(Page):
    def __init__(self, obj):
        super(ContentPage, self).__init__()
        self._title = obj.name + " - " + self._title
        self._char_open = "<article id='" + obj.url_code + "'>"
        self._char_close = "</ul></div></article>"
        self._char_details = "<div id='info-col'><h2>" + obj.name + "</h2>"
        self._char_details += "<p>" + obj.description + "</p>"
        self._char_details += "<ul>"
        self._char_details += "<li><strong>Real Name: </strong>" + obj.real_name + "</li>"
        self._char_details += "<li><strong>Alignment: </strong>" + obj.alignment + "</li>"
        self._char_details += "<li><strong>Height: </strong>" + obj.height + "</li>"
        self._char_details += "<li><strong>Weight: </strong>" + obj.print_weight() + "</li>"
        self._char_details += "<li><strong>Powers: </strong>" + obj.powers + "</li>"
        
    def image(self):
        return = "<div id='img-col'><img src='images/" + obj.url_code + ".jpg' alt='" + obj.name + "'/></div>"

    # override print_out() for character pages
    def print_out(self):
        all = self._head + self._nav_open + self._nav_items + self._nav_close + self._body + self._char_open + image() + self._char_details + self._char_close + self._close
        all = all.format(**locals())
        return all
