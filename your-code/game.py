import os
from rooms import rooms


# Global variables
current_room_name = "Game Room" # game starts from the "Game Room"
collected_keys = []



def clear_console():
    """Clears the command line screen (cross-platform)."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')



def get_user_choice(options, intro = ""):
    while True:
        # display intro message
        print(intro)
        print("Choose one of the following options: ")

        # display all available options
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        # get user's choice
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(options):
                clear_console()
                return options[choice - 1]
            else:
                clear_console()
                print(f"\n\nPlease choose a number between 1 and {len(options)}.")
        except ValueError:
            clear_console()
            print("\n\nInvalid input. Please enter a valid number.")



def display_room_options():
    print(f"\n\nYou're in the room \"{current_room_name}\"")
    result = get_user_choice(["Explore", "Examine"])
    if(result == "Explore"):
        explore()
    elif(result == "Examine"):
        examine()



def explore():
    items = rooms[current_room_name]["interactive_items"]
    doors = rooms[current_room_name]["doors"]

    print(f"\n\n******")
    print(f"\nYou explore the {current_room_name}... And here's what you find: ", end=" ")

    # Print items with commas, add dot after the last item
    for i, item in enumerate(items):
        print(item["item_name"], end=", ")

    # Print doors with commas, add dot after the last door
    for i, door in enumerate(doors):
        print(door["door_name"], end=", " if i < len(doors) - 1 else ".")

    print(f"\n\n******\n")

    display_room_options()




def examine():
    global collected_keys

    # Get all valid items and doors
    valid_items = {item["item_name"]: item["keys_to_collect"] for item in rooms[current_room_name]["interactive_items"]}
    valid_doors = {door["door_name"]: door["destination"] for door in rooms[current_room_name]["doors"]}

    clear_console()
    choice = input("\n\nWhat would you like to examine?")
    clear_console()

    # Check and output results
    if choice in valid_items:
        if valid_items[choice]:
            collected_keys = collected_keys + valid_items[choice]
            print(f"\n\nYou examine {choice}. You find these keys {valid_items[choice]}")
        else:
            print(f"\n\nYou examine {choice}. There isn't anything interesting about it.")
    elif choice in valid_doors:
        if choice in collected_keys:
            print(f"\n\nYou examine {choice}. You unlock it with a key you have.")
            wantsNextRoom = get_user_choice(["Yes", "No"], "\n\nDo you want to go to the next room?")
            if(wantsNextRoom == "Yes"):
                next_room = valid_doors[choice]
                change_room(next_room)
                return
        else:
            print(f"\n\nYou examine {choice}. It is locked but you don't have the key.")
    else:
        print("\n\nThe item you requested is not found in the current room.")

    display_room_options()



def change_room(room_name):
    global current_room_name

    if room_name == "Outside":
        print("\n\n\n\nCongrats! You escaped the room!\n\n\n\n")
        return
    else:
        current_room_name = room_name
        display_room_options()



def start():
    clear_console()
    print("\n\nYou wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    display_room_options()



start()

