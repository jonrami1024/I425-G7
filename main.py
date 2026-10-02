import os

from sqlalchemy.exc import SQLAlchemyError

from starlette.staticfiles import StaticFiles
from fastapi import FastAPI

from api.exceptions import sqlalchemy_exception_handler
from api.driver.routes import router as driver_router

from api.driverSize.routes import router as driverSize_router

app = FastAPI(
    title="Mario Kart 8 API",
    description="API for Mario Kart 8 kart build stats",
    version="1.0.0",
    contact={"url": "https://github.com/jonrami1024/I425-G7"}
)

static_path = os.path.join(os.path.dirname(__file__), "api/static")
app.mount("/static", StaticFiles(directory=static_path))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.include_router(driver_router)
app.include_router(driverSize_router)
