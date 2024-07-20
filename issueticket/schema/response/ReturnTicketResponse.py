from pydantic import BaseModel
from datetime import datetime

class ReturnTicketResponse(BaseModel):
    ticket_id: int
    slot_id: int
    vehicle_number: str
    in_time: datetime
    out_time:datetime

    class Config:
        from_attributes = True