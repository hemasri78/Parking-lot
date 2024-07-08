from pydantic import BaseModel
from schemas.request.vehicleTypeEnum import VehicleTypeEnum
from schemas.request.statusEnum import StatusEnum

class SlotOccupancy(BaseModel):
    slot_no: int
    vehicle_type: VehicleTypeEnum
    status: StatusEnum

    class Config:
        from_attributes = True
