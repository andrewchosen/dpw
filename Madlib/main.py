'''
drink function
    for drink_number times:
            {person_one} drinks a drink.

{person_one} walks into a bar. They ask the bartender for {drink_number} drinks.

if drink_number is 3 or more:
    {person_two} says, "Listen, {person_one}, that is {a_or_an} {adjective_one} amount of drinks to order."
    {person_one} replies, "Don't be such a {adjective_two} {animal}, {person_two}. One is for me, and the other {leftover} drinks are for my other personalities."
    drink function

elif drink_number is 2:
    {person_two} says, "Who's the other drink for?"
    {person_one} replies, "It's for my other personality, you {adjective_two} {animal}."
    drink function

else:
    {person_two} says, "{person_one}, what about your other personalities? What will they drink?"
    {person_one} replies, "They've been {adjective_two} {animal}s. They don't deserve to drink."
    {person_one} drinks the drink.

{person_two} says, "Well okay then. When you're done, we should {action} the {animal_two} while it's still early."
{person_one} responds, "You're on! Let me just order {drink_number_two} more drinks and I'll be ready to {verb_two}!"

if drink_number_two is more than 1 {
    "Are you kidding?? That is {drink_total} drinks! You're going to be sick!" {person_two} exclaims.
    "My other personalities, man! Don't listen to {person_two}, {random_name}. They don't mean it. We've known each other since I was {person_one_age} years old."
else
    "I guess one more wouldn't hurt. Heck, order me one, too!" {{person_two}} says."


'''

# User prompts
person_one = raw_input("Choose a name:   ")
person_two = raw_input("Choose another name:   ")
drink_number_one = raw_input("Choose a number between 1 and 10:   ")
drink_number_two = raw_input("Choose another number between 1 and 10:   ")
adjective_one = raw_input("Choose an adjective:   ")
adjective_two = raw_input("Choose another adjective:   ")
animal = raw_input("Choose an animal(singular):   ")
action = raw_input("Choose an action verb:   ")
animal_two = raw_input("Choose an animal(plural):   ")
