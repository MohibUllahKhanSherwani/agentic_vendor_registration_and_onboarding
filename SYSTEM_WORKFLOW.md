# Vendor Registration & Onboarding System Flow

## Core System Architecture & Roles

1. **Super Admin (Pre-seeded)**
   - **Role**: Platform Administrator.
   - **Pre-seeded Account**: Created via backend seed script (`seed_admin.py`).
   - **Primary Function**: Provisions Department Owners (`POST /admin/create-department-owner`).

2. **Department Owner**
   - **Role**: Departmental Manager (e.g. Procurement, IT, Legal).
   - **Provisioned By**: Super Admin.
   - **Primary Function**: Initiates vendor onboarding requests (`POST /vendor-onboarding/initiate-onboarding`) and monitors onboarding statuses.

3. **Vendor**
   - **Role**: External Vendor Account.
   - **Initiated By**: Department Owner.
   - **Primary Function**: Completes account registration / onboarding submission.

---

## Authentication & Authorization Model
- **Login Endpoint**: `POST /auth/login` (Accepts `Email` & `Password`).
- **Public Registration**: Disabled. Public sign-up is prohibited. Vendor registration occurs strictly via Department Owner onboarding invitations.

---

## API Controller Mapping

| Role | Allowed Actions | Endpoints |
|---|---|---|
| **SuperAdmin** | Create Department Owners, View All Users, View All Onboardings | `POST /admin/create-department-owner`<br>`GET /users/get_all_users`<br>`GET /vendor-onboarding/get-all-onboardings` |
| **DepartmentOwner** | Initiate Vendor Onboardings, View Users, View Onboardings | `POST /vendor-onboarding/initiate-onboarding`<br>`GET /vendor-onboarding/get-all-onboardings`<br>`GET /users/get_all_users` |
| **Vendor** | View Assigned Onboardings | `GET /vendor-onboarding/created-by/{created_by}` |
