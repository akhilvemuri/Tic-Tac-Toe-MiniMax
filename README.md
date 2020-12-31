# Tic-Tac-Toe
<h2>Introduction</h2>

This simple yet fun Tic-Tac-Toe project features a human player vs an unbeatable computer, which was created using the minimax algorithm. I recently came across this age-old artificial intelligence topic and found the theory cool enough to implement a game out of it.

<p align="center">
  <img src="https://github.com/akhilvemuri/tic-tac-toe-minimax/blob/master/assets/game.png" width="75%"/>
</p>

<h2>Understanding Minimax</h2>

The algorithm recursively generates a decision tree of all possible move combinations and follows the best path out of them all. The best move is a subjective term, so we define "best" as the maximized outcome (+1). In game theory and AI, these specific 2-player games are known mathematically as zero-sum games because they feature either a win (+1), a loss (-1), or a draw (0), in which we can easily define the maximized outcome as +1.

<p align="center">
  <img src="https://github.com/akhilvemuri/tic-tac-toe-minimax/blob/master/assets/understanding_minimax.png" width="90%"/>
</p>

At each depth in the decision tree, the maximizing and minimizing player alternate, simulating the switching of turns in a real game. And like the names max and min suggest, the max player returns the best evaluation (i.e. they want the max player to win), while the min player returns the worst evaluation (i.e. they want the max player to lose). This outcome then travels back up the tree until we obtain the most optimal evaluation for the current game state.

Another observation to recognize is that the number of child nodes decreases by 1 at each depth. This is because we reduce how many empty / playable spaces there are by 1 on each turn.

To see more intuitively how the theory behind this algorithm works, https://youtu.be/l-hh51ncgDI has a great introductory video on the concept.
