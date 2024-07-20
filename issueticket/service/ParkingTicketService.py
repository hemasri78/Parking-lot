from datetime import datetime
from fastapi import HTTPException,Depends
import database
from sqlalchemy.orm import Session
from ..repository.ParkingTicketRepository import ParkingTicketRepository
from ..repository.ParkingRepository import ParkingRepository
from ..schema.request.IssueTicketRequest import IssueTicketRequest
from common.models.parkingTicket import ParkingTicket

get_db=database.get_db

class ParkingTicketService:
    @staticmethod
    def issue_ticket(issue_ticket_data: IssueTicketRequest, db: Session):
        existing_ticket = ParkingTicketRepository.get_active_ticket_by_vehicle_number(db, issue_ticket_data.Vehicle_number)
        
        if existing_ticket:
            raise HTTPException(status_code=400, detail="Vehicle is already parked.")
        
        available_slot = ParkingRepository.get_available_slot(
            db, issue_ticket_data.parking_lot_id, issue_ticket_data.Vehicle_type
        )
        
        if not available_slot:
            raise HTTPException(status_code=400, detail="No available slots for the requested vehicle type.")
        
        new_ticket = ParkingTicket(
            slot_id=available_slot.slot_id,
            vehicle_number=issue_ticket_data.Vehicle_number,
            in_time=datetime.utcnow()
        )
        new_ticket = ParkingTicketRepository.add_ticket(db, new_ticket)
        
        ParkingRepository.update_slot_status(db, available_slot, 'occupied')
        
        response_data = {
            "ticket_id": new_ticket.ticket_id,
            "slot_No": available_slot.slot_no,
            "vehicle_number": new_ticket.vehicle_number,
            "in_time": new_ticket.in_time
        }
        return response_data
