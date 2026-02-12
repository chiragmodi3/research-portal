from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pandas as pd
import uuid
import os

from .extractor import extract_financial_tables_fast, format_financial_excel

app = FastAPI()

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
async def serve_frontend():
    return FileResponse("backend/static/index.html")

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_id = str(uuid.uuid4())

    pdf_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    df, detected_years = extract_financial_tables_fast(pdf_path)

    output_path = os.path.join(OUTPUT_DIR, f"{file_id}.xlsx")

    df.to_excel(output_path, index=False)

    format_financial_excel(output_path, detected_years)

    return FileResponse(
        output_path,
        filename="financial_output.xlsx"
    )
