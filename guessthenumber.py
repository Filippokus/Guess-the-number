import random


class Player:
    def __init__(self, name):
        self.name = name
        self.attempt = 0


def create_player():
    name = input("Enter your name: ")
    return name


def main():
    list_players = []
    incorrect_numbers = []

    for _ in range(int(input("How many players will play?:\n"))):
        list_players.append(Player(create_player()))
    print("Players:", ', '.join(player.name for player in list_players))

    while True:
        try:
            input_diapason = input("Enter a range of numbers separated by spaces:\n")
            num1, num2 = map(int, input_diapason.split())
            number = random.randint(num1, num2)
            break
        except ValueError:
            print("Enter two numbers separated by a space")

    winner_found = False
    while not winner_found:
        for player in list_players:
            while True:
                choose = input(f"Player {player.name}, enter a number from {num1} to {num2}: ")
                if choose.isdigit():
                    choose = int(choose)
                    if num1 <= choose <= num2:
                        if choose not in incorrect_numbers:
                            player.attempt += 1
                            break
                        else:
                            print(f"The number {choose} has already been entered")
                    else:
                        print(f"The number must be between {num1} and {num2}.")
                else:
                    print("Please enter an integer")
            if choose == number:
                print(f"Player {player.name} guessed the number on {player.attempt} try!")
                winner_found = True
                break
            else:
                incorrect_numbers.append(choose)
                if len(list_players) > 1:
                    print(f"{player.name} didn't guess correctly, let another player try")
                else:
                    print(f"You guessed wrong, try again")
                continue


if __name__ == '__main__':
    main()
