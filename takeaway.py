# There’s a game, “takeaway”, that is played by two players, using a number of stones.

# The first player goes first. She can take 2, 3, or 5 stones from the pool. The second player goes next; she can also remove 2, 3, or 5 stones. The first player then goes, and so on.

# If a player is unable to move (there are fewer than 2 stones), they lose.

# Your Challenge
# Imagine that both players have “perfect play” — that is, they always make the best possible move. Then, you can absolutely determine who would win a game with n stones.


def can_win(stones):
    """Retruns True if player one can win"""
    
    options = [5, 3, 2]
    # Test each possible path for first move option
    for option in options:
        print(f'testing first move: {option}')
        # As long as first move is less than total stones...
        if option <= stones:
            # first move will be option
            # we will append each move to this list
            moves = [option]
            current = stones - option
            print(f'option: {option} moves: {moves} current: {current}')
            # now test all additional moves in a while loop
            while current >= 2:
                while current >= 5:
                    moves.append(5)
                    current -= 5
                    print(f'moves {moves} stones remaining {current}')
                while current >= 3:
                    moves.append(3)
                    current -= 3
                    print(f'moves {moves} stones remaining {current}')
                while current >= 2:
                    moves.append(2)
                    current -= 2
                    print(f'moves {moves} stones remaining {current}')
            # odd number of moves means that player one wins
            # if even, for loop will not break and will test the next "first move" option
            if len(moves) % 2 != 0:
                return True
    return False



# if __name__ == "__main__":
#     import doctest
#     if doctest.testmod().failed == 0:
#         print('\n✨ ALL TESTS PASSED!\n')