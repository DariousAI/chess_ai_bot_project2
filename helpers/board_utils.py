import chess.svg
from cairosvg import svg2png
from PIL import Image
from io import BytesIO
import streamlit as st

def display_board(board):
    """Render the chess board as an image in Streamlit."""
    board_svg = chess.svg.board(board)
    board_png = svg2png(bytestring=board_svg)
    img = Image.open(BytesIO(board_png))
    st.image(img)
