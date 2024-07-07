from datetime import datetime
from pydantic import BaseModel
from typing import List,Optional

from enum import Enum

class ParkingLotCreate(BaseModel):
    parking_lot_name: str
    two_wheeler_slots: int
    four_wheeler_slots: int

    class Config:
        from_attributes = True

class ParkingLotResponse(BaseModel):
    parking_lot_id: int

    class Config:
        from_attributes = True

class VehicleTypeEnum(str, Enum):
    two_wheeler = "two_wheeler"
    four_wheeler = "four_wheeler"

class StatusEnum(str, Enum):
    occupied = "occupied"
    free = "free"

class SlotOccupancy(BaseModel):
    slot_no: int
    vehicle_type: VehicleTypeEnum
    status: StatusEnum

    class Config:
        from_attributes = True

class ParkingLotOccupancyResponse(BaseModel):
    parking_lot_id: int
    occupancy_details: List[SlotOccupancy]

    class Config:
        from_attributes = True

class IssueTicketRequest(BaseModel):
    parking_lot_id: int
    Vehicle_number: str
    Vehicle_type: VehicleTypeEnum

    class Config:
        from_attributes = True

class IssueTicketResponse(BaseModel):
    ticket_id: int
    slot_No: int
    vehicle_number: str
    in_time: datetime

    class Config:
        from_attributes = True

class UnparkingRequest(BaseModel):
    ticket_id: int

    class Config:
        from_attributes = True

class ReturnTicketResponse(BaseModel):
    ticket_id: int
    slot_id: int
    vehicle_number: str
    in_time: datetime
    out_time:datetime

    class Config:
        from_attributes = True
