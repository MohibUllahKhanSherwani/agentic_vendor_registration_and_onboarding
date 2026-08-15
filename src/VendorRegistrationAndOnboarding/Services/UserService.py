from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def get_all_users(self):
        users = await self.user_repository.get_all_users()
        return users