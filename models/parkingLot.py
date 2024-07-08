from database import Base
from sqlalchemy import Column, DateTime, Enum,Integer,String,ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship


class ParkingLot(Base):
    __tablename__ = "parking_lots"

    parking_lot_id = Column(Integer, primary_key=True, index=True)
    parking_lot_name = Column(String(100), unique=True)
    two_wheeler_slots = Column(Integer)
    four_wheeler_slots = Column(Integer)

    slots = relationship("ParkingSlot", back_populates="parking_lot")
