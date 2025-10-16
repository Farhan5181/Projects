import numpy as np

board = np.array([[1,   2,   3], 
                  [4,   5,   6], 
                  [7,   8,   9]], dtype=object)
print(board)
turn_count = 0

def check_winner():
    # check all rows
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2]:
            print(f"🎉 The winner is {board[i, 0]}!")
            return True
        
    # check all column
    for i in range(3):
        if board[0, i] == board[1, i] == borad[2, i]:
            print(f"🎉 The winner is {board[0, i]}!")
            return True
    
    # check all diagonals
    if board[0, 0] == board[1 ,1] == board[2, 2]:
        print(f"🎉 The winner is {board[1, 1]}!")
        return True
    elif board[2, 0] == board[1, 1] == board[0, 2]:
        print(f"🎉 The winner is {board[1, 1]}!")
        return True

while True:

    check_winner()
    try:
        player1 = int(input("Player1 (x): Enter the position (1-9): "))
        if player1 in board:
            indx = np.where(board == player1)
            # np.where returns a tuple of arrays (rows, cols). Use it directly to index.
            print('found at', indx)
            board[indx] = 'x'
            turn_count += 1 
            print(board)
        else:
            print("⚠️ Invalid move! That position is already taken or doesn't exist. Try again.")
            continue 
    except ValueError:
        print("Enter a number ")
        continue

    if check_winner():
        break

    # Draw
    if turn_count == 9:
        print("\nIt's a draw! 🤝")
        break

    try:
        player2 = int(input("Player2 (o): Enter the position (1-9): "))
        if player2 in board:
            indx2 = np.where(board == player2)
            print("fount at: ", indx2)
            board[indx2] = 'o'
            turn_count += 1
            print(board)
        else:
            print("⚠️ Invalid move! That position is already taken or doesn't exist. Try again.")
            continue
    except ValueError:
        print("Enter a number ")
        continue

    if check_winner():
        break
    
    if turn_count == 9:
        print("\nIt's a draw! 🤝")
        break
    
