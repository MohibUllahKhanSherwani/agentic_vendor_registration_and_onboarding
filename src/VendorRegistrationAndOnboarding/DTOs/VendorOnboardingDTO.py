from pydantic import BaseModel, EmailStr
from typing import Literal, Optional

class InitiateVendorOnboardingRequest(BaseModel):
    VendorName: str #Company name
    VendorEmail: EmailStr
    VendorPhone: str
    CreatedBy: str
    UrgencyLevel: Literal["High", "Medium", "Low"] = "Medium"
    Comments: Optional[str] = None