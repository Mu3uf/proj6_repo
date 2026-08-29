from typing import Any, Dict

class LogParser:
    @staticmethod
    def parse(data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "timestamp": str(data.get("timestamp", "")),
            "source_ip": str(data.get("source_ip", "0.0.0.0")),
            "destination_ip": str(data.get("destination_ip", "0.0.0.0")),
            "event_type": str(data.get("event_type", "UNKNOWN")),
            "action": str(data.get("action", "ALLOW")),
            "port": int(data.get("port", 80)),
            "status": str(data.get("status", "200")),
            "failed_logins": int(data.get("failed_logins", 0)),
            "request_frequency": float(data.get("request_frequency", 0.0)),
            "unique_ports": int(data.get("unique_ports", 1)),
        }