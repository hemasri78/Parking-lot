from sqlalchemy.orm import Session
from common.models.parkingLot import ParkingLot
from common.models.parkingSlot import ParkingSlot

class ParkingLotRepository:
    @staticmethod
    def get_by_name(db: Session, parking_lot_name: str):
        return db.query(ParkingLot).filter(ParkingLot.parking_lot_name == parking_lot_name).first()
    
    @staticmethod
    def get_by_id(db: Session, parking_lot_id: int):
        return db.query(ParkingLot).filter(ParkingLot.parking_lot_id == parking_lot_id).first()

    @staticmethod
    def add_parking_lot(db: Session, parking_lot: ParkingLot):
        db.add(parking_lot)
        db.commit()
        db.refresh(parking_lot)
        return parking_lot

    @staticmethod
    def add_parking_slot(db: Session, parking_slot: ParkingSlot):
        db.add(parking_slot)
        db.commit()