from crewai import Agent

def get_reporter_agent() -> Agent:
    return Agent(
        role="Security Reporter Agent",
        goal="Synthesize threat analysis and risk assessment into structured incident reports.",
        backstory="Incident Response Lead skilled in writing human-readable security briefings.",
        verbose=False,
        allow_delegation=False
    )