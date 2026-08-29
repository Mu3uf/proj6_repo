from typing import Dict, Any, Tuple

class RuleDetector:
    @staticmethod
    def evaluate(parsed_log: Dict[str, Any]) -> Tuple[bool, str]:
        if parsed_log["failed_logins"] > 5:
            return True, "Baseline Rule Triggered: Exceeded maximum allowed failed logins."
        if parsed_log["request_frequency"] > 200.0:
            return True, "Baseline Rule Triggered: Abnormal request frequency spikes."
        return False, "Baseline Rule Passed: Normal activity."