import pydantic as _pydantic
import datetime as _dt
from typing import List


class _CityBase(_pydantic.BaseModel):
    name: str


class CityCreate(_CityBase):
    pass


class City(_CityBase):
    id: int
    district_id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True


class _DistrictBase(_pydantic.BaseModel):
    name: str


class DistrictCreate(_DistrictBase):
    pass


class District(_DistrictBase):
    id: int
    cities: List[City] = []
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
