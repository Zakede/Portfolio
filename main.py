from fasthtml.common import *
import requests, json, base64
from discord_webhook import DiscordWebhook
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
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Jomhuria&display=swap"),
        
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
        cls="navbar fade-in"
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
        cls="front-panel fade-in"
    ),
    

    Div(
        Div(
            *[Div(skill, cls="skill-item") for skill in skills], 
            cls="skill-bar"
        ),
        cls="skills-section fade-in"
    ),
    
    Div(
        H1("Check Out My Works", cls="carousel-title"),
        Div(
            Img(src="Assets/Rat.png", alt="Image 1", cls="carousel-item"),
            Img(src="Assets/Logo.svg", alt="Image 2", cls="carousel-item"),
            Img(src="Assets/Rat.png", alt="Image 3", cls="carousel-item"),
            cls="carousel-container"
        ),
        cls="carousel fade-in",
    ), Script(src="carousel.js"),
    
    A(H1("Check For More!"), cls="carousel-link fade-in", href="/portfolio"),

    Div(
        Div(
        H1("Want To Work Together?", cls="form-title"),
        H1("Contact Me!", cls="form-title-lower"),
        Div(
            Form(method="post", action="/send")(
                Div(
                    Label("Name", for_attr="name", cls="form-label"),
                    Input(type="text", id="name", name="name", cls="form-input"),
                    cls="form-group"
                ),
                Div(
                    Label("Email", for_attr="email", cls="form-label"),
                    Input(type="email", id="email", name="email", cls="form-input"),
                    cls="form-group"
                ),
                Div(
                    Label("Enquiry", for_attr="enquiry", cls="form-label"),
                    Textarea(
                        id="enquiry", 
                        name="enquiry", 
                        rows="4", 
                        cls="form-textarea", 
                        maxlength="200",
                    ),
                    cls="form-group"
                ),
                Button("Send", type="submit", cls="form-submit"),
                cls="contact-form"
            ),
            cls="contact-form-container"
            ),cls="contact-inputs"
        ), cls="contact-container"
    ),
    
    

    )
    
@app.post("/send")
async def upload(request: Request):
    form = await request.form()
    name = form.get("name")
    email =  form.get("emaill")
    enquiry = form.get("enquiry")

    mail = (f""" ``` {name} \n {email} \n {enquiry}```""")
    url = "https://discord.com/api/webhooks/1304743185876254720/8WGrZVH-GDdlSOlxExSsOrdhkipzdd6_ergIBgbjzpNGrwkZe4aIjsuXr5vZMknW-LXS"
    
    webhook = DiscordWebhook(url=f"{url}", content=f"{mail}")
    response = webhook.execute()
    
    if response.status_code == 200:
        return (
            Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Jomhuria&display=swap"), 
            Link(rel="stylesheet", href="styles_send.css"), H1("I've Recived Your Mail!"))
        
    else:
        return (
            Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Jomhuria&display=swap"), 
            Link(rel="stylesheet", href="styles_send.css"), H1("Please Try Again!"))
    
     
serve()