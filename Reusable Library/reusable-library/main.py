import webapp2
from library import FoodData, FoodList
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        food_list = FoodList()

        if self.request.GET:
            if self.request.GET['food_name1']:
                food1 = FoodData()
                food1.name =  self.request.GET['food_name1']
                food1.calories =  self.request.GET['calories1']
                food1.quantity = self.request.GET['quantity1']
                food_list.add_food(food1)

            if self.request.GET['food_name2']:
                food2 = FoodData()
                food2.name =  self.request.GET['food_name2']
                food2.calories =  self.request.GET['calories2']
                food2.quantity = float(self.request.GET['quantity2'])
                food_list.add_food(food2)

            if self.request.GET['food_name3']:
                food3 = FoodData()
                food3.name =  self.request.GET['food_name3']
                food3.calories =  self.request.GET['calories3']
                food3.quantity = float(self.request.GET['quantity3'])
                food_list.add_food(food3)

            if self.request.GET['food_name4']:
                food4 = FoodData()
                food4.name =  self.request.GET['food_name4']
                food4.calories =  self.request.GET['calories4']
                food4.quantity = float(self.request.GET['quantity4'])
                food_list.add_food(food4)

            if self.request.GET['food_name5']:
                food5 = FoodData()
                food5.name =  self.request.GET['food_name5']
                food5.calories =  self.request.GET['calories5']
                food5.quantity = float(self.request.GET['quantity5'])
                food_list.add_food(food5)

            if self.request.GET['food_name6']:
                food6 = FoodData()
                food6.name =  self.request.GET['food_name6']
                food6.calories =  self.request.GET['calories6']
                food6.quantity = float(self.request.GET['quantity6'])
                food_list.add_food(food6)

            calories = int(self.request.GET['daily_calories'])

            p.body += food_list.create_list() + "<br />" + food_list.total_calories(calories)
        else:
            p.body = """
            <form method="GET">
                    <fieldset id="food1">
                        <label for="food_name1">Name</label><input type="text" name="food_name1" />
                        <label for="calories1">Calories</label><input type="text" name="calories1" />
                        <label for="quantity1">Quantity</label><input type="text" name="quantity1" />
                    </fieldset>
                    <fieldset id="food2">
                        <label for="food_name2">Name</label><input type="text" name="food_name2" />
                        <label for="calories2">Calories</label><input type="text" name="calories2" />
                        <label for="quantity2">Quantity</label><input type="text" name="quantity2" />
                    </fieldset>
                    <fieldset id="food3">
                        <label for="food_name3">Name</label><input type="text" name="food_name3" />
                        <label for="calories3">Calories</label><input type="text" name="calories3" />
                        <label for="quantity3">Quantity</label><input type="text" name="quantity3" />
                    </fieldset>
                    <fieldset id="food4">
                        <label for="food_name4">Name</label><input type="text" name="food_name4" />
                        <label for="calories4">Calories</label><input type="text" name="calories4" />
                        <label for="quantity4">Quantity</label><input type="text" name="quantity4" />
                    </fieldset>
                    <fieldset id="food5">
                        <label for="food_name5">Name</label><input type="text" name="food_name5" />
                        <label for="calories5">Calories</label><input type="text" name="calories5" />
                        <label for="quantity5">Quantity</label><input type="text" name="quantity5" />
                    </fieldset>
                    <fieldset id="food6">
                        <label for="food_name6">Name</label><input type="text" name="food_name6" />
                        <label for="calories6">Calories</label><input type="text" name="calories6" />
                        <label for="quantity6">Quantity</label><input type="text" name="quantity6" />
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
