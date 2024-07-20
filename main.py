from fastapi import FastAPI
from lotcreate.router import lotcreate
from issueticket.router import issueticket
from common.models import parkingLot, parkingSlot, parkingTicket
from database import engine

app=FastAPI()
parkingLot.Base.metadata.create_all(engine)
parkingSlot.Base.metadata.create_all(engine)
parkingTicket.Base.metadata.create_all(engine)


@app.get('/')
async def root():
    return {"helo world"}

app.include_router(lotcreate.router)
app.include_router(issueticket.router)
