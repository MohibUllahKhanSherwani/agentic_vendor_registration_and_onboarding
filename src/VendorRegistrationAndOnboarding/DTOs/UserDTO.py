from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from enum import Enum


class UserTypeEnum(str, Enum):
    SUPER_ADMIN = "SuperAdmin"
    DEPARTMENT_OWNER = "DepartmentOwner"
    VENDOR = "Vendor"


class DepartmentDetails(BaseModel):
    DepartmentId: str
    DepartmentName: Optional[str] = None


class BaseUser(BaseModel):
    Email: EmailStr
    UserType: UserTypeEnum
    Password: Optional[str] = None


class SuperAdmin(BaseUser):
    UserType: Literal[UserTypeEnum.SUPER_ADMIN] = UserTypeEnum.SUPER_ADMIN
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class DepartmentOwner(BaseUser):
    UserType: Literal[UserTypeEnum.DEPARTMENT_OWNER] = UserTypeEnum.DEPARTMENT_OWNER
    FirstName: str
    LastName: str
    Department: DepartmentDetails


class Vendor(BaseUser):
    UserType: Literal[UserTypeEnum.VENDOR] = UserTypeEnum.VENDOR

    # Vendor Information
    VendorName: Optional[str] = None
    Phone: Optional[str] = None
    CompanyName: Optional[str] = None
    VendorCategory: Optional[str] = None
    RegistrationNumber: Optional[str] = None
    TaxId: Optional[str] = None