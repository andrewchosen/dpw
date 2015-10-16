class FoodList(object):
    def __init__(self):
        self.__food_items = []
        pass

    #add FoodItem data object to array
    def add_food(self, m):
        self.__food_items.append(m)
        print m.title

    #create list of food items
    def create_list(self):
        output = ''
        for food in self.__food_items:
            output += food.quantity + ' ' + food.name + ' (' + str(food.calories * food.quantity) + ' total calories)<br />'
        return output

    #calculate total calories
    def total_calories(self):
        calories = 0
        for food in self.__food_items:
            calories += food.calories

    @property
    def food_items(self):
        return self.__food_items


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
        self.__year = n

    @property
    def calories(self):
        return self__calories = 0

    @calories.setter
    def calories(self, c):
        self.__calories = c

    @property
    def quantity(self):
        return self.__quantity = 1;

    @quantity.setter
    def quantity(self, q):
        self.__quantity = q