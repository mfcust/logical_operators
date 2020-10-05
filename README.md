# Logical Operators

Recall the three types of conditional statements we've covered in class: if, elif and else. We've used these to make our code run under certain circumstances. For example, if someone asks you if you're hungry, you may say "yes", "no", or respond in some other way.

If you are hungry  
  Say "Great, I have some food for you!"  
Else if you are not hungry  
  Say "Ok, I'll put your food in the fridge."  
Else  
  Say "Sorry, did you hear me? I asked you if you were hungry. Yes or no?"  
  
Coding this exchange in Python would look something like this:

```
hungry = input("Are you hungry? ")

if hungry == "yes":
  print("Great, I have some food for you!")
elif hungry == "no":
  print("Ok, I'll put your food in the fridge.")
else:
  print("Sorry, did you hear me? I asked you if you were hungry. Yes or no?")
```

But what if you were asked two questions, and the response was dependent on a combination of answers? We can use **logical operators** to make more complex conditions. For example, what it the response was dependent on your answers to two questions: "Are you hungry?" and "Did you finish your homework?" You can respond yes, no, or something else for both questions. Here's what it your the responses could look like in English:

If you're hungry AND you finished your hw:  
  Say "Great! Here's dinner and you get a big dessert because you finished all of your homework!"  
Else if you're hungry OR you finished your hw:  
  Say "Here's dinner!"  
Else if you're not hungry AND you didn't finish your hw:  
  Say "Well then keep working on your hw! I'll put your dinner in the fridge until you're ready!"  
Else if you don't respond yes or no to either question  
  Say "Did you not hear my questions? Try answering yes or no in all lower case letters!"  
Else  
  Say "Answer both of my questions seriously this time!"  

Now what does this scenario look like using Python code? Observe below:
```
hungry = input("Are you hungry? ")
hw = input("Did you finish your homework? ")

if hungry == 'yes' and hw == 'yes':
  print("Great! Here's dinner and you get a big dessert because you finished all of your homework!")
elif hungry =='yes' or hw =='yes':
  print("Here's dinner!")
elif hungry =='no' and hw == 'no':
  print("Well then keep working on your hw! I'll put your dinner in the fridge until you're ready!")
elif not(hungry == 'yes' or hungry == 'no' or hw == 'yes' or hw == 'no'):
  print("Did you not hear my questions? Try answering yes or no in all lower case letters!")
else:
  print("Answer both of my questions seriously this time!")
```
Here we are introduced to the logical operators AND, OR and NOT()
For AND, both conditions on either side of AND need to be TRUE for the code inside the if/elif statement to run.
For OR, either one of the conditions on either side of OR need to be TRUE for the code inside the if/elif statement to run. It's ok if one of them is false.
For NOT(), the condition inside the parentheses needs to be FALSE for the code to run.

Try copying and pasting the code above into your .py file, and change your responses to the answers to see what happens!
