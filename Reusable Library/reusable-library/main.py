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
            p.body = food_list.create_list() + "<br />" + food_list.total_calories()
        else:
            p.body = """
        <form method="GET">
                <fieldset id="food1">
                    <label for="food_name">Name</label><input type="text" name="food_name" />
                    <label for="calories">Calories</label><input type="text" name="calories" />
                    <label for="quantity">Quantity</label><input type="text" name="quantity" />
                </fieldset>
                <fieldset id="total">
                    <label for="daily_calories">Daily Calorie Goal</label><input type="text" name="daily_calories" />
                </fieldset>
                <button type="submit">Calculate</button>
        </form>
            """
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
