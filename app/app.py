from fastapi.security import HTTPBasic
from fastapi import FastAPI
from starlette.config import Config
from app.routes.login_logout_routes import loginlogoutrouter
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
app=FastAPI()
limiter = Limiter(
    key_func=get_remote_address
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
origins = ["*"]
security=HTTPBasic()
config = Config('.env')
app.include_router(loginlogoutrouter, tags=["loginlogoutrouter"])

app.add_middleware(CORSMiddleware,
    #allow_origins=origins,
    allow_origin_regex='https?://.*',
    allow_credentials=False,
    allow_methods='GET,HEAD,OPTIONS,POST',
    allow_headers=["*"]
)
