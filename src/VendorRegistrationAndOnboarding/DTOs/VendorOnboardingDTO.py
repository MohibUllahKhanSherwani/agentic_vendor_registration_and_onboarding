from pydantic import BaseModel, EmailStr

class InitiateVendorOnboardingRequest(BaseModel):
    VendorName: str
    VendorEmail: EmailStr
    VendorPhone: str
    CreatedBy: str