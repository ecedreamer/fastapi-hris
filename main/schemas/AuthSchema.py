from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date
from enum import Enum


class Role(Enum):
    admin = "Admin"
    hr = "HR"
    employee = "Employee"


class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)


class EmployeeSchema(BaseModel):
    employer_id: str
    role: str
    full_name: str
    date_of_birth: date
    mobile: str
    status: str = "active"

    @validator('role')
    def valid_roles(cls, value):
        if value not in ["Admin", "HR", "Employee"]:
            raise ValueError('role must be one of the "Admin", "HR", "Employee"')
        return value

