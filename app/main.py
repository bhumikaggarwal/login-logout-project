from fastapi import FastAPI, Request , Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", name="home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
             request = request,
             name = "auth/register.html",
             context = {}
    )

@app.get("/register_page", name="register_page", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
             request = request,
             name = "auth/register.html",
             context = {}
    )

@app.post("/register")
def register(
    request: Request,
    name: str = Form(default=""),
    email: str = Form(default=""),
    password: str = Form(default="")
):
    errors = {}

    #validate name
    if not name:
        errors["name"] = "Name is required."

    #validate email
    if not email:
        errors["email"] = "Email is required."
    elif "@" not in email:
        errors["email"] = "Invalid email format."

    #validate password
    if not password:
        errors["password"] = "Password is required."
    elif len(password) < 8:
        errors["password"] = "Password must be at least 8 characters long."


    if errors:
        return templates.TemplateResponse(
            request=request,
            name="auth/register.html",
            context= {
                "errors": errors,
                "form_data": {
                    "name": name,
                    "email": email
                }
            },
            status_code=422
        )


    return templates.TemplateResponse(
        request=request,
        name="auth/register.html",
        context={
            "errors": {},
            "form_data": {},
            "message": f"User {name} registered successfully with email {email}."
        }
    )

@app.get("/login_page", name="login_page", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/login.html",
        context={}
    )
