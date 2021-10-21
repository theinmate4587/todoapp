from fastapi import FastAPI,Depends,HTTPException,status,File, UploadFile,APIRouter, Body
from fastapi.security import HTTPBasic,HTTPBasicCredentials
from app.model.Responses import Responses
import sys,os
import requests
from datetime import timedelta
from typing import Dict
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from app.model.Settings import Settings
from app.database.crud import CrudFun
import hashlib
from fastapi.requests import Request
from ratelimit import limits

loginlogoutrouter = APIRouter()
responses = Responses()
crud=CrudFun()
settings=Settings()
class Settings(BaseModel):
    authjwt_secret_key: str = settings.secret_key

@AuthJWT.load_config
def get_config():
    return Settings()



@loginlogoutrouter.post('/todo/login_logout/registration')
@limits(calls=10, period=2000)
def registration(username:str=Body(...),password:str=Body(...)):
    updateTime=""
    createTime=""
    phone=0
    data = {'username':username,'password':password,'updateTime':updateTime,"createTime":createTime,"phone":phone}
    try:
        
        result=crud.insert_user_details( data)
    except:
        e = str(sys.exc_info()[1])
        data = {"msg": e}
        return responses.failure(data)
    data = {"result": result}
    if(result=="User Already Exists"):
        return responses.warning(data)
    return responses.success(data)

@loginlogoutrouter.post('/todo/login/login')
def login(username:str=Body(...),password:str=Body(...),Authorize: AuthJWT = Depends()):
    
    data={'username':username,'password':password}
    data=crud.login(data)
    if data=="incorrect":
        return responses.warning("Incorrect login creds")
    hashString =  data["username"]
    delta = timedelta(hours=8)
                
    token=Authorize.create_access_token(subject=username,expires_time=delta)
    data["token"]=token
    return responses.success(data)
    

@loginlogoutrouter.post('/todo/login_logout/edituserdetails')
def edit_user_details(json_body: Dict,Authorize: AuthJWT = Depends()):
    
 
        #current_user = get_jwt()
    Authorize.jwt_required()
    current_user = Authorize.get_raw_jwt()
    username=current_user["sub"]
    
    data=crud.edit_user(username,json_body)
    
    data = {"result": data}
    return responses.success(data)

@loginlogoutrouter.get('/todo/login/logout')
def logout(Authorize: AuthJWT = Depends()):

    responses = Responses()
    try:
        Authorize.jwt_required()
        current_user = Authorize.get_raw_jwt()
    except:
        e = str(sys.exc_info()[1])
        data = {"msg": e}
        return responses.failure(data)

    data = {"user": current_user}
    return responses.success(data)