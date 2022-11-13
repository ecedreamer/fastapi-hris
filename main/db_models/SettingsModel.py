from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from bson import ObjectId
from ..db_config import PyObjectId, department_collection


class Department(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    employer_id: str
    department: str
    status: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    async def get_list(cls):
        departments = [cls(**department) async for department in department_collection.find()]
        return departments

    @classmethod
    async def get_one(cls, id_):
        department = await department_collection.find_one({"_id": PyObjectId(id_)})
        if not department:
            return None
        return cls(**department)

    @classmethod
    async def create(cls, data):
        created_department = await department_collection.insert_one(jsonable_encoder(data))
        new_department = await cls.get_one(str(created_department.inserted_id))
        return new_department

    @classmethod
    async def update(cls, id_, data):
        changed_data = {k: v for k, v in data.dict().items() if v is not None}
        update_report = await department_collection.update_one(
            {"_id": PyObjectId(id_)},
            {"$set": changed_data}
        )
        if update_report.modified_count == 1:
            updated_department = await cls.get_one(id_)
            return updated_department
        else:
            return None

    @classmethod
    async def delete(cls, id_):
        delete_report = await department_collection.delete_one({"_id": PyObjectId(id_)})
        if delete_report.deleted_count == 1:
            return True
        return False
