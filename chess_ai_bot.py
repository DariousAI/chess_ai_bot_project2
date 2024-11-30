import streamlit as st
import chess
from helpers.board_utils import display_board
from helpers.ai import simple_ai_move

# Initialize the Chess Board
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

st.title("Chess AI Bot Game")
st.write("Play chess against a simple AI!")

# Display the current board
display_board(st.session_state.board)

# User makes a move
user_move = st.text_input("Enter your move (e.g., e2e4):")
if st.button("Make Move"):
    try:
        move = chess.Move.from_uci(user_move)
        if move in st.session_state.board.legal_moves:
            st.session_state.board.push(move)

            # AI makes a move
            ai_move = simple_ai_move(st.session_state.board)
            if ai_move:
                st.session_state.board.push(ai_move)
            else:
                st.success("Congratulations! You beat the AI!")
        else:
            st.error("Invalid move! Try again.")
    except:
        st.error("Invalid input. Use UCI format (e.g., e2e4).")

# Check for game end
if st.session_state.board.is_game_over():
    if st.session_state.board.is_checkmate():
        st.success("Checkmate! Game over.")
    elif st.session_state.board.is_stalemate():
        st.info("Stalemate! Game over.")
    elif st.session_state.board.is_insufficient_material():
        st.info("Draw! Insufficient material.")
    else:
        st.info("Game over.")

# Reset button
if st.button("Reset Game"):
    st.session_state.board = chess.Board()
