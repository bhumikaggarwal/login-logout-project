from fastapi import FastAPI, Request , Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.registration import UserRegistartion



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def validate_registration(name: str, email: str, password: str):
    errors = {}

    # Validate name
    if not name.strip():
        errors["name"] = "Name is required."

    # Validate email
    if not email.strip():
        errors["email"] = "Email is required."
    elif "@" not in email:
        errors["email"] = "Invalid email format."

    # Validate password
    if not password:
        errors["password"] = "Password is required."
    elif len(password) < 8:
        errors["password"] = "Password must be at least 8 characters long."



    return errors

@app.get("/", name="home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
             request = request,
             name = "auth/register.html",
             context = {
                 "form_data": {}
             }
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
    errors = validate_registration(name, email, password)


    if errors:
        return templates.TemplateResponse(
            request=request,
            name="auth/register.html",
            context= {
                "errors": errors,
            },
            status_code=422
        )


    return templates.TemplateResponse(
        request=request,
        name="auth/register.html",
        context={
            "errors": {},
            "message": f"User {name} registered successfully with email {email}."
        }
    )

@app.post("/api/register")
def register_user(user: UserRegistartion):
    return {"message": f"User {user.name} registered successfully with email {user.email}."}

@app.get("/login_page", name="login_page", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/login.html",
        context={}
    )
print(validate_registration("John Doe", "johnexample.com", "pad123"))
