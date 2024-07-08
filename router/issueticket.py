from datetime import datetime
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.response.issueTicket import IssueTicketResponse
from schemas.request.issueTicket import IssueTicketRequest
from sqlalchemy.orm import Session
from repository.issueticket import IssueTickets

router=APIRouter(
    prefix='/api/parking_lot',
    tags=["parking_lot"]
)

@router.post('/park',response_model=IssueTicketResponse)
def IssueTicket(issueTicketData:IssueTicketRequest,db: Session = Depends(get_db)):
    return IssueTickets(issueTicketData, db)