# Connect 4 AI with Alpha-Beta Pruning

A Python-based **Connect 4** game with multiple play modes, including **Player vs Player**, **Player vs AI**, and **AI vs AI**.  
The AI uses **Minimax with Alpha-Beta Pruning** and a **custom heuristic evaluation** for decision-making.

## Features

- 🎮 **Three Game Modes**:
  - Player vs Player (PvP)
  - Player vs AI (AI uses Alpha-Beta Pruning)
  - AI vs AI simulation
- 🧠 **AI Decision Making**:
  - Minimax Algorithm
  - Alpha-Beta Pruning for optimization
  - Heuristic evaluation for scoring moves
- 🖼 **Visual Board Representation** using emojis:
  - 🟢 Player X
  - 🔴 Player O
  - ⚪ Empty slot

## Requirements

- Python 3.7+
- No external dependencies required (only uses built-in Python modules)

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Connect4-AI.git
   cd Connect4-AI
   ```

2. **Run the game**:
   ```bash
   python Backtracking.py
   ```

3. **Choose a game mode** by modifying the last lines in `Backtracking.py`:
   ```python
   temp = Connect4()
   temp.start_game()           # Player vs AI
   # temp.start_game_PVP()     # Player vs Player
   # temp.start_game_AI_ONLY() # AI vs AI
   ```

## Game Rules

* Players take turns dropping a piece in one of the 7 columns.
* The first player to connect 4 of their pieces **horizontally**, **vertically**, or **diagonally** wins.
* If the board is full and no player has connected 4, the game ends in a draw.

## AI Logic

The AI evaluates moves using:

* **Win/Loss Detection**: Immediate wins or threats are prioritized.
* **Heuristic Scoring**: Positions are scored based on potential to connect 4.
* **Alpha-Beta Pruning**: Reduces search space for faster decision-making.

## Example Gameplay

```
⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪
⚪⚪⚪⚪⚪⚪⚪
🟢🔴🟢🔴⚪⚪⚪
1 2 3 4 5 6 7
```
