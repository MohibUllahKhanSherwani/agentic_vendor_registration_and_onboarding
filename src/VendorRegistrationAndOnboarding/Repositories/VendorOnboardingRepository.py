from datetime import datetime
from VendorRegistrationAndOnboarding.MongoHandler.Handler import db


class VendorOnboardingRepository:
    def __init__(self):
        self.collection = db.VendorOnboardings

    async def create_onboarding(self, onboarding_data: dict) -> str:
        now = datetime.utcnow()
        onboarding_data["CreatedAt"] = now
        onboarding_data["UpdatedAt"] = now
        onboarding_data["IsDeleted"] = False

        result = self.collection.insert_one(onboarding_data)
        return str(result.inserted_id)

    async def get_onboarding_by_id(self, onboarding_id: str) -> dict:
        return self.collection.find_one({"_id": onboarding_id, "IsDeleted": False})

    async def get_all_onboardings(self) -> list:
        return list(self.collection.find({"IsDeleted": False}))

    async def get_onboardings_by_created_by(self, created_by: str) -> list:
        return list(self.collection.find({"CreatedBy": created_by, "IsDeleted": False}))

    async def update_onboarding(self, onboarding_id: str, update_data: dict) -> bool:
        update_data["UpdatedAt"] = datetime.utcnow()
        result = self.collection.update_one(
            {"_id": onboarding_id, "IsDeleted": False},
            {"$set": update_data}
        )
        return result.modified_count

