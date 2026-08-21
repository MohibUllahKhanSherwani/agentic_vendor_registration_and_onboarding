from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository
from VendorRegistrationAndOnboarding.Repositories.VendorOnboardingRepository import VendorOnboardingRepository
from VendorRegistrationAndOnboarding.utils.utilities import hash_password, verify_password, generate_otp, send_otp_email
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import LoginRequest, CreateDepartmentOwnerRequest
from datetime import datetime, timezone, timedelta
import uuid

class AuthService:

    
    def _format_otp_expiry(self, otp_expiry):
        if not otp_expiry:
            return None
        if otp_expiry.tzinfo is None:
            otp_expiry = otp_expiry.replace(tzinfo=timezone.utc)
        return otp_expiry.strftime("%Y-%m-%d %H:%M:%S UTC")


    def __init__(self):
        self.user_repository = UserRepository()
        self.onboarding_repository = VendorOnboardingRepository()

    async def resend_otp(self, email: str):
        email = email.lower().strip()
        onboarding = await self.onboarding_repository.get_onboarding_by_email(email)
        if not onboarding:
            return {"success": False, "message": "Onboarding email not found"}

        otp = generate_otp()
        otp_expiry = datetime.now(timezone.utc) + timedelta(minutes=10)
        updated = await self.onboarding_repository.update_otp(
            email, otp, otp_expiry
        )
        if not updated:
            return {"success": False, "message": "Cannot generate OTP"}

        expiry_text = self._format_otp_expiry(otp_expiry)
        try:
            send_otp_email(email, onboarding["VendorName"], otp, expiry_text)
        except Exception as error:
            return {"success": False, "message": f"OTP email failed: {error}"}

        return {
            "success": True,
            "message": "OTP sent successfully",
            "OTPExpiry": expiry_text
        }

    async def validate_otp(self,email,otp):
        email = email.lower().strip()
        onboarding = await self.onboarding_repository.get_onboarding_by_email(email)
        if not onboarding:
            return {"success": False, "message": "Onboarding email not found"}

        expiry = onboarding.get("OTPExpiry")
        if not expiry:
            return {
                "success": False,
                "message": "OTP has expired. Please request a new one."
            }
        if expiry.tzinfo is None:
            expiry = expiry.replace(tzinfo=timezone.utc)
        if datetime.now(timezone.utc) > expiry:
            return {
                "success": False,
                "message": "OTP has expired. Please request a new one."
            }
        if str(otp) != str(onboarding["OTP"]):
            return {"success": False, "message": "Invalid OTP"}
        if not await self.onboarding_repository.verify_email(email):
            return {"success": False, "message": "Cannot verify email"}
        return {"success": True, "message": "Email verified successfully"}


    async def create_department_owner(self, data: CreateDepartmentOwnerRequest):
        email = data.Email.lower().strip()
        existing_user = await self.user_repository.get_user_by_email(email)
        if existing_user:
            return {"success": False, "message": f"User with email {email} already exists."}

        user_id = str(uuid.uuid4())
        hashed_pwd = hash_password(data.Password)
        dept_id = str(uuid.uuid4())

        user_data = {
            "_id": user_id,
            "Email": email,
            "FirstName": data.FirstName,
            "LastName": data.LastName,
            "UserType": "DepartmentOwner",
            "Password": hashed_pwd,
            "Department": {
                "DepartmentId": dept_id,
                "DepartmentName": data.DepartmentName
            }
        }

        created_id = await self.user_repository.create_user(user_data)
        return {
            "success": True,
            "message": f"Department Owner created successfully with email: {email}",
            "data": {
                "UserId": created_id,
                "Email": email,
                "UserType": "DepartmentOwner",
                "DepartmentId": dept_id
            }
        }

    async def login_user(self, data: LoginRequest):
        data.Email = data.Email.lower().strip()
        user = await self.user_repository.get_user_by_email(data.Email)

        if not user:
            return {"success": False, "message": f"User with email {data.Email} does not exist."}

        if not verify_password(data.Password, user["Password"]):
            return {"success": False, "message": "Invalid password."}

        return {
            "success": True, 
            "message": "Login successful.", 
            "user": {
                "UserId": user["_id"],
                "Email": user["Email"],
                "FirstName": user["FirstName"],
                "LastName": user["LastName"],
                "UserType": user["UserType"]
                    }
        }
