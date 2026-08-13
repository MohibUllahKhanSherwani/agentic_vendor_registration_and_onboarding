from pydantic import BaseModel, EmailStr
from typing import Literal, Optional


class BaseUser(BaseModel):
    Email: EmailStr
    UserType: Literal["SuperAdmin", "Vendor"]
    Password: str

class SuperAdmin(BaseUser):
    UserType: Literal["SuperAdmin"] = "SuperAdmin"

class Vendor(BaseUser):
    UserType: Literal["Vendor"] = "Vendor"

    # Vendor Information
    CompanyName: Optional[str] = None
    VendorCategory: Optional[str] = None
    Phone: Optional[str] = None
    RegistrationNumber: Optional[str] = None
    TaxId: Optional[str] = None