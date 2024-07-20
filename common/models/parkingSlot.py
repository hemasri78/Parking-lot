from database import Base
from sqlalchemy import Column,Enum,Integer,ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class ParkingSlot(Base):
    __tablename__ = "parking_slots"

    slot_id = Column(Integer, primary_key=True, index=True)
    slot_no = Column(Integer)
    parking_lot_id = Column(Integer, ForeignKey('parking_lots.parking_lot_id'))
    vehicle_type = Column(Enum('two_wheeler', 'four_wheeler', name='vehicle_type_enum'))
    status = Column(Enum('occupied', 'free', name='status_enum'))

    parking_lot = relationship("ParkingLot", back_populates="slots")

    __table_args__ = (
        UniqueConstraint('slot_no', 'parking_lot_id', name='unique_slot_per_lot'),
    )
