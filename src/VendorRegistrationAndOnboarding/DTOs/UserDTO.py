from pydantic import BaseModel, EmailStr
from typing import Literal, Optional

class DepartmentDetails(BaseModel):
    DepartmentId: str
    DepartmentName: Optional[str] = None

class BaseUser(BaseModel):
    Email: EmailStr
    UserType: Literal["SuperAdmin", "DepartmentOwner", "Vendor"]
    Password: Optional[str] = None

class SuperAdmin(BaseUser):
    UserType: Literal["SuperAdmin"] = "SuperAdmin"
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class DepartmentOwner(BaseUser):
    UserType: Literal["DepartmentOwner"] = "DepartmentOwner"
    FirstName: str
    LastName: str
    Department: DepartmentDetails

class Vendor(BaseUser):
    UserType: Literal["Vendor"] = "Vendor"

    # Vendor Information
    VendorName: Optional[str] = None
    Phone: Optional[str] = None
    CompanyName: Optional[str] = None
    VendorCategory: Optional[str] = None
    RegistrationNumber: Optional[str] = None
    TaxId: Optional[str] = None
