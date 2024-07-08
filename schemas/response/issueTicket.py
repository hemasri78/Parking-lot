from datetime import datetime
from pydantic import BaseModel

class IssueTicketResponse(BaseModel):
    ticket_id: int
    slot_No: int
    vehicle_number: str
    in_time: datetime

    class Config:
        from_attributes = True