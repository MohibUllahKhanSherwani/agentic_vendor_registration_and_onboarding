from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from VendorRegistrationAndOnboarding.Controllers import AuthController, UserController, AdminController, VendorOnboardingController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health", tags=["health"])
def health():
    return {"status": "Service is ok"}

app.include_router(AuthController.router, prefix="/auth", tags=["Authentication"])
app.include_router(UserController.router, prefix="/users", tags=["Users"])
app.include_router(AdminController.router, prefix="/admin", tags=["Admin"])
app.include_router(VendorOnboardingController.router, prefix="/vendor-onboarding", tags=["Vendor Onboarding"])
