from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.AuthService import AuthService
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import LoginRequest, VerifyOTPRequest

router = APIRouter()
auth_service = AuthService()

@router.post("/login")
async def login(data: LoginRequest):
    return await auth_service.login_user(data)

@router.post("/resend_otp")
async def resend_otp(data: VerifyOTPRequest):
    return await auth_service.resend_otp(data.Email)

@router.post("/verify_otp")
async def verify_otp(data: VerifyOTPRequest):
    return await auth_service.validate_otp(data.Email, data.Otp)