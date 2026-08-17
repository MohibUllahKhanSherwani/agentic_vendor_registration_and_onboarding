from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.AuthService import AuthService
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import Register, Login

router = APIRouter()
auth_service = AuthService()

@router.post("/signup")
async def signup(data: Register):
    return await auth_service.create_vendor(data)

@router.post("/login")
async def login(data: Login):
    return await auth_service.login_user(data)