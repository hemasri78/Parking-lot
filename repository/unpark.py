from datetime import datetime
from fastapi import HTTPException,status
import database
from sqlalchemy.orm import Session
from schemas.request.unparking import UnparkingRequest
from models.parkingTicket import ParkingTicket
from models.parkingSlot import ParkingSlot

get_db=database.get_db

def unparkVehicles(unparking_data: UnparkingRequest, db: Session):

    ticket_id = unparking_data.ticket_id

    parking_ticket = db.query(ParkingTicket).filter(
        ParkingTicket.ticket_id == ticket_id,
        ParkingTicket.out_time==None).first()
    
    if not parking_ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    
    if parking_ticket.out_time is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vehicle already unparked")
    
    parking_slot = db.query(ParkingSlot).filter(ParkingSlot.slot_id == parking_ticket.slot_id).first()
    if parking_slot:
        parking_slot.status = 'free'
    
    parking_ticket.out_time = datetime.utcnow()
    
    try:
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update parking slot status")
    
    response_data={
        "ticket_id": parking_ticket.ticket_id,
        "slot_id": parking_ticket.slot_id,
        "vehicle_number": parking_ticket.vehicle_number,
        "in_time": parking_ticket.in_time,
        "out_time": parking_ticket.out_time,
    }
    return response_data