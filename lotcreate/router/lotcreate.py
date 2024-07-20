from ..service.ParkingLotService import ParkingLotService
from ..schema.request.parkingLotCreate import ParkingLotCreate
from ..schema.response.ParkingLotResponse import ParkingLotResponse
from ..schema.response.ParkingLotOccupancyResponse import ParkingLotOccupancyResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import get_db

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.post("/initialize", response_model=ParkingLotResponse)
def createLot(parkingLotData: ParkingLotCreate,db: Session = Depends(get_db)):
    return ParkingLotService.initialize_parking_lot(parkingLotData, db)

@router.get("/details/{parking_lot_id}", response_model=ParkingLotOccupancyResponse)
def getParkingLotDetail(parking_lot_id: int,db: Session = Depends(get_db)):
    return ParkingLotService.get_parking_lot_details(parking_lot_id, db)