from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.AuthService import AuthService
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import LoginRequest

router = APIRouter()
auth_service = AuthService()

@router.post("/login")
async def login(data: LoginRequest):
    return await auth_service.login_user(data)