# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
   for check in row:
      print(tic_tac_toe_board[check], end=" ")
   print()