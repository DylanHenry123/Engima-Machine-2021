# My Enigma Machine
# Setting the physical format for the rotors
rotor_set_one = {"A": "I", "B": "S", "C": "L", "D": "V", "E": "T", "F": "P", "G": "X", "H": "Y", "I": "U", "J": "R",
                 "K": "N", "L": "D", "M": "F", "N": "Q", "O": "A", "P": "E", "Q": "C", "R": "B", "S": "H", "T": "K",
                 "U": "G", "V": "O", "W": "Z", "X": "W", "Y": "M", "Z": "J"}

rotor_set_two = {"A": "U", "B": "E", "C": "A", "D": "B", "E": "F", "F": "Y", "G": "N", "H": "G", "I": "R", "J": "S",
                 "K": "M", "L": "W", "M": "X", "N": "I", "O": "J", "P": "C", "Q": "L", "R": "T", "S": "P", "T": "V",
                 "U": "Q", "V": "O", "W": "H", "X": "D", "Y": "Z", "Z": "K"}

rotor_set_three = {"A": "O", "B": "T", "C": "H", "D": "L", "E": "R", "F": "P", "G": "F", "H": "E", "I": "Z", "J": "X",
                   "K": "G", "L": "K", "M": "N", "N": "W", "O": "S", "P": "C", "Q": "U", "R": "Q", "S": "Y", "T": "D",
                   "U": "B", "V": "M", "W": "I", "X": "V", "Y": "A", "Z": "J"}

rotor_set_four = {"A": "I", "B": "C", "C": "A", "D": "M", "E": "K", "F": "H", "G": "W", "H": "L", "I": "J", "J": "D",
                  "K": "Y", "L": "N", "M": "E", "N": "Z", "O": "U", "P": "T", "Q": "B", "R": "S", "S": "Q", "T": "F",
                  "U": "G", "V": "P", "W": "R", "X": "O", "Y": "V", "Z": "X"}

rotor_set_five = {"A": "U", "B": "C", "C": "P", "D": "F", "E": "D", "F": "Y", "G": "Q", "H": "K", "I": "L", "J": "E",
                  "K": "G", "L": "I", "M": "V", "N": "X", "O": "H", "P": "A", "Q": "O", "R": "Z", "S": "M", "T": "S",
                  "U": "T", "V": "N", "W": "J", "X": "B", "Y": "W", "Z": "R"}

reflector = {"A": "N", "B": "Y", "C": "U", "D": "V", "E": "L", "F": "A", "G": "S", "H": "P", "I": "B", "J": "Z",
             "K": "O", "L": "K", "M": "D", "N": "F", "O": "C", "P": "W", "Q": "H", "R": "Q", "S": "G", "T": "M",
             "U": "X", "V": "E", "W": "J", "X": "R", "Y": "I", "Z": "T"}


class Rotor:
    def __init__(self, a_rotor_name, a_letter_set):
        self.name = a_rotor_name
        self.rotor_contents = a_letter_set
        self.current_rotation = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def shuffle_start_rotation(self, value):
        """
        Allows you to choose the starting position of the rotor(e.g. what letter to start on)
        :param value: str
        :return: none
        """
        times = 26 - (ord(value) - ord('A'))
        if 1 <= times <= 25:
            for j in range(times):
                temp = self.current_rotation[-1]
                for i in range(25, 0, -1):
                    self.current_rotation[i] = self.current_rotation[i - 1]

                self.current_rotation[0] = temp

    def rotor_tick(self):
        """
        Moves the rotor one position for new letter
        :return: none
        """
        temp = self.current_rotation[-1]
        for i in range(25, 0, -1):
            self.current_rotation[i] = self.current_rotation[i - 1]

        self.current_rotation[0] = temp

    def encrypt_letter(self, value):
        new_letter = self.rotor_contents[value]
        index = self.current_rotation.index(new_letter)

        return index

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class PlugBoard:
    def __init__(self):
        self.board = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "",
                      "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "",
                      "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}

    def rig_letters(self, key, value):
        # Put the values into the dictionary.
        self.board[key] = value

    def encrypt_letter(self, value):
        # Change the value of the character for the encrypted message.
        new_letter = self.board[value]

        return new_letter


# Instantiating the object
plugBoard = PlugBoard()
ROTOR_ONE = Rotor("One", rotor_set_one)
ROTOR_TWO = Rotor("Two", rotor_set_two)
ROTOR_THREE = Rotor("Three", rotor_set_three)
ROTOR_FOUR = Rotor("Four", rotor_set_four)
ROTOR_FIVE = Rotor("Five", rotor_set_five)
REFLECTOR = Rotor("Reflector", reflector)

