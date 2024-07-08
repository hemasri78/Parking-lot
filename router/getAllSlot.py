from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from repository.getallSlot import getParkingLotDetails
from sqlalchemy.orm import Session
from schemas.response.parkingSlot import ParkingLotOccupancyResponse

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.get("details/{parking_lot_id}", response_model=ParkingLotOccupancyResponse)
def getParkingLotDetail(parking_lot_id: int,db: Session = Depends(get_db)):
    return getParkingLotDetails(parking_lot_id, db)