 # Tic-Tac-Toe Game

A classic Tic-Tac-Toe game where you play against an AI opponent. The AI uses the minimax algorithm to make unbeatable moves!

## Description

This is a Python-based Tic-Tac-Toe game where:
- You play as **X**
- The computer plays as **O**
- The AI uses the minimax algorithm, making it nearly impossible to beat

## How to Run

```bash
python tictactoe/tic_tac_toe.py
```

Or from the tictactoe directory:

```bash
cd tictactoe
python tic_tac_toe.py
```

## How to Play

1. The board is numbered 0-8, representing positions from top-left to bottom-right:
   ```
   0 | 1 | 2
   ---------
   3 | 4 | 5
   ---------
   6 | 7 | 8
   ```

2. When prompted, enter a number (0-8) to place your mark (X) in that position.

3. The game alternates between you and the AI until someone wins or the game ends in a draw.

## Features

- **AI Opponent**: Uses the minimax algorithm for optimal decision-making
- **Unbeatable AI**: The AI will either win or force a draw - can you beat it?
- **Simple CLI Interface**: Clean and easy-to-understand text-based interface
- **Win/Draw Detection**: Automatically detects winning conditions and draws

## Requirements

- Python 3.x

No external dependencies required!

## Game Rules

- Get three of your marks in a row (horizontally, vertically, or diagonally) to win
- If all positions are filled without a winner, the game is a draw
