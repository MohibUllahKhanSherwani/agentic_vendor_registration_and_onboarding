from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime


class OnboardingStatus(str, Enum):
    INVITATION_PENDING = "InvitationPending"
    INVITATION_SENT = "InvitationSent"
    IN_PROGRESS = "InProgress"
    INFORMATION_REQUIRED = "InformationRequired"
    DOCUMENTS_REQUIRED = "DocumentsRequired"
    UNDER_VALIDATION = "UnderValidation"
    READY_FOR_REVIEW = "ReadyForReview"
    COMPLETED = "Completed"


class CreateVendorOnboardingRequest(BaseModel):
    PRNumber: Optional[str] = None
    VendorName: str
    VendorEmail: EmailStr
    VendorPhone: str


class VendorOnboardingResponse(BaseModel):
    id: str
    PRNumber: Optional[str] = None
    VendorName: str
    VendorEmail: EmailStr
    VendorPhone: str
    CreatedBy: Optional[str] = None
    Status: OnboardingStatus
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
