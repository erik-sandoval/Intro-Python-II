from room import Room
from player import Player
from item import Item

# Declare all the rooms
item = {
    'sword': Item("Sword", "very sharp!"),
    'shield': Item("Shield", "sturdy and heavy."),
    'arrows': Item("Arrows", "silent and effecient"),
    'gun': Item("Gun", "wait what?"),
    'health': Item("Health Potion", "just what I needed!"),
    'axe': Item("Axe", "might come in handy."),
    'bow': Item('Bow', 'no arrows?')
}
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", item['health']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['arrows']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['gun']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['axe']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
# Make a new player object that is currently in the 'outside' room.

player = Player("Erik", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    avail_rooms = dict(n=player.current_room.n_to, w=player.current_room.w_to,
                       s=player.current_room.s_to, e=player.current_room.e_to)

    print(f'You are at {player.current_room.name}')

    if (player.current_room.items == None):
                print("The room is empty")
    else:
        print(f'You look down and find a {player.current_room.items.name}\n\n')

    for k, v in avail_rooms.items():
        if (v != None):
            print(f"Press '{k}' to go {v.name}")

    direction = input(
        "\n\n Please choose a direction from the above options, pick up the item found on the floor: ").lower()

    direction = direction.strip().split(maxsplit=1)

    if (direction[0] == 'n'):
        player.current_room = player.current_room.n_to
    elif (direction[0] == 'e'):
        player.current_room = player.current_room.e_to
    elif (direction[0] == 's'):
        player.current_room = player.current_room.s_to
    elif (direction[0] == 'w'):
        player.current_room = player.current_room.w_to
    elif (direction[0] == 'take' or direction[0] == 'grab'):
        if(len(direction) == 2):
            if (player.current_room.items.name.lower() == direction[1]):
                player.addItem(direction[1])
                player.current_room.items = None
                print(f"{direction[1]} picked up\n\n")
            else:
                print(
                    f"{direction[1]} not found in {player.current_room.name}")
        else:
            print("Specify item to grab")
    else:
        print(f"input not recognized, please follow instructions")
