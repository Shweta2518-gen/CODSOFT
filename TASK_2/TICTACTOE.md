# Tic-Tac-Toe Game

A classic Tic-Tac-Toe game written in Python where you play against an AI opponent using the Minimax algorithm.

## Overview

Tic-Tac-Toe is a two-player game where players take turns marking spaces in a 3×3 grid. In this version, you play as "X" against an AI opponent "O" that uses the Minimax algorithm to make optimal moves, making it nearly impossible to beat!

## Features

- **Player vs AI**: Play against a smart computer opponent
- **Minimax Algorithm**: The AI uses the Minimax algorithm to always make the best possible move
- **Console Interface**: Clean and simple text-based interface
- **Win/Draw Detection**: Automatically detects wins and draws
- **Input Validation**: Validates player moves to prevent invalid inputs

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the `TASK_2` directory
3. Run the game:

```bash
python tic_tac_toe.py
```

## How to Play

1. The game displays a 3×3 grid numbered 0-8:
   ```
   0 | 1 | 2
   ---------
   3 | 4 | 5
   ---------
   6 | 7 | 8
   ```

2. Enter a number (0-8) to place your mark ("X") in that position
3. The AI will then make its move ("O")
4. The game continues until someone wins or it's a draw

## Controls

- **Your Turn**: Enter a number from 0-8 to place your mark
- **AI Turn**: The AI automatically makes its move

## Winning Conditions

- 3 marks in a row horizontally, vertically, or diagonally
- The first player to get 3 in a row wins

## Game Rules

- You play as "X" and go first
- The AI plays as "O" and goes second
- Positions are numbered from 0 (top-left) to 8 (bottom-right)
- You cannot place a mark on an already occupied position

## Code Structure

- `print_board()`: Displays the current game board
- `check_winner(player)`: Checks if the specified player has won
- `is_draw()`: Checks if the game is a draw
- `player_move()`: Handles the player's input and move
- `minimax(is_maximizing)`: Implements the Minimax algorithm for AI decision making
- `ai_move()`: Makes the AI's move using Minimax
- `main()`: Main game loop

## AI Implementation

The AI uses the **Minimax algorithm**, a recursive decision-making algorithm commonly used in two-player games. It works by:

1. Simulating all possible future moves
2. Scoring each outcome (win = +1, loss = -1, draw = 0)
3. Assuming both players play optimally
4. Choosing the move that maximizes the AI's minimum gain

This makes the AI unbeatable - at best, you can only achieve a draw!

## License

This project is for educational purposes.

