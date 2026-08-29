from typing import List, Dict, Any
from fastapi import APIRouter
from schemas.threat import ThreatResult

router = APIRouter()
threat_store: List[ThreatResult] = []

@router.get("/threats", response_model=List[ThreatResult])
async def get_threats():
    return threat_store

@router.get("/threats/stats", response_model=Dict[str, Any])
async def get_stats():
    total = len(threat_store)
    critical = sum(1 for t in threat_store if t.risk_level == "Critical")
    high = sum(1 for t in threat_store if t.risk_level == "High")
    medium = sum(1 for t in threat_store if t.risk_level == "Medium")
    low = sum(1 for t in threat_store if t.risk_level == "Low")
    return {
        "total": total,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low
    }