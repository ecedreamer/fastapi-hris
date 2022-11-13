from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field
from datetime import date

from main.db_config import user_collection, employee_collection


class Employer(BaseModel):
    org_name: str
    org_logo: str | None
    location: str
    max_employee: int = 50


class User(BaseModel):
    email: EmailStr
    password: str
    status: str = "active"

    @classmethod
    async def create_user(cls, data):
        dict_data = jsonable_encoder(data)
        previous_user = await user_collection.find_one({"email": dict_data.get("email")})
        if previous_user:
            return False
        create_report = await user_collection.insert_one(dict_data)
        created_user = await user_collection.find_one({"_id": create_report.inserted_id})
        created_user["_id"] = str(created_user["_id"])
        return created_user

    @classmethod
    async def delete(cls, id_):
        print("Deleting user", id_)


class Employee(BaseModel):
    user_id: str
    employer_id: str
    role: str = Field(include=["Admin", "HR", "Employee"])
    full_name: str
    date_of_birth: date
    mobile: str
    status: str = "active"

    @classmethod
    async def create(cls, user_id, data):
        dict_data = jsonable_encoder(data)
        dict_data["user_id"] = user_id
        create_report = await employee_collection.insert_one(dict_data)
        created_employee = await employee_collection.find_one({"_id": create_report.inserted_id})
        created_employee["_id"] = str(created_employee["_id"])
        return created_employee
