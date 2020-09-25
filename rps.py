# rock-paper-scissors by Christiaan de Jong

import random
import json
import os.path
from os import path

default = '[{"name":"rock","wins":{"scissors":"crushes","lizard":"crushes"}},{"name":"paper","wins":{"rock":"covers","spock":"disproves"}},{"name":"scissors","wins":{"paper":"cuts","lizard":"decapitates"}},{"name":"spock","wins":{"rock":"vaporizes","scissors":"smashes"}},{"name":"lizard","wins":{"paper":"eats","spock":"poisons"}}]'
item_list = []

class Item:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins


def create_items():
    """ this function fills itemList with items from 'items.json' or if 'items.json' couldn't be found from 'default'
        arguments: no arguments 
        results: no results
    """
    if path.exists("items.json"):
        file = open("items.json", "r")
        data = json.load(file)
        file.close()
    else:
        print()
        print('[WARN]: items.json not found! loading default items, for 101 items rps download this: https://github.com/CdeJong/Rock-Paper-Scissors-101 and put it in the same folder as this file.')
        data = json.loads(default)
    
    itemList.clear()
    for item in data:
        item_list.append( Item(item.get("name"), item.get("wins")) )


def get_item_list():
    """ this function creates list of all options.
        arguments: no arguments 
        results: String (list of all options)
    """
    result = ""
    for item in item_list:
        # if item is not the last item paste a comma after the name.
        if item_list[-1:] != item:
            result += item.name + ", "
            continue
        result += item.name
    return result


def get_item_by_name(name):
    """ this function returns Item if a Item with name exists.
        arguments: String name (name of Item object) 
        results: Item
    """
    result = None
    for item in item_list:
        if item.name == name.lower():
            result = item
            break
    return result

        
def get_winner(player_item, computer_item):
    """ this function figures out who won the game.
        arguments: Item playerItem (Item the player chose), Item computerItem (Item the computer chose)
        results: String Winner ('draw', 'player', 'computer' or if no winner is found 'error')
    """
    if computer_item.name == player_item.name:
        return "draw"
    elif computer_item.name in player_item.wins:
        return "player"
    elif player_item.name in computer_item.wins:
        return "computer"
    else:
        return "error"
        

def rps():
    """ this starts a game of rock-paper-scissors (or a variant of that game) in a loop so you can replay faster.
        arguments: no arguments
        results: no results
    """
    while True:
        rps_game()
        print()
        a = input("Do you want to play again? (Y/n)\n >> ")
        if a.lower() == "n":
            break;
        else:
            print()
            print("Okay, lets play again!")


def rps_game():
    """ this starts a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments
        results: no results
    """
    create_items()

    while True:
        print()
        print("Options:", get_item_list())
        playerItemName = input("Choose your weapon:\n >> ")

        if bool(get_item_by_name(playerItemName)):
            break;
        else:
            print()
            print("[WARN]: item does not exists! Choose one from the options below.")
    
    player_item = get_item_by_name(playerItemName)
    computer_item = random.choice(item_list)
    winner = get_winner(player_item, computer_item)


    print()
    print('Player:', player_item.name)
    print('Computer:', computer_item.name)
    print()

    
    if winner == "draw":
        print("DRAW")
    elif winner == "player":
        print(player_item.name, player_item.wins.get(computer_item.name))
        print("PLAYER WINS!")
    elif winner == "computer":
        print(computer_item.name, computer_item.wins.get(player_item.name))
        print("COMPUTER WINS!")
    else:
        print("[WARN]: An error has occurred! No winner could be found. Possible something is wrong in 'items.json'")