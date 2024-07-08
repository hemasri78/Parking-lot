from fastapi import HTTPException,Depends
import database
from schemas.request.parkingSlot import SlotOccupancy
from schemas.response.parkingSlot import ParkingLotOccupancyResponse
from models.parkingLot import ParkingLot
from sqlalchemy.orm import Session

get_db=database.get_db

def getParkingLotDetails(parking_lot_id: int, db: Session = Depends(get_db)):
    parking_lot = db.query(ParkingLot).filter(ParkingLot.parking_lot_id == parking_lot_id).first()
    if parking_lot is None:
        raise HTTPException(status_code=404, detail="Parking lot not found")
    
    occupancy_details = []
    for slot in parking_lot.slots:
        occupancy_details.append(SlotOccupancy(slot_no=slot.slot_no, vehicle_type=slot.vehicle_type, status=slot.status))
    
    return ParkingLotOccupancyResponse(parking_lot_id=parking_lot_id, occupancy_details=occupancy_details)