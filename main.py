import uvicorn
import requests

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8083, reload=True)