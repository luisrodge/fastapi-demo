import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

from app.database import Base


class District(Base):
    __tablename__ = "districts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    cities = _orm.relationship("City", back_populates="district")


class City(Base):
    __tablename__ = "cities"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    district_id = _sql.Column(_sql.Integer, _sql.ForeignKey("districts.id"))
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    district = _orm.relationship("District", back_populates="cities")


# class User(_database, Base):
#     __tablename__ = "users"
#     id = _sql.Column(_sql.Integer, primary_key=True, index=True)
#     name = _sql.Column(_sql.String)
#     username = _sql.Column(_sql.String, unique=True, index=True)
