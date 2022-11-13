from pydantic import BaseModel


class DepartmentSchema(BaseModel):
    employer_id: str
    department: str
    status: str | None = "active"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "employer_id": "1222122",
                "department": "Management",
                "status": "active",
            }
        }


class DepartmentUpdateSchema(BaseModel):
    employer_id: str | None = None
    department: str | None = None
    status: str | None = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "employer_id": "1222122",
                "department": "Management",
                "status": "active",
            }
        }


