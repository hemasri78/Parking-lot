from sqlalchemy.orm import Session
from ..repository.ParkingSlotRepository import ParkingSlotRepository


class ParkingSlotService:
    @staticmethod
    def create_two_wheeler_slots(two_wheeler_slots: int, parking_lot_id: int, db: Session):
        ParkingSlotRepository.create_two_wheeler_slots(db, two_wheeler_slots, parking_lot_id)

    @staticmethod
    def create_four_wheeler_slots(four_wheeler_slots: int, two_wheeler_slots: int, parking_lot_id: int, db: Session):
        ParkingSlotRepository.create_four_wheeler_slots(db, four_wheeler_slots, two_wheeler_slots, parking_lot_id)