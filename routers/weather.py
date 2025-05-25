import logging
from fastapi import APIRouter, Request, Response, HTTPException

# initialize router
router = APIRouter()

# API1: get
@router.get('/{city}')
async def get_weather(req:Request, city:str):
    print(city)
    try:
        return {
            "city": city,
            "temp": 42.5,
            "unitMeasure": "degC",
            # "reqObj":req
        } 
    except HTTPException as e:
        return Response(status_code=e.status_code, content=e.detail)