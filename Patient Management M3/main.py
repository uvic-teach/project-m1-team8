from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sql_app import models
from db import get_db, engine
import sql_app.models as models
import sql_app.schemas as schemas
from sql_app.repositories import UserHealthInfoRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

models.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.post('/userhealthinfo', tags=["UserHealthInfo"],response_model=schemas.Item,status_code=201)
async def create_userhealthinfo(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """
    
    db_item = UserHealthInfoRepo.fetch_by_name(db, name=item_request.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await UserHealthInfoRepo.create(db=db, item=item_request)

@app.get('/userhealthinfo', tags=["UserHealthInfo"],response_model=List[schemas.Item])
def get_all_userhealthinfo(name: Optional[str] = None,db: Session = Depends(get_db)):

    if name:
        items =[]
        db_item = UserHealthInfoRepo.fetch_patient_name(db,name)
        items.append(db_item)
        return items
    else:
        return UserHealthInfoRepo.fetch_all_patient_info(db)


@app.get('/userhealthinfo/{patient_id}', tags=["UserHealthInfo"],response_model=schemas.Item)
def get_userhealthinfo(patient_id: int,db: Session = Depends(get_db)):
    """
    Get the Item with the given ID provided by User stored in database
    """
    db_item = UserHealthInfoRepo.fetch_patient_id(db,patient_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    return db_item

@app.delete('/userhealthinfo/{patient_id}', tags=["UserHealthInfo"])
async def delete_patientinfo(item_id: int,db: Session = Depends(get_db)):
    """
    Delete the Item with the given ID provided by User stored in database
    """
    db_item = UserHealthInfoRepo.fetch_patient_id(db,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    await UserHealthInfoRepo.delete(db,item_id)
    return "Item deleted successfully!"

@app.put('/items/{item_id}', tags=["UserHealthInfo"],response_model=schemas.Item)
async def update_item(item_id: int,item_request: schemas.Item, db: Session = Depends(get_db)):
    """
    Update an Item stored in the database
    """
    db_item = UserHealthInfoRepo.fetch_by_id(db, item_id)
    if db_item:
        update_item_encoded = jsonable_encoder(item_request)
        db_item.name = update_item_encoded['name']
        db_item.price = update_item_encoded['price']
        db_item.description = update_item_encoded['description']
        db_item.store_id = update_item_encoded['store_id']
        return await UserHealthInfoRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")