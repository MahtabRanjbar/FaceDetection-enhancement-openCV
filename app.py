import streamlit as st

from model import ImageModel
from view import ImageView

if __name__ == "__main__":
    app = ImageView(ImageModel())
    app.run()
