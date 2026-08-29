class RiskService:
    @staticmethod
    def calculate_risk(anomaly_score: float, rule_triggered: bool) -> str:
        if rule_triggered or anomaly_score < -0.35:
            return "Critical"
        elif anomaly_score < -0.15:
            return "High"
        elif anomaly_score < 0.0:
            return "Medium"
        else:
            return "Low"