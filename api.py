from joblib import load
import os
import s3fs
from fastapi import FastAPI

# import model

S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})
FILE_PATH_S3 = "projet-funathon/2026/project1/models/rf_model_final.joblib" 

with fs.open(FILE_PATH_S3, mode="rb") as model:
    rf_model_final = load(model)

FILE_PATH_S3 = "projet-funathon/2026/project1/models/gb_model_final.joblib" 

with fs.open(FILE_PATH_S3, mode="rb") as model:
    gb_model_final = load(model)

# API

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Housing price prediction API is running"}