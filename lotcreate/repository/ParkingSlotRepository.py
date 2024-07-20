from sqlalchemy.orm import Session
from common.models.parkingSlot import ParkingSlot

class ParkingSlotRepository:
    @staticmethod
    def create_two_wheeler_slots(db: Session, two_wheeler_slots: int, parking_lot_id: int):
        for i in range(two_wheeler_slots):
            new_slot = ParkingSlot(
                slot_no=i + 1,
                parking_lot_id=parking_lot_id,
                vehicle_type='two_wheeler',
                status='free'
            )
            db.add(new_slot)
        db.commit()

    @staticmethod
    def create_four_wheeler_slots(db: Session, four_wheeler_slots: int, two_wheeler_slots: int, parking_lot_id: int):
        for i in range(four_wheeler_slots):
            new_slot = ParkingSlot(
                slot_no=two_wheeler_slots + i + 1,
                parking_lot_id=parking_lot_id,
                vehicle_type='four_wheeler',
                status='free'
            )
            db.add(new_slot)
        db.commit()