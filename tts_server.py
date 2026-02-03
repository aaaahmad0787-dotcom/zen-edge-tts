import edge_tts
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uuid

app = FastAPI()

VOICE = "hi-IN-MadhurNeural"

@app.get("/tts")
async def tts(text: str):
    filename = f"{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)
    return FileResponse(filename, media_type="audio/mpeg")
