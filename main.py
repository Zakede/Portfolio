from fasthtml.common import *
import requests, json, base64
from io import *

app, rt = fast_app(static_path="public", pico=False)

skills = ["Design", "Python", "JavaScript", "HTML/CSS", "Adobe Suite", "Figma", "Automation"]

@app.get("/")
def home():
    return (
        #Meta Tags
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Mannat's Portfolio - Graphic Designer and Python Developer"),
        Meta(name="keywords", content="Graphic Design, Python, Portfolio, Web Development, Mannat"),
        Meta(name="author", content="Mannat"),
        
        #Links
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="true"),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Funnel+Sans:ital,wght@0,300..800;1,300..800&display=swap"),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Anton&display=swap"),
        Link(rel="stylesheet", href="styles.css"), 
        
        Title("Mannat's Portfolio"), 
        Link(rel="icon", href="Assets/Logo.svg"),
        Favicon(dark_icon="Assets/Logo.svg", light_icon="Assets/Logo.svg"),
        
    Nav(
        Div(
            A(Img(src="Assets/Logo.svg", alt="Logo", cls="logo", draggable="false"), href="/", cls="logo-link"),
            Div(
                A("Home", href="/home", cls="nav-link"),
                A("Contact", href="/contact", cls="nav-link"),
                A("Bungus", href="/", cls="nav-link"),
                cls="nav-links"
            ),
            cls="nav-container",
        ),
        Br(),
        cls="navbar"
        ),
    
    Div(
        Div(
            P("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus  
            maximus id velit id condimentum. Fusce dapibus lacus sit amet nunc fringilla commodo. 
            Integer lobortis odio vitae leo porttitor, nec luctus velit volutpat. Donec tristique faucibus enim at varius. 
            Nam sollicitudin euismod erat, eu porttitor massa cursus vitae. Maecenas dictum vitae odio vitae fermentum. 
            Morbi varius eros a lorem pulvinar tincidunt. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 
            Ut eleifend pulvinar interdum. Cras vehicula, orci in malesuada lacinia, neque ipsum scelerisque ligula, nec malesuada augue magna at ante. 
            Nullam quis elit porta, volutpat dui non, lacinia nisi. Maecenas vel feugiat leo. Suspendisse potenti."""), 
            cls="panel-text"
        ),
        Div(
            A(Img(src="Assets/Rat.png", alt="Logo", cls="logo", draggable="false"), href="/", cls="logo-link"),
            cls="panel-logo-container"
        ), 
        cls="front-panel"
    ),
    

    Div(
        Div(
            *[Div(skill, cls="skill-item") for skill in skills], 
            cls="skill-bar"
        ),
        cls="skills-section"
    )



    
    
    
    )
    
serve()