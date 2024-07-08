from pydantic import BaseModel
from schemas.request.vehicleTypeEnum import VehicleTypeEnum

from enum import Enum

class IssueTicketRequest(BaseModel):
    parking_lot_id: int
    Vehicle_number: str
    Vehicle_type: VehicleTypeEnum

    class Config:
        from_attributes = True