#one line comment
'''
Doc strings

'''

first_name = "Kermit"
last_name = "De Frog"

# response = raw_input("Enter your name   ")
# print "Hello there, ", response

birth_year = 1985
current_year = 2015
age = current_year - birth_year
# print "You are " + str(age) + " years old."

budget = 200

if budget > 100:
    #stuff to do
    brand = "Nike"
    print "Yay, I can get some " + brand + " shoes."
elif budget > 50:
    # print "We can at least get some generic sneakers."
    pass
else:
    # print "No shoes for me."
    pass

characters = ["Leia", "Luke", "Chewy", "Lando"]
characters.append("Obi Wan")
# print characters
# print characters[0]

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
print movies["Star Wars"]