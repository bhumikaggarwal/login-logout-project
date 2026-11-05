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
    name: str = Form(min_length=2, max_length=50),
    email: str = Form(),
    password: str = Form(min_length=8)
):
    return templates.TemplateResponse(
        request=request,
        name="auth/register.html",
        context={
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
