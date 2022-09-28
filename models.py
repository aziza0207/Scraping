from sqlalchemy import Column, Integer, String
from engine import Base


class Ads(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    price = Column(Integer)
    date = Column(String)