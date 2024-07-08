from pydantic import BaseModel

class UnparkingRequest(BaseModel):
    ticket_id: int

    class Config:
        from_attributes = True