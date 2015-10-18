#class for food list and utilities
class FoodList(object):
    def __init__(self):
        self.__food_items = []
        self.__goal = 0
        pass

    #add FoodItem data object to array
    def add_food(self, m):
        self.__food_items.append(m)
        return m.name

    #create list of food items
    def create_list(self):
        output = ''
        for food in self.__food_items:
            output += "<article><p>" + str(food.quantity) + ' <strong>' + food.name + '</strong> for ' + str(food.calories * food.quantity) + ' calories</p></article>'
        return output

    #calculate total calories
    def total_calories(self, t):
        calories = 0
        result = ""
        for food in self.__food_items:
            calories += food.calories * food.quantity
        #if total calories is over daily goal, do this
        if calories > t:
            result = "<strong class='over'>" + str(calories - t) + "</strong> daily calories over your goal. Oops! :("
        #if total is under goal, do this
        elif calories < t:
            result = "<strong class='under'>" + str(t - calories) + "</strong> daily calories under your goal. Way to go! :D"
        #otherwise total is exactly the goal, so do this
        else:
            result = "<strong>exactly</strong> your daily goal. Niiiice! 8)"
        return "<div id='result'>Your total calories consumed today are " + str(calories) + " which is " + result + "</div>"

    @property
    def food_items(self):
        return self.__food_items

#food item class
class FoodData(object): #Data Object
    def __init__(self):
        self.__name = ""
        self.__calories = 0
        self.__quantity = 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, c):
        self.__calories = int(c)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, q):
        self.__quantity = int(q)
