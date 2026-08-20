from fastapi import APIRouter
from VendorRegistrationAndOnboarding.Services.AuthService import AuthService
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import CreateDepartmentOwnerRequest

router = APIRouter()
auth_service = AuthService()

@router.post("/create-department-owner")
async def create_department_owner(data: CreateDepartmentOwnerRequest):
    return await auth_service.create_department_owner(data)

