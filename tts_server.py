import edge_tts
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

VOICE = "hi-IN-MadhurNeural"

@app.get("/tts")
async def tts(text: str):

    async def audio_stream():
        communicate = edge_tts.Communicate(text, VOICE)
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]

    return StreamingResponse(
        audio_stream(),
        media_type="audio/mpeg"
    )
