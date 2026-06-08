from fastapi import FastAPI, UploadFile, File 
import pandas as pd
app = FastAPI()

current_dataset = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):
    global current_dataset
    df = pd.read_csv(file.file)
    current_dataset =df
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": {column: str(dtype) for column, dtype in df.dtypes.items()}
    }
    
    
@app.get("/data/stats")
def get_stats():
    if current_dataset is None:
        return {"error": "No dataset uploaded"}
    return current_dataset.describe().to_dict()