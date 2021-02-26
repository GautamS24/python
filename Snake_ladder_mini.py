import random

# Snake takes you down from 'key' to 'value'
snakes={
    12: 2,
    17: 4,
    31: 19,
    35: 22,
    }
# ladder takes you from 'key' to 'value'
ladders={
    3: 16,
    5: 7,
    18: 20,
    21: 30,
    }
def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name
def get_dice_value():
    dice_value=random.randint(1,6)
    print("Lucky number",str(dice_value))
    return dice_value
# defining snake ladder
def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
    elif current_value in ladders:
        final_value = ladders.get(current_value)

    else:
        final_value = current_value

    return final_value
def check_win(player_name, position):
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)
def start():
    player1_name, player2_name = get_player_names()

    player1_current_position = 0
    player2_current_position = 0

    while True:
        dice_value = get_dice_value()
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)
if __name__ == "__main__":
    start()