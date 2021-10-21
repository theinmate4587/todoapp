from fastapi import responses,HTTPException
from fastapi.responses import JSONResponse
class Responses:
    def success(self,data):
        return JSONResponse(content=data,status_code=200)

    def failure(self,data=""):
        return JSONResponse(content=data,status_code=500)
    def warning(self,data=""):
        return JSONResponse(content=data,status_code=201)