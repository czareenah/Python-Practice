#Let's display a fortune

import random

daily_number = random.randint(1,100)

fortune_number = random.randint(1,10)

fortune_text = ''

if fortune_number == 1:
    fortune_text = "Anything you do, do it well. The last thing you want is to be sorry for what you didn't do."

if fortune_number == 2:
    fortune_text = "Today it's up to you to create the peacefulness you long for."

if fortune_number == 3:
    fortune_text = "A friend asks only for your time not your money."

if fortune_number == 4:
    fortune_text = "Change can hurt, but it leads a path to something better."

if fortune_number == 5:
    fortune_text = "A dream you have will come true."

if fortune_number == 6:
    fortune_text = "You already know the answer to the questions lingering inside your head."

if fortune_number == 7:
    fortune_text = "Serious trouble will bypass you."

if fortune_number == 8:
    fortune_text = "You will travel to many exotic places in your lifetime."    

if fortune_number == 9:
    fortune_text = "Its amazing how much good you can do if you dont care who gets the credit."    

if fortune_number == 10:
    fortune_text = "The greatest risk is not taking one."    

print(f'{fortune_text} Your Daily Number is: {daily_number}')