import webapp2
from library import FoodData, FoodList
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        food_list = FoodList()

        #add food item for testing
        food1 = FoodData()
        food1.name = "Bananas"
        food1.calories = 20
        food1.quantity = 3
        food_list.add_food(food1)

        food2 = FoodData()
        food2.name = "Apples"
        food2.calories = 200
        food2.quantity = 3
        food_list.add_food(food2)

        if self.request.GET:
            p.body = "We have parameters!"
        else:
            p.body = food_list.create_list() + "<br />" + food_list.total_calories()

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
