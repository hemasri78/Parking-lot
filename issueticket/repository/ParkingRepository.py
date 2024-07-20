from sqlalchemy.orm import Session
from common.models.parkingSlot import ParkingSlot

class ParkingRepository:
    @staticmethod
    def get_available_slot(db: Session, parking_lot_id: int, vehicle_type: str):
        return db.query(ParkingSlot).filter(
            ParkingSlot.parking_lot_id == parking_lot_id,
            ParkingSlot.vehicle_type == vehicle_type,
            ParkingSlot.status == 'free'
        ).first()

    @staticmethod
    def update_slot_status(db: Session, slot: ParkingSlot, status: str):
        slot.status = status
        db.commit()
        db.refresh(slot)
        return slot