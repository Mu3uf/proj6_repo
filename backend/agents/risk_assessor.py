from crewai import Agent

def get_risk_assessor_agent() -> Agent:
    return Agent(
        role="Risk Assessment Agent",
        goal="Evaluate threat risk levels and quantify blast radius based on anomaly scores.",
        backstory="Risk Management Expert focused on scoring vector severity and operational impact.",
        verbose=False,
        allow_delegation=False
    )