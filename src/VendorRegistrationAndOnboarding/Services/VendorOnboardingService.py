import uuid
from VendorRegistrationAndOnboarding.Repositories.VendorOnboardingRepository import VendorOnboardingRepository
from VendorRegistrationAndOnboarding.DTOs.VendorOnboardingDTO import CreateVendorOnboardingRequest


class VendorOnboardingService:
    def __init__(self):
        self.onboarding_repository = VendorOnboardingRepository()

    async def create_onboarding(self, data: CreateVendorOnboardingRequest, created_by: str = None) -> dict:
        onboarding_id = str(uuid.uuid4())

        onboarding_data = {
            "_id": onboarding_id,
            "VendorName": data.VendorName,
            "VendorEmail": data.VendorEmail.lower().strip(),
            "VendorPhone": data.VendorPhone,
            "CreatedBy": data.CreatedBy,
            "Status": "InvitationPending"
        }

        created_id = await self.onboarding_repository.create_onboarding(onboarding_data)

        return {
            "success": True,
            "message": "Vendor onboarding request created successfully.",
            "data": {
                "_id": created_id,
                "Status": "InvitationPending"
            }
        }

    async def get_all_onboardings(self) -> list:
        return await self.onboarding_repository.get_all_onboardings()

    async def get_onboardings_by_created_by(self, created_by: str) -> list:
        return await self.onboarding_repository.get_onboardings_by_created_by(created_by)

