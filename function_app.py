import azure.functions as func
from fastapi import FastAPI
import logging
from routers import weather

fs_app = FastAPI()
fs_app.include_router(weather.router, prefix="/weather")

# def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
#     return func.AsgiMiddleware(app).handle_async(req)

app = func.AsgiFunctionApp(app=fs_app, http_auth_level=func.AuthLevel.ANONYMOUS)