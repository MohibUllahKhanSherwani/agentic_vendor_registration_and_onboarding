from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from VendorRegistrationAndOnboarding.Controllers import UserController

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

app.include_router(UserController.router, prefix="/users", tags=["Users"])