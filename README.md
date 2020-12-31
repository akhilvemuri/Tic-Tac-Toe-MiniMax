# Tic-Tac-Toe
<h2>Introduction</h2>
This simple tic-tac-toe project features an unbeatable AI, which uses the minimax algorithm. I recently learned about how this algorithm works and found the theory cool enough to implement a game out of it.

<h2>Understanding Minimax</h2>
This recursive search algorithm finds the best move out of all moves possible to play in order for the computer to either win or draw the game. In artificial intelligence or game theory, these specific 2-player games are known mathematically as zero-sum games because they feature either a winner (+1), a loser (-1), or a draw (0) outcome.

We define the maximizing player as the player trying to maximize the outcome, and the minimizing player as the player trying to minimize the outcome. In our case, the computer is maximizing while the human is minimizing, although it doesn't matter who is assigned to which role. At each depth in the decision tree, the player is switched
