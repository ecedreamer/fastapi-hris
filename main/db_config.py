from motor import motor_asyncio
from bson import ObjectId

MONGO_URL = "mongodb://localhost:27017"
client = motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.fastapi_hrm

department_collection = database.get_collection("department")
user_collection = database.get_collection("user")
employee_collection = database.get_collection("employee")


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
