"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate
taking stones until there are zero left.

The game of Nimm goes as follows:

1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""



def main():
    while True:
# while True has been added so that the game repeats after a round has been won by a player.


        num_stones = 20
        p1_turns = 20
        p2_turns = 20

# This section defines and assigns values to num_stones, p1_turns & p2_turns.


        while num_stones != 0:

            if p1_turns >= p2_turns:
                p1_turns -= 20
                print("There are " + str(num_stones) + " stones left.")
                stones_removed = int(input("Player 1, would you like to remove 1 or 2 stones?: "))

# This section will let the player with the greater number of turns to start, by default if the number of turns is the
# same, Player 1 will start first. Then, the player is asked for the number of stones that they want to remove which is
# stored in stones_removed.



                while stones_removed < 1 or stones_removed > 2:
                    stones_removed = int(input("Invalid input. Player 1, please enter either 1 or 2 stones: "))

# This section will repeatedly ask the player to input either one or two stones if they enter values
# that are not one or two.



                num_stones = num_stones - stones_removed

# This section then subtracts the number of stones the player wants to removed (stones_removed) from the
# total number of stones left (num_stones).


                if num_stones <= 0:
                    print("Congratulations! Player 2 has won this round.")
                    print(" ")
                    break

# This section considers the scenario when the number of stones left is zero after the player removes the stones and
# the winner is declared. The loop is then broken to end the game.



            if p2_turns >= p1_turns:

                p2_turns -= 20
                print("There are " + str(num_stones) + " stones left.")
                stones_removed = int(input("Player 2, would you like to remove 1 or 2 stones?: "))

                while stones_removed < 1 or stones_removed > 2:
                    stones_removed = int(input("Invalid input. Player 2, please enter either 1 or 2 stones: "))

                num_stones = num_stones - stones_removed

                if num_stones <= 0:
                    print("Congratulations! Player 1 has won this round.")
                    print(" ")
                    break

# This section is the same as above, but for the scenario when its Player 2's turn.



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
