from fastapi import APIRouter, HTTPException,Depends
import schemas,models,database
from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)
get_db=database.get_db

@router.get("details/{parking_lot_id}", response_model=schemas.ParkingLotOccupancyResponse)
def get_parking_lot_details(parking_lot_id: int, db: Session = Depends(get_db)):
    parking_lot = db.query(models.ParkingLot).filter(models.ParkingLot.parking_lot_id == parking_lot_id).first()
    if parking_lot is None:
        raise HTTPException(status_code=404, detail="Parking lot not found")
    
    occupancy_details = []
    for slot in parking_lot.slots:
        occupancy_details.append(schemas.SlotOccupancy(slot_no=slot.slot_no, vehicle_type=slot.vehicle_type, status=slot.status))
    
    return schemas.ParkingLotOccupancyResponse(parking_lot_id=parking_lot_id, occupancy_details=occupancy_details)