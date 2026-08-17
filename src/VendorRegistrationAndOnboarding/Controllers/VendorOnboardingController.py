from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.VendorOnboardingService import VendorOnboardingService
from VendorRegistrationAndOnboarding.DTOs.VendorOnboardingDTO import CreateVendorOnboardingRequest

router = APIRouter()
onboarding_service = VendorOnboardingService()


@router.post("", tags=["Vendor Onboarding"])
@router.post("/", tags=["Vendor Onboarding"])
async def create_onboarding(data: CreateVendorOnboardingRequest):
    return await onboarding_service.create_onboarding(data)
