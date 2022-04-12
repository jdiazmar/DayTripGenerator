starting_point = "Welcome to Day Trip Generator"
print(starting_point)

import random
from tkinter.messagebox import YES

destinations_list = ['New York', 'Miami', 'Los Angeles', 'Chicago', 'Dallas']
destination = random.choice(destinations_list)
print(destination)

transportations_list = ['Car', 'Train', 'Plane', 'Motorcycle', 'Charter Bus']
transportation = random.choice(transportations_list)
print(transportation)

entertainments_list = ['NBA game', 'NFL game', 'NHL game', 'Mueseum', 'Movie']
entertainment = random.choice(entertainments_list)
print(entertainment)

restaurants_list = ['Cheddars', 'Longhorns', 'BJs', 'Red Lobsters', 'Yardhouse']
restaurant = random.choice(restaurants_list)
print(restaurant)

valid_response = False
while valid_response == False:

    

    happy_customer = input('Are you ready to go? Confirm with a Yes or a No! ')

    if happy_customer == "Yes":
        print(f"Awesome! To confirm, we're going to {destination} in a {transportation}, to a {entertainment}, and afterwards go eat at {restaurant}!")
        valid_response = True
    elif happy_customer == "No":
        print("Well, let's see if this next one makes you happy... Let's try again!")
        valid_response = False
        
        destination = random.choice(destinations_list)
        print(destination)

        transportation = random.choice(transportations_list)
        print(transportation)

        entertainment = random.choice(entertainments_list)
        print(entertainment)

        restaurant = random.choice(restaurants_list)
        print(restaurant)
    else:
        print("Please, just reply with a yes or no!")
