# Logical Operators

Recall the three types of conditional statements we've covered in class: if, elif and else
We've used these to make our code run under certain circumstances. For example, if someone asks you if you're hungry, you may say yes, no, or respond in some other way

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

But what if you were asked two questions, and the repsonse was dependent on a combination of answers? We can use a **logical operators**
