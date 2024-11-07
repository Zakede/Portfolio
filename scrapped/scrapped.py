from fasthtml.common import *
import requests, json, base64
from io import *

app, rt = fast_app(static_path="public", pico=False)

fonts = [
    "https://fonts.googleapis.com", 
    """https://fonts.gstatic.com" crossorigin""", 
    "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
]

@app.get("/")
def home():
    return (
        Link(rel="stylesheet", href=[*fonts]), 
        Link(rel="stylesheet", href="styles.css"), 
        Title("Mannat's Portfolio"), 
        Link(rel="icon", href="Assets/Rat.png"),
        Favicon(dark_icon="Assets/Rat.png", light_icon="Assets/Rat.png"),
        
    Nav(
        Div(
            A(Img(src="Assets/Rat.png", alt="Logo", cls="logo"), href="/", cls="logo-link"),
            Div(
                A("Home", href="/home", cls="nav-link"),
                A("Contact", href="/contact", cls="nav-link"),
                A("Bungus", href="/", cls="nav-link"),
                cls="nav-links"
            ),
            cls="nav-container"
        ),
        cls="navbar"
        ),
    
    Div(
        Div(
            H1("This IS My Silly Site :)", cls="front-text"),
            Img(src="Assets/Rat.png", alt="Front-Img", cls="front-img"),
            cls="front"
        )
    ),

    Div(Img(src="Assets/Rat.png", alt="Rat Image 1", cls="rat-img"),
    Img(src="Assets/Rat.png", alt="Rat Image 2", cls="rat-img"),
    Img(src="Assets/Rat.png", alt="Rat Image 3", cls="rat-img"),
    cls="rat")
    
    )


serve()
