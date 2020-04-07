# for loops
for  letter in "Coffee": 
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for  friend in friends:
    print(friend)

friends = ["Jim", "Karen", "Kevin"]
for  index in range(10):
    print(index)

# building a guessing game 
secret_word ="giraffe"
guess = "" #guess variable
guess_count = 0 #tracks guesses
guess_limit = 3 #tracks limit
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): # as long not out of guesses and not secret word, keep looping
    if guess_count < guess_limit:
        guess = input("Enter guess: ") #everytime you guess, you incremet guess count
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses: # 2 scenarios you can end the game
    print("Out of Guesses, you lose ")
else:
     print ("You win!")

# while loop
    i = 1
while i<=10: 
    print(i)

# building a dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"

}

print(monthConversions["Jan"]) 
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv", "not a valid key"))

# A Better Calcluator 
num1 = float(input("Enter first #: "))
op = (input("Enter operator:"))
num2 = float(input("Enter second #: "))
if op = "+":
    print(num1 + num2)
elif op == "-"
    print(num1 - num2)
elif op == "/": 
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

#IF and ELSE, and comparisons
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a short male")
else:
    print("You are neither male or tall")

def maxnum (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2

#return 
def cube (num):
    return num*num*num
cube(3)

# functions 
def sayhi (name, age):
    print("Hello " + name + ", you are " + age)
sayhi("Mike", "35")
sayhi("Steve", "70")  


def cube (num):
    num*num*num
cube(3)

# tuples
coordinates = [(4, 5), (6,7), (3,4), (2, 9)]
print(coordinates)


# obtaining input from users to form a sentence 
name = input("Enter your name: ")
print ("Hello " + name + "!")
name = input("Enter your name: ")
age = input("Enter your age: ")
print ("Hello " + name + "! You are " + age + ".")

# building a basic calculator
num1 = input ("Enter a number: ")
num2 = float ("Enter another number: ")
result = num1 + num2
print(result)

# building a simple mad libs game 
colour = input("Enter a colour")
noun = input("Enter a plural noun")
cele = input("Enter a celebrity")

print("roses are " + colour + " ,")
print(noun + " are blue")
print("i love " +  cele)

# Working with Strings: Grabbing a range 1-3 of elements
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:3])

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

phrase = "Giraffe Academy"
print(phrase.upper().isupper())

phrase = "Giraffe Academy"
print(phrase + " is cool")

# List Functions Examples 
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "kelly")
print(friends)
