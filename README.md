### 🧱 Tech Stack

## Backend
- FastAPI
- Python
- Pandas
- OpenPyXL

## Financial Research Portal
- The Financial Research Portal is a web-based tool that extracts structured financial data from uploaded PDF financial statements and converts them into analyst-ready Excel sheets.
- The application focuses on reliability and usability, allowing evaluators to upload a document and immediately generate a formatted Excel output.

## 🌐 Public Deployment

The application is deployed using Render (Free Tier):
https://research-portal-symr.onrender.com

## 🧪 How to Run Locally

1️⃣ Install Requirements
pip install -r backend/requirements.txt

2️⃣ Install Tesseract OCR

Download:
https://github.com/UB-Mannheim/tesseract/wiki
Add to PATH.

Verify:
tesseract --version

3️⃣ Install Poppler

Download:
https://github.com/oschwartz10612/poppler-windows/releases
Add /bin folder to system PATH.

Verify:
pdftoppm -h

4️⃣ Run Backend
uvicorn backend.main:app --reload

Backend runs at:
http://localhost:8000

# OCR & PDF Processing (LOCAL)

- This project uses local OCR processing instead of external APIs.

🔎 Tesseract OCR

- Used for extracting text from scanned financial documents.

📄 Poppler

- Used via pdf2image to convert PDF pages into images before OCR.

## 📁 Project Structure

research-portal/
│
├── backend/
│   ├── main.py
│   ├── extractor.py
│   └── static/
│   |    └── index.html
|   └── requirements.txt
│
├── uploads/
├── outputs/
├── render.yaml
└── README.md

## 🚧 Free Hosting Limitations

Since Render Free Tier is used:

- ⏳ First request may take ~30–50 seconds (cold start)
- 📄 Large PDFs may process slower
- 🧠 OCR runs locally on server instance

These limitations do not affect core functionality.
