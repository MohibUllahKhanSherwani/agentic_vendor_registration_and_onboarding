from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import datetime

class CreateVendorOnboardingRequest(BaseModel):
    VendorName: str
    VendorEmail: EmailStr
    VendorPhone: str

class VendorOnboardingResponse(BaseModel):
    id: str
    VendorName: str
    VendorEmail: EmailStr
    VendorPhone: str
    CreatedBy: Optional[str] = None
    Status: Literal["InvitationPending", "InvitationSent", "InProgress", "InformationRequired", "DocumentsRequired", "UnderValidation", "ReadyForReview", "Completed"] = "InvitationPending"
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
