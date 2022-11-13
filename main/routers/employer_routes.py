from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from typing import List, Dict
from ..schemas.SettingSchema import DepartmentSchema, DepartmentUpdateSchema
from ..db_models.SettingsModel import Department


router = APIRouter(
    prefix="/employer",
    tags=["employer"],
    dependencies=None,
    responses={404: {"description": "Not found"}},
)


@router.get("/departments")
async def department_list():
    departments = await Department.get_list()
    return {"results": departments}


@router.post("/departments")
async def department_create(department: DepartmentSchema):
    new_department = await Department.create(department)
    return {"status": "ok", "result": new_department}


@router.get("/departments/{dep_id}")
async def department_detail(dep_id: str):
    department = await Department.get_one(dep_id)
    if not department:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})

    return {"status": "ok", "result": department}


@router.put("/departments/{dep_id}")
async def department_update(dep_id: str, department: DepartmentUpdateSchema):
    updated_document = await Department.update(dep_id, department)
    if not updated_document:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
    return {"status": "ok", "result": updated_document}


@router.delete("/departments/{dep_id}")
async def department_delete(dep_id: str):
    delete_report = await Department.delete(dep_id)
    if not delete_report:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
    return {"status": "ok", "result": "Deleted successfully"}
