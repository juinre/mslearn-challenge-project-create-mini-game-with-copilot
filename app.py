# Create a console application to play the game piedra, papel o tijera divided in functions 
# The game will be played by two players, the user and the computer
# The computer will randomly choose one of the three options: piedra, papel o tijera
# The game will start clearing the console
# The game display a welcome message in spanish with the rules of the game and message asking the user to press a key to start the game
# The user will be asked in spanish has to write one of the three options: piedra, papel o tijera
# The input will be converted to lowercase and validated
# The program will display the choice of the user and the computer in the same line as "Tu: piedra" - "Computadora: papel"
# In a new line the program will display the result of the game and who won as "Piedra rompe a Tijera. Ganaste!", "Tijera corta a Papel. Perdiste!", "Empate!"
# The program will ask the user in a menu if they want to play again as ¿Jugar de nuevo? (S/N)
# The input will be converted to lowercase and validated
# If the user chooses not to play again, the program will display a resume in spanish with the number of games played, wins, loses and ties
# The program will exit

# The program will be divided in the following functions:
# clear_screen() -> void
# welcome_message() -> void
# user_choice() -> string
# computer_choice() -> string
# game_result(user_choice, computer_choice) -> string
# play_again() -> boolean
# game_stats(wins, loses, ties) -> void


import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    print("Bienvenido al juego Piedra, Papel o Tijera")
    print()
    print("Las reglas son las siguientes:")
    print()
    print("\t- Piedra rompe a Tijera")
    print("\t- Tijera corta a Papel")
    print("\t- Papel envuelve a Piedra")
    print()
    input("Presiona una tecla para comenzar ")

def user_choice():
    choice = input("Elige una opción: piedra, papel o tijera: ").lower()

    # Validate the input clear the line
    while choice != "piedra" and choice != "papel" and choice != "tijera":
        print("\033[A                             \033[A")
        choice = input("Opción No Válida. Elige una opción: piedra, papel o tijera: ").lower()
        
    return choice

def computer_choice():
    choices = ["piedra", "papel", "tijera"]
    return random.choice(choices)

def game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif user_choice == "piedra":
        if computer_choice == "tijera":
            return "Piedra rompe a Tijera. Ganaste!"
        else:
            return "Papel envuelve a Piedra. Perdiste!"
    elif user_choice == "papel":
        if computer_choice == "piedra":
            return "Papel envuelve a Piedra. Ganaste!"
        else:
            return "Tijera corta a Papel. Perdiste!"
    elif user_choice == "tijera":
        if computer_choice == "papel":
            return "Tijera corta a Papel. Ganaste!"
        else:
            return "Piedra rompe a Tijera. Perdiste!"
            
def play_again():
    print()
    choice = input("¿Jugar de nuevo? (S/N): ").lower()
    # validate the input clear the line
    while choice != "s" and choice != "n":
        print("\033[A                             \033[A")
        choice = input("Opción No Válida. ¿Jugar de nuevo? (S/N): ").lower()
   
    return choice == "s"

def game_stats(wins, loses, ties):
    print(f"Jugados: {wins + loses + ties} Ganados: {wins} Perdidos: {loses} Empates: {ties}")

def main():
    wins = 0
    loses = 0
    ties = 0
    clear_screen()
    welcome_message()
    while True:
        print() 
        user = user_choice()
        computer = computer_choice()
        print(f"Tu: {user} - Computadora: {computer}")
        result = game_result(user, computer)
        print(result)
        if "Ganaste" in result:
            wins += 1
        elif "Perdiste" in result:
            loses += 1
        else:
            ties += 1
        if not play_again():
            print() 
            game_stats(wins, loses, ties)
            print("Gracias por jugar!")
            print()
            break

if __name__ == "__main__":
    main()

# To run the program, execute the following command:
# python app.py
