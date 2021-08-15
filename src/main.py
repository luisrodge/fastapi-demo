import fastapi as _fastapi
import services as _services
import schemas as _schemas
import sqlalchemy.orm as _orm
from typing import List

app = _fastapi.FastAPI()

_services.create_database()


@app.post("/districts", response_model=_schemas.District)
def create_district(district: _schemas.DistrictCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_district = _services.get_district_by_name(db=db, name=district.name)
    if db_district:
        raise _fastapi.HTTPException(
            status_code=400, detail="district already exists")
    return _services.create_district(db=db, district=district)


@app.put("/districts/{id}", response_model=_schemas.District)
def update_district(
    id: int,
    district: _schemas.DistrictCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_district(db=db, district=district, id=id)


@app.get("/districts", response_model=List[_schemas.District])
def get_districts(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.get_districts(db=db, skip=skip, limit=limit)


@app.get("/districts/{id}", response_model=_schemas.District)
def get_district(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_district = _services.get_district(db=db, id=id)
    if db_district is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="district not found")
    return db_district


@app.delete("/districts/{id}")
def delete_district(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_district(db=db, id=id)
    return {"message": f"successfully deleted district with id: {id}"}


@app.post("/districts/{id}/cities", response_model=_schemas.City)
def create_city(id: int, city: _schemas.CityCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_district = _services.get_district(db=db, id=id)
    if db_district is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="district not found")
    return _services.create_city(db=db, city=city, district_id=id)


@app.put("/cities/{id}", response_model=_schemas.City)
def update_city(
    id: int,
    city: _schemas.CityCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_city(db=db, city=city, id=id)


@app.get("/cities", response_model=List[_schemas.City])
def get_cities(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.get_cities(db=db, skip=skip, limit=limit)


@app.get("/cities/{id}", response_model=_schemas.City)
def get_city(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_city = _services.get_city(db=db, id=id)
    if db_city is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="city not found")
    return db_city


@app.delete("/cities/{id}")
def delete_city(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_city(db=db, id=id)
    return {"message": f"successfully deleted city with id: {id}"}
