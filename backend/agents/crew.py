from crewai import Crew, Process, Task
from agents.analyzer import get_analyzer_agent
from agents.risk_assessor import get_risk_assessor_agent
from agents.reporter import get_reporter_agent

class ThreatIntelligenceCrew:
    def __init__(self):
        self.analyzer = get_analyzer_agent()
        self.assessor = get_risk_assessor_agent()
        self.reporter = get_reporter_agent()

    def run(self, parsed_log: dict, anomaly_score: float, risk_level: str, baseline_reason: str) -> str:
        t1 = Task(
            description=f"Analyze log event: {parsed_log}. Rule Reason: {baseline_reason}",
            expected_output="Anomalous behavior analysis summary.",
            agent=self.analyzer
        )
        t2 = Task(
            description=f"Evaluate risk severity '{risk_level}' given anomaly score {anomaly_score}.",
            expected_output="Detailed risk vector assessment.",
            agent=self.assessor
        )
        t3 = Task(
            description="Synthesize findings into an executive incident response briefing.",
            expected_output="Formatted final threat report.",
            agent=self.reporter
        )

        crew = Crew(
            agents=[self.analyzer, self.assessor, self.reporter],
            tasks=[t1, t2, t3],
            process=Process.sequential,
            verbose=False
        )
        return str(crew.kickoff())