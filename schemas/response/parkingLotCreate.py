from pydantic import BaseModel

class ParkingLotResponse(BaseModel):
    parking_lot_id: int

    class Config:
        from_attributes = True