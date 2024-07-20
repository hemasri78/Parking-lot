from sqlalchemy.orm import Session
from common.models.parkingTicket import ParkingTicket
from common.models.parkingSlot import ParkingSlot

class UnparkingTicketRepository:
    @staticmethod
    def get_active_ticket_by_id(db: Session, ticket_id: int):
        return db.query(ParkingTicket).filter(
            ParkingTicket.ticket_id == ticket_id,
            ParkingTicket.out_time == None
        ).first()

    @staticmethod
    def update_ticket(db: Session, ticket: ParkingTicket):
        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def get_slot_by_id(db: Session, slot_id: int):
        return db.query(ParkingSlot).filter(ParkingSlot.slot_id == slot_id).first()

    