from fastapi import APIRouter
from schemas.threat import LogEvent, ThreatResult
from services.detection_service import DetectionService

router = APIRouter()
detection_service = DetectionService()

@router.post("/detect", response_model=ThreatResult)
async def detect_threat(log_event: LogEvent):
    return detection_service.process_event(log_event)