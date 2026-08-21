import uuid
from VendorRegistrationAndOnboarding.Repositories.VendorOnboardingRepository import VendorOnboardingRepository
from VendorRegistrationAndOnboarding.DTOs.VendorOnboardingDTO import InitiateVendorOnboardingRequest


class VendorOnboardingService:
    def __init__(self):
        self.onboarding_repository = VendorOnboardingRepository()

    async def create_onboarding(self, data: InitiateVendorOnboardingRequest) -> dict:
        onboarding_id = str(uuid.uuid4())

        onboarding_data = {
            "_id": onboarding_id,
            "VendorName": data.VendorName,
            "VendorEmail": data.VendorEmail.lower().strip(),
            "VendorPhone": data.VendorPhone,
            "CreatedBy": data.CreatedBy,
            "Status": "InvitationSent",
            "UrgencyLevel": data.UrgencyLevel,
            "Comments": data.Comments,
        }

        created_id = await self.onboarding_repository.create_onboarding(onboarding_data)

        return {
            "success": True,
            "message": "Vendor onboarding request created successfully.",
            "data": {
                "_id": created_id,
                "Status": "InvitationSent"
            }
        }

    async def get_all_onboardings(self) -> list:
        return await self.onboarding_repository.get_all_onboardings()

    async def get_onboardings_by_created_by(self, created_by: str) -> list:
        return await self.onboarding_repository.get_onboardings_by_created_by(created_by)

