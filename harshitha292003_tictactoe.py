#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    print("\n".join([" | ".join(board[i:i+3]) for i in range(0, 9, 3)]), "\n")

def check_win(board, player):
    return any(all(board[i] == player for i in line) for line in 
               [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])

def play_game():
    board, player = [str(i+1) for i in range(9)], 'X'
    while True:
        display_board(board)
        move = input(f"Player {player}, choose (1-9): ")
        if move in board:
            board[int(move)-1] = player
            if check_win(board, player):
                display_board(board); print(f"Player {player} wins!"); break
            if all(spot in 'XO' for spot in board):
                display_board(board); print("It's a tie!"); break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

play_game()


# In[2]:


def show_grid(grid):
    print("\n".join([" | ".join(grid[i:i+3]) for i in range(0, 9, 3)]), "\n")

def is_winner(grid, marker):
    patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(all(grid[i] == marker for i in pattern) for pattern in patterns)

def tic_tac_toe():
    grid, player = [str(i+1) for i in range(9)], 'X'
    while True:
        show_grid(grid)
        choice = input(f"Player {player}, pick a spot (1-9): ")
        if choice in grid:
            grid[int(choice)-1] = player
            if is_winner(grid, player):
                show_grid(grid); print(f"🎉 Player {player} wins!"); break
            if all(spot in 'XO' for spot in grid):
                show_grid(grid); print("🤝 It's a draw!"); break
            player = 'O' if player == 'X' else 'X'
        else:
            print("❌ Invalid move. Try again!")

tic_tac_toe()


# In[ ]:




