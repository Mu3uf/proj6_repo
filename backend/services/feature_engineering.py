from typing import List, Dict, Any

class FeatureEngineer:
    @staticmethod
    def transform(parsed_log: Dict[str, Any]) -> List[float]:
        return [
            float(parsed_log["failed_logins"]),
            float(parsed_log["request_frequency"]),
            float(parsed_log["unique_ports"]),
        ]