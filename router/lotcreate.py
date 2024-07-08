from repository import lotcreate
from schemas.request.parkingLotCreate import ParkingLotCreate
from schemas.response.parkingLotCreate import ParkingLotResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import get_db

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.post("initialize", response_model=ParkingLotResponse)
def createLot(parkingLotData: ParkingLotCreate,db: Session = Depends(get_db)):
    return lotcreate.initialize_parking_lot(parkingLotData, db)