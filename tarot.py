from random import randint

major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

minor_pip = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

minor_suits = ["Pentacles", "Wands", "Cups", "Swords"]

minor_arcana = []

for suit in minor_suits:
    for pip in minor_pip:
        minor_arcana.append(str(pip) + ' of ' + str(suit))


type_of_reading = ["Love", "Money", "Career"]

full_arcana = major_arcana + minor_arcana

print("Welcome to Tarot Reader Express")
#user_reading = input("What type of reading are you looking for?")

print(str(minor_arcana[randint(0, 13)]) + " of " + str(minor_suits[randint(0, 3)]))
#print(full_arcana)
