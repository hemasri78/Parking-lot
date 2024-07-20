from pydantic import BaseModel
from common.schema.request.vehicleTypeEnum import VehicleTypeEnum
from common.schema.request.statusEnum import StatusEnum

class SlotOccupancy(BaseModel):
    slot_no: int
    vehicle_type: VehicleTypeEnum
    status: StatusEnum

    class Config:
        from_attributes = True
