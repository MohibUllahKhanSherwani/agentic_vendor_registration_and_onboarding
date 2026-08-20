from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository
from VendorRegistrationAndOnboarding.utils.utilities import hash_password, verify_password
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import LoginRequest, CreateDepartmentOwnerRequest
import uuid

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

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
