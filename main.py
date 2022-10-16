import random

CHOICE = ["R", "P", "S"]

class Game:
    def __init__(self, choice):
        self.player_choice = choice
        self.computer_choice = random.choice(CHOICE)

    def print_choice(self):
        print(f"Computer chose '{self.computer_choice}' and you chose '{self.player_choice}'")
        print("-----------------------------------------------------------------------------")

    def win_or_lose(self):
        if self.player_choice == self.computer_choice:
            print("TRY AGAIN")
        elif self.player_choice == "R":
            if self.computer_choice == "P":
                print("YOU LOSE")
            elif self.computer_choice == "S":
                print("YOU WON")
        elif self.player_choice == "P":
            if self.computer_choice == "S":
                print("YOU LOSE")
            elif self.computer_choice == "R":
                print("YOU WON")
        elif self.player_choice == "S":
            if self.computer_choice == "P":
                print("YOU WON")
            elif self.computer_choice == "R":
                print("YOU LOSE")

        print("-----------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------")

game_on = True

while game_on:
    choice = input("WELCOME!!!\nType your option.\nType 'R' for rock, 'P' for paper and 'S' for scissors.\nType 'Q' to quit\n-----------------------------------------------------------------------------\n").upper()
    if choice == "Q":
        print("GAME OVER")
        break
    game = Game(choice=choice)
    game.print_choice()
    game.win_or_lose()