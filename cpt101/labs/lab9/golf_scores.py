#!/usr/bin/env python
# Cory Parker
# CPT101
# Golf Scores
"""
1) Read each player's name and golf score as user input, saving these records
in a file named golf.txt (Each record will have a field for the player's name
and score)

2) Reads records from the golf.txt file and displays them
"""

# 1)
FILENAME = "golf.txt"

def write_data():  # Current is default path
    # ------------------------------------
    # Writes names of players and scores to file
    # ------------------------------------
    file = open(FILENAME, "w")    # Creates file object
    try:
        # User input for the number of golf players
        players = int(input("\nEnter number of players (integer):\n"))
        """
        ------------------------------------------------------------------------
        ValueError raised when function gets an argument of correct type but
        improper value
        ------------------------------------------------------------------------
        """
    except ValueError as ex:
        print(f"""\nLo Siento! You needed to type and integer\n
              (ノÒ益Ó)ノ彡▔▔▏\n""")
   
    for player in range(1, players+1):
        print("\nEnter player score for golfer: ", player)
        # User information
        player_name = input("\nEnter player's name: \n")
        player_score = int(input("\nEnter player's score: \n"))

        # Writing data to record
        file.write(player_name + ": ")
        try:
            file.write(str(player_score) + "\n")

        # If user doesn't eneter a valid integer, don't include
        except ValueError as ex:
            print(f"""
            \nOops!  You needed to enter an integer!\n
                  """)
            continue

    file.close()    # Closes file... 

def read_data():
    # Reads data from file
    file = open(FILENAME, "r")
    print(13*"=")
    print(f"{file.read()}", end="")
    print(13*"=")


def main():
    write_data()
    read_data()


if __name__ == "__main__":
    main()
