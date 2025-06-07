# Name: Jose Da Silva, 06/06/25. Week1 Assignment: BeerBottles.py
# This code calls user to input the number of beer bottles available.
#  It then uses range function and for loop to count the number of
# beer bottlers to zero when it asks for more beer bottles to be purchased.

# It asks user for thenumber of beer bottles to be purchased.
Num_Bottles = int(input("Enter the number of bottles: "))

# The range function contains the starting point from the value user choses and decreases to zero by 1 unit every time.
for i in range(Num_Bottles, 0, -1):
    if i > 0:
        print(f"{i} Bottles of beer on the wall, {i} bottles of beer\n Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
else:
    # Once there i reaches zero, the else statement is called and prints the statements below.
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Time to buy more bottles of beer.")
print()

# Source: Reddit, r/lernpython: 99 Beers of Bottle Python Script.
# https://www.reddit.com/r/learnpython/comments/7qa5tp/99_beers_of_bottle_python_script/
