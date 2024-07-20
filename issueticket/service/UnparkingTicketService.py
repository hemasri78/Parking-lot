from datetime import datetime
from fastapi import HTTPException
import database
from sqlalchemy.orm import Session
from ..schema.request.UnparkingRequest import UnparkingRequest
from ..repository.UnparkingTicketRepository import UnparkingTicketRepository
from ..repository.ParkingRepository import ParkingRepository


get_db=database.get_db


class UnparkingTicketService:
    @staticmethod
    def unpark_vehicle(unparking_data: UnparkingRequest, db: Session):
        ticket_id = unparking_data.ticket_id

        parking_ticket = UnparkingTicketRepository.get_active_ticket_by_id(db, ticket_id)
        
        if not parking_ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        
        if parking_ticket.out_time is not None:
            raise HTTPException(status_code=400, detail="Vehicle already unparked")
        
        parking_slot = UnparkingTicketRepository.get_slot_by_id(db, parking_ticket.slot_id)
        if parking_slot:
            ParkingRepository.update_slot_status(db, parking_slot, 'free')
        
        parking_ticket.out_time = datetime.utcnow()
        
        try:
            UnparkingTicketRepository.update_ticket(db, parking_ticket)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Failed to update parking slot status")
        
        response_data = {
            "ticket_id": parking_ticket.ticket_id,
            "slot_id": parking_ticket.slot_id,
            "vehicle_number": parking_ticket.vehicle_number,
            "in_time": parking_ticket.in_time,
            "out_time": parking_ticket.out_time,
        }
        return response_data