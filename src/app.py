import streamlit as st

from src.model import ImageModel
from src.view import ImageView

if __name__ == "__main__":
    app = ImageView(ImageModel())
    app.run()
