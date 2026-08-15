from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.UserService import UserService

router = APIRouter()
user_service = UserService()

@router.get("/get_all_users")
async def get_all_users():
    return await user_service.get_all_users()
