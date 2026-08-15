from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository
from VendorRegistrationAndOnboarding.utils.utilities import hash_password, verify_password
from VendorRegistrationAndOnboarding.DTOs.AuthDTO import Register, Login
import uuid

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, data: Register):
        user_id = str(uuid.uuid4())
        password = hash_password(data.Password)
        data.Email = data.Email.lower().strip()
        
        #Check existing user
        existing_user = await self.user_repository.get_user_by_email(data.Email)
        if existing_user:
                return {"success":False,"message":f"User with email {data.Email} already exists."}

        user_data = {
            "_id": user_id,
            "Email": data.Email,
            "FirstName": data.FirstName,
            "LastName": data.LastName,
            "UserType": "Vendor", # Will change it once to Admin to create one admin user and then will change it to Vendor
            "Password": password,
        }
        user_id = await self.user_repository.create_user(user_data)
        return {"success": True, "message": f"User created successfully with email: {data.Email}"}

    async def login_user(self, data: Login):
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