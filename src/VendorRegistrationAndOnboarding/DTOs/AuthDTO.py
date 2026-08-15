from pydantic import BaseModel, EmailStr


class Register(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr
    Password: str

class Login(BaseModel):
    Email: EmailStr
    Password: str