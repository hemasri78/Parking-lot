from datetime import datetime
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from issueticket.schema.response.IssueTicketResponse import IssueTicketResponse
from ..schema.request.IssueTicketRequest import IssueTicketRequest
from sqlalchemy.orm import Session
from ..service.ParkingTicketService import ParkingTicketService
from ..service.UnparkingTicketService import UnparkingTicketService
from ..schema.request.UnparkingRequest import UnparkingRequest
from ..schema.response.ReturnTicketResponse import ReturnTicketResponse

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.post('/park',response_model=IssueTicketResponse)
def IssueTicket(issueTicketData:IssueTicketRequest,db: Session = Depends(get_db)):
    return ParkingTicketService.issue_ticket(issueTicketData, db)

@router.post("/unpark", response_model=ReturnTicketResponse)
def unparkVehicle(unparking_data: UnparkingRequest,db: Session = Depends(get_db)):
    return UnparkingTicketService.unpark_vehicle(unparking_data, db)