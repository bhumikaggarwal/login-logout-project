from pydantic import BaseModel,Field,field_validator

class UserRegistartion(BaseModel):

    name: str = Field(..., min_length=2, max_length=50)
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Name must contain atleast 2 characters.")
        return value

    email: str

    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, value):
        if isinstance(value, str):
            value = value.strip().lower()

            if "@" not in value:
                raise ValueError("Invalid email format.")

        return value

    password: str = Field(..., min_length=8)
    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must have at least one digit.")
        return value
