from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def get_all_users(self):
        users = await self.user_repository.get_all_users()
        return users

    async def get_department_owners(self):
        department_owners = await self.user_repository.get_users_by_type("DepartmentOwner")
        return department_owners

    async def get_vendors(self):
        vendors = await self.user_repository.get_users_by_type("Vendor")
        return vendors


