from sqlalchemy.orm import Session
from common.models.parkingTicket import ParkingTicket

class ParkingTicketRepository:
    @staticmethod
    def get_active_ticket_by_vehicle_number(db: Session, vehicle_number: str):
        return db.query(ParkingTicket).filter(
            ParkingTicket.vehicle_number == vehicle_number,
            ParkingTicket.out_time == None
        ).first()

    @staticmethod
    def add_ticket(db: Session, ticket: ParkingTicket):
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

