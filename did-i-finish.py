#Code Wars Did I Finish my Sudoku? (5kyu)
board1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

board2 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]
#Checks to see if a sudoko board has been completed successfully
def done_or_not(board):
    #construct lists of numbers in columns and adds to board list
    columns = [[], [], [], [], [], [], [], [], []]
    for index, column in enumerate(columns):
        for num in range(9):
            column.append(board[num][index])
    board.extend(columns)
    #constructs lists of numbers in the 9 blocks and adds to board list
    blocks = []
    block_ranges = [
        [0, 3, 0, 3],
        [0, 3, 3, 6],
        [0, 3, 6, 9],
        [3, 6, 0, 3],
        [3, 6, 3, 6],
        [3, 6, 6, 9],
        [6, 9, 0, 3],
        [6, 9, 3, 6],
        [6, 9, 6, 9]
    ]
    for lst in block_ranges:
        block = []
        for row in range(lst[0], lst[1]):
            for col in range(lst[2], lst[3]):
                block.append(board[row][col])
        blocks.append(block)
    board.extend(blocks)
    #checks each list of nums(rows, columns,  blocks) for nums 1-9 for successful completion
    for row in board:
        sorted_row = sorted(row)
        for index, num in enumerate(sorted_row):
            if num != index + 1:
                return 'Try again!'
    return 'Finished!'



print(done_or_not(board1))
print(done_or_not(board2))