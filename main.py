from fastapi import FastAPI, UploadFile, File 
import pandas as pd
app = FastAPI()

current_dataset = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": {column: str(dtype) for column, dtype in df.dtypes.items()}
    }