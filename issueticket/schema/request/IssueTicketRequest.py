from pydantic import BaseModel
from common.schema.request.vehicleTypeEnum import VehicleTypeEnum


class IssueTicketRequest(BaseModel):
    parking_lot_id: int
    Vehicle_number: str
    Vehicle_type: VehicleTypeEnum

    class Config:
        from_attributes = True