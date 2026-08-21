import uuid
from datetime import datetime, timedelta, timezone
from VendorRegistrationAndOnboarding.Repositories.VendorOnboardingRepository import VendorOnboardingRepository
from VendorRegistrationAndOnboarding.DTOs.VendorOnboardingDTO import InitiateVendorOnboardingRequest
from VendorRegistrationAndOnboarding.utils.utilities import generate_otp, send_otp_email


class VendorOnboardingService:
    def __init__(self):
        self.onboarding_repository = VendorOnboardingRepository()

    async def create_onboarding(self, data: InitiateVendorOnboardingRequest) -> dict:
        onboarding_id = str(uuid.uuid4())
        otp = generate_otp()
        otp_expiry = datetime.now(timezone.utc) + timedelta(minutes=10)

        onboarding_data = {
            "_id": onboarding_id,
            "VendorName": data.VendorName,
            "VendorEmail": data.VendorEmail.lower().strip(),
            "VendorPhone": data.VendorPhone,
            "CreatedBy": data.CreatedBy,
            "UrgencyLevel": data.UrgencyLevel,
            "Comments": data.Comments,
            "Status": "InvitationPending",
            "OTP": otp,
            "OTPExpiry": otp_expiry,
            "IsEmailVerified": False
        }

        created_id = await self.onboarding_repository.create_onboarding(onboarding_data)
        expiry_text = otp_expiry.strftime("%Y-%m-%d %H:%M:%S UTC")

        try:
            send_otp_email(data.VendorEmail, data.VendorName, otp, expiry_text)
        except Exception as error:
            return {
                "success": False,
                "message": f"Vendor onboarding created, but OTP email failed: {error}",
                "data": {"_id": created_id, "Status": "InvitationPending"}
            }

        await self.onboarding_repository.update_onboarding(
            created_id,
            {"Status": "InvitationSent"}
        )

        return {
            "success": True,
            "message": "Vendor onboarding request created successfully.",
            "data": {
                "_id": created_id,
                "Status": "InvitationSent",
                "OTPExpiry": expiry_text
            }
        }

    async def get_all_onboardings(self) -> list:
        return await self.onboarding_repository.get_all_onboardings()

    async def get_onboardings_by_created_by(self, created_by: str) -> list:
        return await self.onboarding_repository.get_onboardings_by_created_by(created_by)

