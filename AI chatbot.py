import time
import random
name = input("Hello , what is your name?")
time.sleep(2)
print("Hello" + name )

feeling = input ("How are you today ?")

time.sleep(1)
if "good" in feeling :
    print("I am feeling good too!!!")
else:
    print("I am sorry to hear that!")
    time.sleep(1)
    favcolour = input("What is you favourite colour ?")

    colours = ["Red","Green","Blue"]
    time.sleep(1)

    print("My favourite colour is " + random.choice(colours))

    mood = input(" what are you doing today? ")
    mood = ["dancing","reading","playing","watching tv","hiking"]
    time.sleep(1)
    print("I feel like" + random.choice(mood) + "today")
    time.sleep(1)
    input("cool")

    food = input("which food type do you like most? ")
    food =[" Asian","Italian","Japnese","chinese","latin"]
    time.sleep(1)
    print("I mostly like ", + random.choice + "food")
    sport = input("which sport do you like to watch most ?")
    sport = ["cricket","baseball","soccker","football"]
    time.sleep(1)
    print("I like to watch" + random.choice(sport))
    time.sleep(1)
    print("I love talking with you")

    peak = input("Do you know the height of world's tallest mountain ?")
    time.sleep(1)
    print("8848")
    print("Anyone can answer that?")
    planet = input("How many planets are there in this solar system ")
    time.sleep(1)

    print("I guess there are 8 planets")

    tired = input ("I am feeling tired today ")
    time.sleep(1)
    print("see you! Have a great day.")