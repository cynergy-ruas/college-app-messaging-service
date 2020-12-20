from fastapi import FastAPI
from fastapi import APIRouter
from app.api.dbroutes import some_router
from app.services.wsconfig import webapp
# from app.services.webrev import webrev
app = FastAPI()
app.include_router(some_router)
app.include_router(webapp)
# app.include_router(webapp)
