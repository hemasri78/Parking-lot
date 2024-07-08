from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from repository.unpark import unparkVehicles
from schemas.request.unparking import UnparkingRequest
from schemas.response.unparking import ReturnTicketResponse

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.post("/api/parking_lot/unpark", response_model=ReturnTicketResponse)
def unparkVehicle(unparking_data: UnparkingRequest,db: Session = Depends(get_db)):
    return unparkVehicles(unparking_data, db)