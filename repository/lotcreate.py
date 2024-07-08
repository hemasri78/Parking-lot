from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.request.parkingLotCreate import ParkingLotCreate
from schemas.response.parkingLotCreate import ParkingLotResponse
from models.parkingLot import ParkingLot
from models.parkingSlot import ParkingSlot



def initialize_parking_lot(parking_lot_data: ParkingLotCreate,db: Session):
    existing_lot = db.query(ParkingLot).filter(ParkingLot.parking_lot_name == parking_lot_data.parking_lot_name).first()
    if existing_lot:
        raise HTTPException(status_code=400, detail=f"{parking_lot_data.parking_lot_name} already exists")
    new_parking_lot = ParkingLot(
        parking_lot_name=parking_lot_data.parking_lot_name,
        two_wheeler_slots=parking_lot_data.two_wheeler_slots,
        four_wheeler_slots=parking_lot_data.four_wheeler_slots
    )
    db.add(new_parking_lot)
    db.commit()
    db.refresh(new_parking_lot)

    for i in range(parking_lot_data.two_wheeler_slots):
        new_slot = ParkingSlot(
            slot_no=i + 1,
            parking_lot_id=new_parking_lot.parking_lot_id,
            vehicle_type='two_wheeler',
            status='free'
        )
        db.add(new_slot)

    for i in range(parking_lot_data.four_wheeler_slots):
        new_slot = ParkingSlot(
            slot_no=parking_lot_data.two_wheeler_slots + i + 1,
            parking_lot_id=new_parking_lot.parking_lot_id,
            vehicle_type='four_wheeler',
            status='free'
        )
        db.add(new_slot)

    db.commit()

    return ParkingLotResponse(parking_lot_id=new_parking_lot.parking_lot_id, message=f"parking lot with {new_parking_lot.parking_lot_id} created successfully.")