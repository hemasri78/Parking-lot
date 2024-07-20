from pydantic import BaseModel


class ParkingLotCreate(BaseModel):
    parking_lot_name: str
    two_wheeler_slots: int
    four_wheeler_slots: int

    class Config:
        from_attributes = True