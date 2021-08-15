from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import app.services as services
from app.schemas import District, DistrictCreate


router = APIRouter()


@router.post("", response_model=District)
def create_district(district: DistrictCreate, db: Session = Depends(services.get_db)):
    db_district = services.get_district_by_name(db=db, name=district.name)
    if db_district:
        raise HTTPException(status_code=400, detail="district already exists")
    return services.create_district(db=db, district=district)


@router.put("/{id}", response_model=District)
def update_district(
    id: int,
    district: DistrictCreate,
    db: Session = Depends(services.get_db),
):
    return services.update_district(db=db, district=district, id=id)


@router.get("", response_model=List[District])
def get_districts(
    skip: int = 0, limit: int = 10, db: Session = Depends(services.get_db)
):
    return services.get_districts(db=db, skip=skip, limit=limit)


@router.get("/{id}", response_model=District)
def get_district(id: int, db: Session = Depends(services.get_db)):
    db_district = services.get_district(db=db, id=id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="district not found")
    return db_district


@router.delete("/{id}")
def delete_district(id: int, db: Session = Depends(services.get_db)):
    services.delete_district(db=db, id=id)
    return {"message": f"successfully deleted district with id: {id}"}
