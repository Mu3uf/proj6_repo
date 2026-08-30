from fastapi import APIRouter
from schemas.threat import LogEvent, ThreatResult
from services.detection_service import DetectionService
from services.websocket_manager import ws_manager

router = APIRouter()
detection_service = DetectionService()

@router.post("/detect", response_model=ThreatResult)
async def detect_threat(log_event: LogEvent):
    result = detection_service.process_event(log_event)
    await ws_manager.broadcast(result.model_dump_json())
    return result