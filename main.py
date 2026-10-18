import os

from sqlalchemy.exc import SQLAlchemyError

from starlette.staticfiles import StaticFiles
from fastapi import FastAPI

from api.exceptions import sqlalchemy_exception_handler

# from api
from api.driver.routes import router as driver_router
from api.driverSize.routes import router as driverSize_router
from api.body.routes import router as body_router
from api.bodyTypeGroup.routes import router as bodyType_router
from api.tire.routes import router as tire_router
from api.tireGroup.routes import router as tireGroup_router
from api.glider.routes import router as glider_router
from api.calculateStats.routes import router as calculate_stats_router
from api.users.routes import router as user_router
from api.builds.routes import router as builds_router
from api.build_ratings.routes import router as ratings_router

app = FastAPI(
    title="Mario Kart 8 API",
    description="API for Mario Kart 8 kart build stats. This project is an unofficial, open-source utility and is not affiliated with, authorized, maintained, or endorsed by Nintendo Co., Ltd. or any of its affiliates. All product names, logos, and brands are property of their respective owners.",
    version="1.0.0",
    contact={
        "name": "Github",
        "url": "https://github.com/jonrami1024/I425-G7"
    }
)

static_path = os.path.join(os.path.dirname(__file__), "api/static")
app.mount("/static", StaticFiles(directory=static_path))


app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)

# add app routers
app.include_router(driver_router)
app.include_router(driverSize_router)
app.include_router(body_router)
app.include_router(bodyType_router)
app.include_router(tire_router)
app.include_router(tireGroup_router)
app.include_router(glider_router)
app.include_router(calculate_stats_router)
app.include_router(user_router)
app.include_router(builds_router)
app.include_router(ratings_router)