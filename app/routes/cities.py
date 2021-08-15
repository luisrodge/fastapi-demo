from fastapi import APIRouter
from fastapi import Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

import app.services as services
from app.schemas import City, CityCreate


router = APIRouter()


@router.post("/cities", response_model=City)
def create_city(
    id: int,
    city: CityCreate,
    db: Session = Depends(services.get_db),
):
    db_district = services.get_district(db=db, id=id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="district not found")
    return services.create_city(db=db, city=city, district_id=id)


@router.put("/{id}", response_model=City)
def update_city(
    id: int,
    city: CityCreate,
    db: Session = Depends(services.get_db),
):
    return services.update_city(db=db, city=city, id=id)


@router.get("", response_model=List[City])
def get_cities(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(services.get_db),
):
    return services.get_cities(db=db, skip=skip, limit=limit)


@router.get("/{id}", response_model=City)
def get_city(id: int, db: Session = Depends(services.get_db)):
    db_city = services.get_city(db=db, id=id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="city not found")
    return db_city


@router.delete("/{id}")
def delete_city(id: int, db: Session = Depends(services.get_db)):
    services.delete_city(db=db, id=id)
    return {"message": f"successfully deleted city with id: {id}"}
