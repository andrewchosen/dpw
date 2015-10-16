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
            output += str(food.quantity) + ' ' + food.name + ' (' + str(food.calories * food.quantity) + ' total calories)<br />'
        return output

    #calculate total calories
    def total_calories(self):
        calories = 0
        result = ""
        for food in self.__food_items:
            calories += food.calories * food.quantity
        if calories > self.__goal:
            result = calories - self.__goal + " daily calories over your goal. Oops!"
        elif calories < self.__goal:
            result = self.__goal - calories + " daily calories under your goal. Way to go!"
        else:
            result = "exactly your daily goal. Niiiice!"
        return "Your total calories consumed today are " + str(calories) + " which is " + result

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
        self.__name = n

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, c):
        self.__calories = c

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, q):
        self.__quantity = q