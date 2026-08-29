from crewai import Agent

def get_analyzer_agent() -> Agent:
    return Agent(
        role="Threat Analyzer Agent",
        goal="Analyze suspicious log entries, identify event anomalies, and extract patterns.",
        backstory="Security Analyst specializing in behavioral log parsing and baseline checking.",
        verbose=False,
        allow_delegation=False
    )