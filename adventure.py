"""Week 3 Coding Assignment. Juanita Stuenkel"""

import random

inventory = list()

def display_player_status(player_health):
    """prints player's health"""
    print(f"Your current health: {player_health}." )

def handle_path_choice(player_health):
    """decides left or right"""
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        if player_health <= 90:
            player_health += 10
        elif player_health > 90:
            player_health = 100
    elif path == "right":
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """player deals 15 damage to the monster"""
    monster_health -= 15
    print("You strike the monster for 15 damage!")
    print(f"The monster is at {monster_health} health!")
    return monster_health

def monster_attack(player_health):
    """monster attacks the player, with a chance of a critical hit"""
    critical = random.random()

    if critical < 0.5:
        player_health -= 20
        print("The monster lands a critical hit for 20 damage!")
    if critical > 0.5:
        player_health -= 10
        print("The monster hits you for 10 damage!")
    return player_health

def combat_encounter(player_health, monster_health, has_treasure=bool):
    """runs combat encounter"""
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        player_attack(monster_health)
        display_player_status(player_health)
        if monster_health > 0:
            player_health = monster_attack(player_health)
            monster_attack(player_health)
        if player_health <= 0:
            print("Game OVer!")
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure


def check_for_treasure(has_treasure):
    """checks for treasure"""
    if has_treasure is True:
        print("You found the hidden treasure! You win!")
    if has_treasure is False:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    """ adds acquired item to list and print aquired item"""
    inventory.append(item) # Add more items to list as they are acquired in the room
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """ displays inventory in a number list"""
    if len(inventory) > 0:
        print("Your inventory:")
        for index, item in enumerate(inventory):
            print(f"{index + 1}. {item}")
    else:
        print("Your inventory is empty.")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """ runs through each dungeon room """
    try:
        dungeon_rooms[0] = ("A big hole", "Candy", "puzzle", ("Wow!", "Nope!", -10))
    except TypeError:
        print("Error: Cannot modify a tuple as they are immutable!")
    for dungeon_room in dungeon_rooms:   # used to go through each list within the tuple to use it
        print(dungeon_room[0])
        if dungeon_room[1] != None:
            acquire_item(inventory, dungeon_room[1])
        if dungeon_room [2] == "puzzle":
            print("You encounter a puzzle!")
            puzzle_input = input("Solve or skip the puzzle?")
            successA = True
            if puzzle_input == "solve":
                successA = random.choice([True, False])
            if successA is True:
                print(dungeon_room[3][0])
                player_health += dungeon_room[3][2]
            else:
                print(dungeon_room[3][1])
        elif dungeon_room [2] == "trap":
            print("You see a potential trap!")
            trap_input = input("Disarm or bypass the trap?")
            successB = True
            if trap_input == "Disarm":
                successB = random.choice([True, False])
            if successB is True:
                print(dungeon_room[3][0])
            else:
                print(dungeon_room[3][1])
        elif dungeon_room [2] is None:
            print("There doesn't seem to be a challenge in this room. You move on.")
    
    return (player_health, inventory)
   

def main():
    """runs program with other functions"""

    player_health = 100
    monster_health = 55
    has_treasure = False

    dungeon_rooms = (
    ("A dark cavern", "Smelly sock", "puzzle", ("You did it!", "You failed", -10)),
    ("An old mineshaft", None, "trap", ("You avoid the trap!", "You fell!", -15)),
    ("A beautiful oasis", "healing potion", "none", None)
    )

    has_treasure = random.choice([True, False])

    player_health = handle_path_choice(player_health)


    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    player_health = monster_attack(player_health)
    monster_health = player_attack(monster_health)

    check_for_treasure(treasure_obtained_in_combat)

    if player_health > 0:
        enter_dungeon(player_health, inventory, dungeon_rooms)

    if player_health <= 0:
        player_health = 0
        print("You are barely alive!")
        display_inventory(inventory)

    display_inventory(inventory)

    print("You picked up a smelly sock along the way but throw it away.")
    inventory.remove("Smelly sock") #removes specific item from inventory list

    display_inventory(inventory)

if __name__ == "__main__":
    main()
    