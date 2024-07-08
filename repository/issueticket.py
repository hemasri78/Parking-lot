from datetime import datetime
from fastapi import HTTPException,Depends
import database
from sqlalchemy.orm import Session
from schemas.request.issueTicket import IssueTicketRequest
from models.parkingTicket import ParkingTicket
from models.parkingSlot import ParkingSlot
from models.parkingLot import ParkingLot

get_db=database.get_db

def IssueTickets(issue_ticket_data:IssueTicketRequest,db: Session):
    existing_ticket = db.query(ParkingTicket).filter(
        ParkingTicket.vehicle_number == issue_ticket_data.Vehicle_number,
        ParkingTicket.out_time == None ).first()
    
    if existing_ticket:
        raise HTTPException(status_code=400, detail="Vehicle is already parked.")
    
    available_slot = db.query(ParkingSlot).join(ParkingLot).filter(
        ParkingSlot.parking_lot_id == issue_ticket_data.parking_lot_id,
        ParkingSlot.vehicle_type == issue_ticket_data.Vehicle_type,
        ParkingSlot.status == 'free'
    ).first()
    
    if not available_slot:
        raise HTTPException(status_code=400, detail="No available slots for the requested vehicle type.")
    
    new_ticket = ParkingTicket(
        slot_id=available_slot.slot_id,
        vehicle_number=issue_ticket_data.Vehicle_number,
        in_time=datetime.utcnow()  
    )
    db.add(new_ticket)
    
    available_slot.status = 'occupied'
    db.commit()
    
    response_data = {
        "ticket_id": new_ticket.ticket_id,
        "slot_No": available_slot.slot_no,
        "vehicle_number": new_ticket.vehicle_number,
        "in_time": new_ticket.in_time
    }
    return response_data
