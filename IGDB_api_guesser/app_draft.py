
import random
import requests
import string

#ENCRYPTION OF API KEY (from video HOW TO HIDE YOUR API KEYS IN PYTHON PROJECTS)
from dotenv import load_dotenv
import os

#loads the configuration from .env
def configure():
    load_dotenv()

configure()

#IGDB api authorization
authorization = "Bearer " + os.getenv('access_token')


#TRYING TO RANDOMLY SELECT A LETTER
def generate_random_letter():
    
    random_letter = random.choice(string.ascii_letters)
    return random_letter


#GENERATING THE FRANCHISE ANSWER

def post_franchise_request():


    random_letter = generate_random_letter()

    response_franchise = requests.post(
        'https://api.igdb.com/v4/games',
        headers= {'Client-ID': os.getenv('client_id'),
                  'Authorization': authorization},
        data=f'search "{random_letter}"; fields franchises.name,genres.name,release_dates.y,keywords.name; where rating > 80 & franchises.name != "" & keywords.name != "";'
        )
    
    response_franchise_json = response_franchise.json()

    return response_franchise_json


def generate_franchise():

    response_franchise_json = []

    while response_franchise_json == []:

        generated_franchise = post_franchise_request()

        response_franchise_json = generated_franchise

    #generating a random number from 0 to the end of the list and then getting that
    #particular franchise
    #print(response_franchise_json)

    random_number = random.randint(0, len(response_franchise_json) - 1)

    #print(response_franchise_json[0])

    #ANSWER
    answer = response_franchise_json[random_number]['franchises'][0]['name']

    #print(f"{response_franchise_json[random_number]['franchises'][0]['name']}")
    print(f"The genre is: {response_franchise_json[random_number]['genres'][0]['name']}")
    print(f"It came out in: {response_franchise_json[random_number]['release_dates'][0]['y']}")
    print(f"A keyword associated is: {response_franchise_json[random_number]['keywords'][0]['name']}")


    return answer



def start_game(): 


    strikes = 3

    print("Let's play guess what franchise I am thinking of! You get three tries")
    #print(f'Strikes: {strikes}')

    print("---------------------")

    franchise = generate_franchise()
    string_franchise = str(franchise)

    print("---------------------")



    while strikes > 0:

        print(f'you have {strikes} strikes')
        user_input = input("What is your guess: ")

        if user_input.lower() == string_franchise.lower():
            print("You win!")
            break
        else:
            strikes -= 1
            print("Try again")

    if strikes == 0:
        print(f"The correct franchise was {string_franchise}")
        


start_game()







    





