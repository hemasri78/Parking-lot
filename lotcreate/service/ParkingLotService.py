from fastapi import HTTPException
from sqlalchemy.orm import Session

from lotcreate.service import ParkingSlotService
from ..schema.request.parkingLotCreate import ParkingLotCreate
from ..schema.response.ParkingLotResponse import ParkingLotResponse
from common.models.parkingLot import ParkingLot
from ..schema.request.SlotOccupancy import SlotOccupancy
from ..schema.response.ParkingLotOccupancyResponse import ParkingLotOccupancyResponse
from ..repository.ParkingLotRepository import ParkingLotRepository


class ParkingLotService:
    @staticmethod
    def initialize_parking_lot(parking_lot_data: ParkingLotCreate, db: Session):
        existing_lot = ParkingLotRepository.get_by_name(db, parking_lot_data.parking_lot_name)
        if existing_lot:
            raise HTTPException(status_code=400, detail=f"{parking_lot_data.parking_lot_name} already exists")

        new_parking_lot = ParkingLot(
            parking_lot_name=parking_lot_data.parking_lot_name,
            two_wheeler_slots=parking_lot_data.two_wheeler_slots,
            four_wheeler_slots=parking_lot_data.four_wheeler_slots
        )
        new_parking_lot = ParkingLotRepository.add_parking_lot(db, new_parking_lot)

        ParkingSlotService.create_two_wheeler_slots(parking_lot_data.two_wheeler_slots, new_parking_lot.parking_lot_id, db)
        ParkingSlotService.create_four_wheeler_slots(parking_lot_data.four_wheeler_slots, parking_lot_data.two_wheeler_slots, new_parking_lot.parking_lot_id, db)

        return ParkingLotResponse(
            parking_lot_id=new_parking_lot.parking_lot_id, 
            message=f"Parking lot with ID {new_parking_lot.parking_lot_id} created successfully."
        )
    
    @staticmethod
    def get_parking_lot_details(parking_lot_id: int, db: Session):
        parking_lot = ParkingLotRepository.get_by_id(db, parking_lot_id)
        if parking_lot is None:
            raise HTTPException(status_code=404, detail="Parking lot not found")

        occupancy_details = [
            SlotOccupancy(slot_no=slot.slot_no, vehicle_type=slot.vehicle_type, status=slot.status)
            for slot in parking_lot.slots
        ]

        return ParkingLotOccupancyResponse(parking_lot_id=parking_lot_id, occupancy_details=occupancy_details)


