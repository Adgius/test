from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost",
    "http://localhost:8080"
]

origins_regex = r"127.0.0.1:.+"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_origin_regex=origins_regex,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
#                    "Authorization"],
# )

@app.get("/", response_class=HTMLResponse)
def map(request: Request):
  return templates.TemplateResponse("test2.html", {"request": request})

@app.get("/get_file")
def download_file():
  return FileResponse(path='custom.geojson')

@app.get("/get_file2")
def download_file():
  return FileResponse(path='all_countries.geojson')

@app.get("/get_file3")
def download_file():
  return FileResponse(path='russia_geojson_wgs84.geojson')

@app.on_event("shutdown")
def disconnect():
    #Disconnect from bd
    pass