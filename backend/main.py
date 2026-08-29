from dotenv import load_dotenv
load_dotenv()
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from routes.detection import router as detection_router, detection_service
from routes.threats import router as threats_router, threat_store
from services.websocket_manager import ws_manager
from schemas.threat import LogEvent

app = FastAPI(title="Threat Intelligence Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(detection_router, prefix="/api")
app.include_router(threats_router, prefix="/api")

@app.websocket("/ws/threats")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            log_data = json.loads(data)
            log_event = LogEvent(**log_data)
            result = detection_service.process_event(log_event)
            threat_store.append(result)
            await ws_manager.broadcast(result.model_dump_json())
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)