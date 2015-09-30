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

print "-----------------------------------"

'''
#While Loop ---
i = 0
while i<9:
    print "The count is", i
    i = i+1

#For Loop ---
for i in range(0,10):
    print "The count is", i
    i = i+1

#For Each Loop ---
rappers = ["Tupac", "Nas", "Biggle Smalls"]

for r in rappers:
    # print "One of the best rappers is " + r
    pass

#Functions ---
x = 2

def calcArea(h, w):
    area = h * w
    return area + x
    # pass

a = calcArea(20, 40);
print "My area is " + str(a) + "sqft."
'''

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''

message = message.format(**locals())

print message