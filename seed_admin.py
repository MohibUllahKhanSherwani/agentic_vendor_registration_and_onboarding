import asyncio
import uuid
from VendorRegistrationAndOnboarding.Repositories.UserRepository import UserRepository
from VendorRegistrationAndOnboarding.utils.utilities import hash_password

async def seed_admin():
    user_repository = UserRepository()
    admin_email = "admin@vendorconnect.com"
    
    existing = await user_repository.get_user_by_email(admin_email)
    if existing:
        print(f"SuperAdmin with email {admin_email} already exists.")
        return

    admin_data = {
        "_id": str(uuid.uuid4()),
        "Email": admin_email,
        "FirstName": "Mohib",
        "LastName": "Khan",
        "UserType": "SuperAdmin",
        "Password": hash_password("Admin@12345"),
    }
    created_id = await user_repository.create_user(admin_data)
    print(f"SuperAdmin seeded successfully with ID: {created_id} (Email: {admin_email})")

if __name__ == "__main__":
    asyncio.run(seed_admin())
