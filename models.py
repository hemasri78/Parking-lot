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

class ParkingTicket(Base):
    __tablename__ = "parking_tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey('parking_slots.slot_id'))
    vehicle_number = Column(String(20))
    in_time = Column(DateTime(timezone=True), default=func.now())
    out_time = Column(DateTime(timezone=True), nullable=True)
    

    