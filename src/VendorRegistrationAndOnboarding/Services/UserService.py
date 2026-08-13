from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository
from VendorRegistrationAndOnboarding.utils.utilities import hash_password, verify_password
from VendorRegistrationAndOnboarding.DTOs.UserDTO import BaseUser
import uuid

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, data: BaseUser):
        user_id = str(uuid.uuid4())
        password = hash_password(data.Password)
        data.Email = data.Email.lower().strip()
        
        #Check existing user
        existing_user = await self.user_repository.get_user_by_email(data.Email)
        if existing_user:
                return {"success":False,"message":f"User with email{data.Email} already exists."}
    
        user_data = {
            "_id": user_id,
            "Email": data.Email,
            "UserType": data.UserType, # Will change it once to Admin to create one admin user and then will change it to Vendor
            "Password": password,
        }
        user_id = await self.user_repository.create_user(user_data)
        return {"success": True, "message": f"User created successfully with ID: {user_id}"}