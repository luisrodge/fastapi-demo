import database as _database
import models as _models
import schemas as _schemas
import sqlalchemy.orm as _orm


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_district_by_name(db: _orm.Session, name: str):
    return db.query(_models.District).filter(_models.District.name == name).first()


def create_district(db: _orm.Session, district: _schemas.DistrictCreate):
    db_district = _models.District(name=district.name)
    db.add(db_district)
    db.commit()
    db.refresh(db_district)
    return db_district


def update_district(db: _orm.Session, id: int, district: _schemas.DistrictCreate):
    db_district = get_district(db=db, id=id)
    db_district.name = district.name
    db.commit()
    db.refresh(db_district)
    return db_district


def get_districts(db: _orm.Session, skip: int, limit: int):
    return db.query(_models.District).offset(skip).limit(limit).all()


def get_district(db: _orm.Session, id: int):
    return db.query(_models.District).filter(_models.District.id == id).first()


def delete_district(db: _orm.Session, id: int):
    db.query(_models.District).filter(_models.District.id == id).delete()
    db.commit()


def create_city(db: _orm.Session, city: _schemas.CityCreate, district_id: int):
    city = _models.City(**city.dict(), district_id=district_id)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city


def update_city(db: _orm.Session, id: int, city: _schemas.CityCreate):
    db_city = get_city(db=db, id=id)
    db_city.name = city.name
    db.commit()
    db.refresh(db_city)
    return db_city


def get_cities(db: _orm.Session, skip: int, limit: int):
    return db.query(_models.City).offset(skip).limit(limit).all()


def get_city(db: _orm.Session, id: int):
    return db.query(_models.City).filter(_models.City.id == id).first()


def delete_city(db: _orm.Session, id: int):
    db.query(_models.City).filter(_models.City.id == id).delete()
    db.commit()
