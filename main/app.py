from fastapi import FastAPI
from .routers import employee_routes, employer_routes

app = FastAPI()

app.include_router(employee_routes.router)
app.include_router(employer_routes.router)
