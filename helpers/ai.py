import random

def simple_ai_move(board):
    """AI makes a random legal move."""
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves) if legal_moves else None
