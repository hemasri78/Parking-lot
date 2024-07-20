from pydantic import BaseModel
from typing import List
from ..request.SlotOccupancy import SlotOccupancy

class ParkingLotOccupancyResponse(BaseModel):
    parking_lot_id: int
    occupancy_details: List[SlotOccupancy]

    class Config:
        from_attributes = True
