# Author: Louie Zhu
# Date: 4/1/2025
# File: exceptions.py
# Description: Define a function that handles various types of database errors globally

from fastapi import Request
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError
) -> JSONResponse:
    error_map = {
        "IntegrityError": {
            "status": 400,
            "detail": "Data integrity error. Possible duplicate entry or foreign key violation"
        },
        "OperationalError": {
            "status": 400,
            "detail": "Data integrity error. Possible duplicate entry or foreign key violation."
        },
        "ProgrammingError": {
            "status": 500,
            "detail": "Database programming error. Possible invalid SQL query or schema issue."
        },
        "DataError": {
            "status": 400,
            "detail": "Invalid data input. Check data types and constraints."
        },
        "DatabaseError": {
            "status": 500,
            "detail": "A general database error occurred."
        },
        "DisconnectionError": {
            "status": 503,
            "detail": "The database connection was lost. Please try again."
        }
    }

    error_type = exc.__class__.__name__
    error = error_map.get(error_type, {"status": 500, "detail": "An unexpected database error occurred."})

    # return HTTPException(status_code=status_code, detail=message)
    return JSONResponse(
        status_code=error["status"],
        content={"detail": error["detail"]},
    )


