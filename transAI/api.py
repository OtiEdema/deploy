from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from backend import generate_transcription, save_as_pdf, save_as_word

import os

app = FastAPI()

class TranscriptionRequest(BaseModel):
    url: str
    format: str  # "PDF" or "Word"

def clean_up_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

@app.post("/transcribe")
async def transcribe(request: TranscriptionRequest, background_tasks: BackgroundTasks):
    url = request.url
    output_format = request.format

    if output_format not in ["PDF", "Word"]:
        raise HTTPException(status_code=400, detail="Invalid format. Choose 'PDF' or 'Word'.")

    transcription, summary, keywords = generate_transcription(url)
    
    if output_format == "PDF":
        file_path = "transcription.pdf"
        save_as_pdf(transcription, summary, keywords, filename=file_path)
        mime_type = "application/pdf"
    else:
        file_path = "transcription.docx"
        save_as_word(transcription, summary, keywords, filename=file_path)
        mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    background_tasks.add_task(clean_up_file, file_path)
    return {
        "file_path": file_path,
        "mime_type": mime_type
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
