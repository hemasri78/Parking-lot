from datetime import datetime
from fastapi import APIRouter, HTTPException,Depends
import schemas,models,database
from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)
get_db=database.get_db

@router.post('/park',response_model=schemas.IssueTicketResponse)
async def IssueTicket(issue_ticket_data:schemas.IssueTicketRequest,db: Session = Depends(get_db)):
    existing_ticket = db.query(models.ParkingTicket).filter(
        models.ParkingTicket.vehicle_number == issue_ticket_data.Vehicle_number,
        models.ParkingTicket.out_time == None ).first()
    
    if existing_ticket:
        raise HTTPException(status_code=400, detail="Vehicle is already parked.")
    
    available_slot = db.query(models.ParkingSlot).join(models.ParkingLot).filter(
        models.ParkingSlot.parking_lot_id == issue_ticket_data.parking_lot_id,
        models.ParkingSlot.vehicle_type == issue_ticket_data.Vehicle_type,
        models.ParkingSlot.status == 'free'
    ).first()
    
    if not available_slot:
        raise HTTPException(status_code=400, detail="No available slots for the requested vehicle type.")
    
    new_ticket = models.ParkingTicket(
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
