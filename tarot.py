from random import randint
import csv

readings_dict = {}

#load readings for cards from csv api to dictionary
with open('TAROT_READINGS.csv', mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    readings_dict = {rows[0]:rows[1:3] for rows in csv_reader}

#set basic cards for major arcana
major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

#set minor numbers for cards
minor_pip = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

#set the main suits
minor_suits = ["Pentacles", "Wands", "Cups", "Swords"]

#set the types of readings that can be performed
type_of_reading = ["Love", "Career", "Money"]

#iterate through to create minor arcana from pip and suits and amend to new full arcana list
minor_arcana = []

for suit in minor_suits:
    for pip in minor_pip:
        minor_arcana.append(str(pip) + ' of ' + str(suit))

full_arcana = major_arcana + minor_arcana

#function to pull three card reading for past, present, future
def pull_three_cards(reading):

    #set the dictionary list array position
    if reading == "Career":
        position = 1
    elif reading == "Money":
        position = 2
    else: position = 0

    # pull three cards and .pop from list when pulled
    first_card = full_arcana.pop(randint(0, len(full_arcana) - 1))
    second_card = full_arcana.pop(randint(0, len(full_arcana) - 1))
    third_card = full_arcana.pop(randint(0, len(full_arcana) - 1))

    first_card_reading = ''
    second_card_reading = ''
    third_card_reading = ''

    #assign meaning from csv data to each card readings
    for x, y in readings_dict.items():
        if x == first_card:
            first_card_reading = y[position]
        if x == second_card:
            second_card_reading = y[position]
        if x == third_card:
            third_card_reading = y[position]

    #print out the reading for past, present, and future cards pulled
    print("When it comes to {reading}...".format(reading=reading))
    print("The First card is {first_card} and represents {first_card_reading} in the Past.".format(first_card = first_card, first_card_reading = first_card_reading))

    print("The Second card is {second_card} and represents {second_card_reading} in the Present.".format(second_card = second_card, second_card_reading = second_card_reading))

    print("The Third card is {third_card} and represents {third_card_reading} in the Future.".format(third_card = third_card, third_card_reading = third_card_reading))

#start tarot reading for user
print("Welcome to Tarot Reader Express")
user_reading = ''

while user_reading not in type_of_reading:
    user_reading = input("What type of reading are you looking for?\n1. Love\n2. Career\n3. Money\n")

pull_three_cards(user_reading)
