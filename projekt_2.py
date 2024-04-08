"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tereza Streckerová
email: tereza.vack@gmail.com
discord: te.str
"""

import random

separator = "-" * 50
print("Hi there!", separator, "I´ve generated a random 4 digit number for you.",
      "Let´s play a bulls and cows game.", separator, sep="\n")


def generate_number():
    """
    Program vygeneruje náhodné 4 místné číslo nezačínající 0
    :return: vygenerované číslo, které se snaží uživatel uhádnout
    """
    number_1 = random.sample(range(1, 10), 1)
    number_234 = random.sample(range(0, 10), 3)

    while number_1[0] in number_234:
        number_1 = random.sample(range(1, 10), 1)

    con_num = number_1 + number_234
    s = [str(i) for i in con_num]
    output = "".join(s)
    return output


def insert_number():
    """
    Kontrola hádaného čísla od uživatele
    :return: číslo, které je porovnáváno s vygenerovaným
    """
    while True:
        player_number = input("Enter only 4 digit number: ")
        if len(player_number) != 4 or player_number.isdigit() is False:
            print("It must be 4 digit!")
            continue

        if int(player_number[0]) == 0:
            print("It can´t be 0 on first place")
            continue
        break

    for digit in player_number:
        if player_number.count(digit) > 1:
            print("You have duplicity")
            break
    return player_number


def count_bulls(player_number, gen_number):
    """
    Počet uhádnutých čísel na správné pozici
    :param player_number: číslo uživatele
    :param gen_number: generované číslo
    :return: počet správně umístěných čísel
    """
    bulls = 0
    for i in range(0, len(gen_number)):
        if player_number[i] == gen_number[i]:
            bulls += 1
    return bulls


def count_cows(player_number, gen_number, bulls):
    """
    Počet pouze správně uhádnutých čísel, tedy čísel, které se nacházejí v generovaném čísle, ale nejsou správně umístěny.
    :param player_number: číslo uživatele
    :param gen_number: generované číslo
    :param bulls: počet správně umístěných čísel
    :return: počet uhádnutých čísel bez správného umístění
    """
    cows = 0
    for p in player_number:
        if p in gen_number:
            cows += 1

    return cows - bulls


def print_bulls_cows(bulls, cows):
    """
    Výpis počtu uhádnutých čísel
    :param bulls: počet správně umístěných čísel
    :param cows: počet uhádnutých čísel bez správného umístění
    :return: výpis počtu bulls a cows
    """
    if bulls == 1:
        print(bulls, "bull",  end=", ")
    else:
        print(bulls, "bulls",  end=", ")
    if cows == 1:
        print(cows, "cow")
    else:
        print(cows, "cows")


def write_rating(turn_count):
    """
    Hodnocení počtu tahů
    :param turn_count: počet tahů uživatele
    :return: slovní hodnocení
    """
    score = {1: "incredible!!!", 2: "amazing!", 3: "amazing!", 4: "amazing!", 5: "average", 6: "average",
             7: "not so good", 8: "not so good", 9: "not so bad"}
    if turn_count in score.keys():
        print("That is", score[turn_count])
    else:
        print("It is very, very, very bad!!!")

    return


def main():
    gen_number = generate_number()
    # print(gen_number, separator, sep="\n")

    game_runs = True
    turn_count = 0

    while game_runs:
        player_number = insert_number()
        turn_count += 1
        print(">>>", player_number)

        if player_number == gen_number:
            print(f"Correct, you´ve guessed the right number in {turn_count} guesses!", separator, sep="\n")
            write_rating(turn_count)
            break

        bulls = count_bulls(player_number, gen_number)
        cows = count_cows(player_number, gen_number, bulls)

        print_bulls_cows(bulls, cows)
        print(separator)


if __name__ == "__main__":
    main()
