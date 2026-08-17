from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateDepartmentOwnerRequest(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr
    Password: str
    DepartmentName: Optional[str] = None
