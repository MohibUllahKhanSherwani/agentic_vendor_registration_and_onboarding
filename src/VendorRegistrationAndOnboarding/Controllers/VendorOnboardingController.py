from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.VendorOnboardingService import VendorOnboardingService
from VendorRegistrationAndOnboarding.DTOs.VendorOnboardingDTO import InitiateVendorOnboardingRequest

router = APIRouter()
onboarding_service = VendorOnboardingService()

@router.post("/initiate-onboarding")
async def initiate_onboarding(data: InitiateVendorOnboardingRequest):
    return await onboarding_service.create_onboarding(data)

@router.get("/get-all-onboardings")
async def get_all_onboardings():
    return await onboarding_service.get_all_onboardings()

@router.get("/created-by/{created_by}")
async def get_onboardings_by_created_by(created_by: str):
    return await onboarding_service.get_onboardings_by_created_by(created_by)


