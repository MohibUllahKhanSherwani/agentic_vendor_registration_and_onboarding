from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.UserService import UserService
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import Register, Login

router = APIRouter()
user_service = UserService()

@router.post("/signup")
async def signup(data: Register):
    return await user_service.create_user(data)
