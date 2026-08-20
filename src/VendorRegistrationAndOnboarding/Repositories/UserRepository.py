from datetime import datetime
from VendorRegistrationAndOnboarding.MongoHandler.Handler import db

class UserRepository:
    def __init__(self):
        self.collection = db.Users

    async def create_user(self, user_data):
        user_data["CreatedAt"] = datetime.utcnow()
        user_data["UpdatedAt"] = datetime.utcnow()
        user_data["IsDeleted"] = False

        result =  self.collection.insert_one(user_data)

        return str(result.inserted_id)

    async def get_user_by_id(self, user_id: str):
        results = self.collection.find_one({"_id": user_id, "IsDeleted": False})
        return results

    async def get_user_by_email(self, email: str):
        results = self.collection.find_one({"Email": email, "IsDeleted": False})
        return results      

    async def get_all_users(self):
        results = self.collection.find({"IsDeleted": False})
        return list(results)

    async def get_users_by_type(self, user_type: str):
        if user_type == "SuperAdmin":
            return []
        results = self.collection.find({"UserType": user_type, "IsDeleted": False})
        return list(results)