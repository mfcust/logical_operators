# 1a) Copy and paste the 2nd block of code from the markdown file and run it below:










#Answer the questions below using comments (put a '#' symbol before your answer)
# 1b) What happens when you answer 'yes' to both questions?


# 1c) What happens when you answer 'no' to both questions?


# 1d) What happens when you answer 'yes' to one question and 'no' to the other question?


# 1e) What happens if you answer something random for both questions?


# 1f) What happens when you type something random for one question and 'no' for the other question?


# 1g) What happens if you type in something random for one question and 'yes' for the other question?


# 2) Uncomment the code below by removing the (''') from each side. Then, fill in the boolean expressions (conditions) for the if, elif and else statements below
#so that the print statements correctly inform you about variable x. For example, if x is greater than 10, your program should print "x is greater than 10!!"
#When you change the value of x, your program should print the correct statement telling you that x is either greater than 10, less than 0, in between 0 and 10,
#or not a number. HINT: Relational operators are ==, !=, <, >, >=, <=, and logical operators are and, or and not().

x = 10
'''
#use a relational operator to create your condition inside the parentheses
if ():
  print("x is greater than 10!!")
  
#use a relational operator to create your condition inside the parentheses
elif ():
  print("x is less than zero!!")

#use the logical operator 'and' to join two conditions inside the parentheses
elif ():
  print("x is a number between 0 and 10!!")
else:
  print("x is not a number!!")
'''



# 3) Uncomment the code below and input 3 conditions for each if and elif statements, and separate each with the 'or' logical operator.
# HINT: A condition separated by 'or' operators looks like this: variable_name == 'string' or variable_name == 'string2' or variable_name == 'string3'
#You can delete the hint comments inside the parentheses as well
'''
fave_food = input("What's your favorite food? ")

#Type 3 conditions separated by 'or' that specify your favorite foods inside the parentheses below
if ():
  print('I love ' + fave_food + " too!!!")
#Type 3 conditions separated by 'or' that specify your favorite foods inside the parentheses below
elif ():
  print("EW GROSS, I HATE " + fave_food + "!!!")
else:
  print("I guess " + fave_food + " is alright.")
'''



# 4) Uncomment the code below and wrap your entire boolean expression with the not() logical operator so that your print statement accurately describes the variable y.
#HINT: The print function should only execute if you change the value of y to a number that is either less than 0 or greater than 100
y = 100
'''
if y >= 0 and y <= 100:
  print("y is NOT a number between 0 and 100!!")
'''


# 5) We can have multiple logical operators to make even more complex conditions! Uncomment the code below, and inside the parentheses replace the comments
# for each if and elif statement by writing the appropriate python code for each condition. Use the hunger and time_of_day variables to do this.
#HINT: a potential condition in one set of parentheses can look like this: (hunger=='yes/no/maybe/whatever you want' and time_of_day=='breakfast/lunch/dinner/whatever you want')
######YOU MUST DELETE THE HINT COMMENTS IN EACH SET OF PARENTHESES IN ORDER FOR YOUR PROGRAM TO WORK######



hunger = input("Are you hungry? ")
time_of_day = input("Is it breakfast, lunch or dinner?")

if ('''if hungry AND breakfast''') or ('''if hungry AND dinner'''):
  print("It's time to eat!!")
  
elif ('''if hunger is no AND breakfast''') or ('''if hunger is no AND dinner'''):
  print("More food for me!!")
        
elif ('''if hungry AND not breakfast AND not dinner'''):
  print("Get yourself some lunch, or have a snack!!")
else:
  print("Sweet, let's go play outside!")




###---------------------------BONUS QUESTION---------------------------###

# 1) Write a program from scratch that asks the user two questions: "Is it raining?" and "Is it cold out?". Store those values as rain and cold.
#If it is raining and it's cold, print "Better wear your raincoat!" If it's raining but not cold, print "Don't forget your umbrella!" If it isn't raining and it
#is cold, print "Wear your warm jacket!" If it isn't raining and it isn't cold, print "It's a nice day, enjoy it! THEN if the user types in "secret password" 
#into the response for either question, print "You figured out the secret password!!!"



