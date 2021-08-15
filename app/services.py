from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import District, City
from app.schemas import DistrictCreate, CityCreate


def create_database():
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_district_by_name(db: Session, name: str):
    return db.query(District).filter(District.name == name).first()


def create_district(db: Session, district: DistrictCreate):
    db_district = District(name=district.name)
    db.add(db_district)
    db.commit()
    db.refresh(db_district)
    return db_district


def update_district(db: Session, id: int, district: DistrictCreate):
    db_district = get_district(db=db, id=id)
    db_district.name = district.name
    db.commit()
    db.refresh(db_district)
    return db_district


def get_districts(db: Session, skip: int, limit: int):
    return db.query(District).offset(skip).limit(limit).all()


def get_district(db: Session, id: int):
    return db.query(District).filter(District.id == id).first()


def delete_district(db: Session, id: int):
    db.query(District).filter(District.id == id).delete()
    db.commit()


def create_city(db: Session, city: CityCreate, district_id: int):
    city = City(**city.dict(), district_id=district_id)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city


def update_city(db: Session, id: int, city: CityCreate):
    db_city = get_city(db=db, id=id)
    db_city.name = city.name
    db.commit()
    db.refresh(db_city)
    return db_city


def get_cities(db: Session, skip: int, limit: int):
    return db.query(City).offset(skip).limit(limit).all()


def get_city(db: Session, id: int):
    return db.query(City).filter(City.id == id).first()


def delete_city(db: Session, id: int):
    db.query(City).filter(City.id == id).delete()
    db.commit()
