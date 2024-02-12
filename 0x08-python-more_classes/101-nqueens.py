#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of boards that are  representing the chessboard.
    columns (list):  list of columns  containing solutions.

columns are represented in the format [[r, f], [r, f], [r, f], [r, f]]
where `r` and `f` represent the count and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [count.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_column(board):
    """Return the list of lists representation of a solved chessboard."""
    column = []
    for r in range(len(board)):
        for f in range(len(board)):
            if board[r][f] == "Q":
                column.append([r, f])
                break
    return (column)


def xout(board, count, coll):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list):  current working chessboard.
        count (int): count row where a queen was last played.
        coll (int):  column where a queen was last played.
    """
    # X out all forward spots
    for f in range(coll + 1, len(board)):
        board[count][f] = "x"
    # X out all backwards spots
    for f in range(coll - 1, -1, -1):
        board[count]f] = "x"
    # X out all spots below
    for r in range(count + 1, len(board)):
        board[r][coll] = "x"
    # X out all spots above
    for r in range(count - 1, -1, -1):
        board[r][coll] = "x"
    # X out all spots diagonally down to the right
    f = coll + 1
    for r in range(count + 1, len(board)):
        if f >= len(board):
            break
        board[r][f] = "x"
        f += 1
    # X out all spots diagonally up to the left
    f = coll - 1
    for r in range(row - 1, -1, -1):
        if f < 0:
            break
        board[r][f]
        f -= 1
    # X out all spots diagonally up to the right
    f = coll + 1
    for r in range(count - 1, -1, -1):
        if f >= len(board):
            break
        board[r][f] = "x"
        f += 1
    # X out all spots diagonally down to the left
    f = coll - 1
    for r in range(count + 1, len(board)):
        if f < 0:
            break
        board[r][f] = "x"
        f -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The number of working chessboard.
        row (int): The current working row.
        queens (int): Current number of placed queens.
        column (list): Columns list of solutions
    Returns:
        column
    """
    if queens == len(board):
        column.append(draw_column(board))
        return (column)

    for c in range(len(board)):
        if board[count][f] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[count][f] = "Q"
            parameter(tmp_board, count, f)
            column = recursive_solved(tmp_per, count + 1,
                                        queens + 1, column)

    return (column)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    column = recursive_solved(board, 0, 0, [])
    for line in column:
        print(line)
