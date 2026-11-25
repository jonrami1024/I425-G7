# Jonathan Ramirez-Molina
# Date: 10/30/2026
# File: sorting.py
# Description:
from typing import Type
from sqlalchemy import Select, asc, desc
from sqlmodel import SQLModel

def apply_sorting(stmt: Select, sort: str, resc: Type[SQLModel]) -> Select:
    sort_fields = sort.split(',')
    for field in sort_fields:
        direction = asc
        if field.startswith('-'):
            direction = desc
            field = field[1:]

        if hasattr(resc, field):
            stmt = stmt.order_by(direction(getattr(resc, field)))
    return stmt