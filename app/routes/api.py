from fastapi import APIRouter

from app.routes import cities, districts


router = APIRouter()

router.include_router(districts.router, tags=[
                      "districts"], prefix="/districts")

router.include_router(cities.router, tags=[
                      "cities"], prefix="/cities")


# router.include_router(items.router, tags=[
#                       "items"], prefix="/items")
