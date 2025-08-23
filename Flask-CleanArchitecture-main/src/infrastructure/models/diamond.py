from sqlalchemy import Column, Integer, String, Float
from infrastructure.databases.base import Base

class Diamond(Base):
    __tablename__ = "diamonds"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String(50))
    shape_cut = Column(String(50))
    carat = Column(Float)
    color = Column(String(20))
    clarity = Column(String(20))
    polish = Column(String(20))
    symmetry = Column(String(20))
    fluorescence = Column(String(20))
    estimated_price = Column(Float)
