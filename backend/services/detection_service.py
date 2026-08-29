import os
import uuid
import joblib
import numpy as np

from schemas.threat import LogEvent, ThreatResult
from services.log_parser import LogParser
from services.feature_engineering import FeatureEngineer
from services.rule_detector import RuleDetector
from services.risk_service import RiskService
from agents.crew import ThreatIntelligenceCrew

class DetectionService:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "../models/isolation_forest.joblib")
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            self.model = None
        self.crew = ThreatIntelligenceCrew()

    def process_event(self, log_event: LogEvent) -> ThreatResult:
        parsed = LogParser.parse(log_event.model_dump())
        features = FeatureEngineer.transform(parsed)
        rule_triggered, rule_reason = RuleDetector.evaluate(parsed)

        if self.model:
            features_arr = np.array(features).reshape(1, -1)
            score = float(self.model.decision_function(features_arr)[0])
            pred = int(self.model.predict(features_arr)[0])
        else:
            score = -0.5 if rule_triggered else 0.5
            pred = -1 if rule_triggered else 1

        risk_level = RiskService.calculate_risk(score, rule_triggered)
        classification = "Suspicious Activity" if (pred == -1 or rule_triggered) else "Normal Activity"
        reason = rule_reason if rule_triggered else f"Isolation Forest score: {score:.2f}"

        report_summary = None
        if classification == "Suspicious Activity":
            report_summary = self.crew.run(parsed, score, risk_level, rule_reason)

        return ThreatResult(
            id=str(uuid.uuid4()),
            timestamp=parsed["timestamp"],
            source_ip=parsed["source_ip"],
            destination_ip=parsed["destination_ip"],
            classification=classification,
            anomaly_score=score,
            risk_level=risk_level,
            reason=reason,
            report=report_summary
        )