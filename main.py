from fastapi import FastAPI
import lotcreate,getall_slot,issueticket,unpark
import models
from database import engine

app=FastAPI()
models.Base.metadata.create_all(engine)


@app.get('/')
async def root():
    return {"helo world"}

app.include_router(lotcreate.router)
app.include_router(getall_slot.router)
app.include_router(issueticket.router)
app.include_router(unpark.router)