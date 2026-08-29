from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class LogEvent(BaseModel):
    timestamp: Optional[str] = Field(default_factory=lambda: datetime.utcnow().isoformat())
    source_ip: str
    destination_ip: str
    event_type: str
    action: str
    port: int
    status: str
    failed_logins: int
    request_frequency: float
    unique_ports: int

class ThreatResult(BaseModel):
    id: str
    timestamp: str
    source_ip: str
    destination_ip: str
    classification: str
    anomaly_score: float
    risk_level: str
    reason: str
    report: Optional[str] = None