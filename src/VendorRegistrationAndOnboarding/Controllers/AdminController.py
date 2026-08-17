from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.UserService import UserService
from VendorRegistrationAndOnboarding.DTOs.DepartmentOwnerDTO import CreateDepartmentOwnerRequest

router = APIRouter()
user_service = UserService()


@router.post("/department-owners", tags=["Admin"])
async def create_department_owner(data: CreateDepartmentOwnerRequest):
    return await user_service.create_department_owner(data)
