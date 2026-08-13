from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.UserService import UserService
from VendorRegistrationAndOnboarding.DTOs.UserDTO import BaseUser

router = APIRouter()
user_service = UserService()

@router.post("/signup")
async def signup(data: BaseUser):
    return await user_service.create_user(data)
