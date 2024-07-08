from database import Base
from sqlalchemy import Column, DateTime, Enum,Integer,String,ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship

class ParkingTicket(Base):
    __tablename__ = "parking_tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey('parking_slots.slot_id'))
    vehicle_number = Column(String(20))
    in_time = Column(DateTime(timezone=True), default=func.now())
    out_time = Column(DateTime(timezone=True), nullable=True)
    