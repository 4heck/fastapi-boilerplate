import datetime

import pydantic


class BaseEntity(pydantic.BaseModel):
    id: int
    created_on: datetime.datetime
    updated_on: datetime.datetime

    class Config:
        orm_mode = True