rotors = [ROTOR_ONE, ROTOR_TWO, ROTOR_THREE, ROTOR_FOUR, ROTOR_FIVE]
chosen_rotors = []


def choose_rotor():
    choice = int(input("Rotor: "))

    if choice == 1:
        chosen_rotors.append(rotors[0])

    elif choice == 2:
        chosen_rotors.append(rotors[1])

    elif choice == 3:
        chosen_rotors.append(rotors[2])

    elif choice == 4:
        chosen_rotors.append(rotors[3])

    elif choice == 5:
        chosen_rotors.append(rotors[4])

    else:
        print("Input is not valid, Try again")
        choose_rotor()


def rotor_position():
    print("\nChoose the starting letters of the rotors")
    for i in range(len(chosen_rotors)):
        print(f"\nRotor {i + 1}: ")
        starting_value = input("Letter: ")

        chosen_rotors[i].shuffle_start_rotation(starting_value)


def rig_plug_board():
    plug_board = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # 10 potential wires that link two letters together. The other 6 letters remain unchanged.
    for i in range(10):
        print(f"\nChoose a letter A-Z (pair: {i + 1}, remaining characters: {plug_board}):")
        first = input("Letter: ")
        second = input("Links to: ")

        if first in plug_board and second in plug_board:

            plugBoard.rig_letters(key=first, value=second)
            plugBoard.rig_letters(key=second, value=first)

            plug_board.remove(first)
            plug_board.remove(second)

        else:
            print("input not valid, restart process")
            rig_plug_board()

    for i in range(len(plug_board)):
        plugBoard.rig_letters(plug_board[i], plug_board[i])

    print("\nOther values have been filled in automatically")


def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Choosing the rotors to use to encrypt
    print("\nSelect which three Rotors you would like to use (1, 2, 3, 4, 5): ")
    for i in range(3):
        choose_rotor()

    # Setting the rotor positions to be different
    rotor_position()

    # At the moment you can choose a rotor and you can choose the starting position of a rotor

    print("""\n 
Now its time to rig the plug board.
10 wires will link 10 pairs of numbers
6 numbers will remain unchanged 
""")

    # Sets up the plug board ready to encrypt
    rig_plug_board()

    # Take in a message.
    print("")
    plain_text = input("Message: ")
    plain_text = plain_text.upper()

    ciphered_text = []

    count = 1

    # Loops through each letter in message to encrypt
    for char in plain_text:

        if char in alphabet:
            # Every letter entered, rotor 1 ticks
            rotors[0].rotor_tick()
            # Every 26th letter entered, rotor 2 ticks
            if count % 26 == 0:
                rotors[1].rotor_tick()
            # Every 676th letter entered, rotor 3 ticks
            if count % 676 == 0:
                rotors[3].rotor_tick()

            # For each letter in the message, pass through the plug board
            real_value = plugBoard.encrypt_letter(char)

            # Then through the first rotor
            index_one = rotors[0].encrypt_letter(real_value)

            # Then through the second rotor
            corresponding_letter = rotors[1].current_rotation[index_one]
            index_two = rotors[1].encrypt_letter(corresponding_letter)

            # Then through the third rotor
            corresponding_letter_two = rotors[2].current_rotation[index_two]
            index_three = rotors[2].encrypt_letter(corresponding_letter_two)

            # Then through the reflector
            corresponding_letter_three = REFLECTOR.current_rotation[index_three]
            index_four = REFLECTOR.encrypt_letter(corresponding_letter_three)

            # Then back through rotor three
            corresponding_letter_four = rotors[2].current_rotation[index_four]
            index_five = rotors[2].encrypt_letter(corresponding_letter_four)

            # Then back through rotor two
            corresponding_letter_five = rotors[1].current_rotation[index_five]
            index_six = rotors[1].encrypt_letter(corresponding_letter_five)

            # Then back through rotor one
            corresponding_letter_six = rotors[0].current_rotation[index_six]
            index_seven = rotors[0].encrypt_letter(corresponding_letter_six)

            # Gets the final value passing it back through the plug board
            penultimate_value = rotors[0].rotor_contents[rotors[0].current_rotation[index_seven]]
            final_value = plugBoard.encrypt_letter(penultimate_value)

            # Append the final letter value
            ciphered_text.append(final_value)

            count = count + 1


    # Then the new message is printed in the correct format
    encrypted_message = "".join(ciphered_text)
    chunks = [encrypted_message[i:i+4] for i in range(0, len(encrypted_message), 4)]

    cipher_text = " ".join(chunks)


    print(f"\nCiphered text: {cipher_text}")


if __name__ == '__main__':
    main()

# Number of possible settings for enigma:
# 5x4x3 x 26^3 x (26!)/(6! x 10! x 2^10)
# Roughly 1.59 x 10^20