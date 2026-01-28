"""CrewAI Research Analysis Flow - Advanced Multi-Agent System with Flows"""

from crewai import Agent, Task, Crew, Flow
from crewai.flow.flow import listen, start
from pydantic import BaseModel, Field
from typing import List
import os


# Pydantic Models for Structured Output
class Finding(BaseModel):
    title: str = Field(..., description="Title of the finding")
    description: str = Field(..., description="Detailed description")
    importance: str = Field(..., description="high, medium, or low")


class Recommendation(BaseModel):
    action: str = Field(..., description="Recommended action")
    rationale: str = Field(..., description="Why this is recommended")
    priority: int = Field(..., ge=1, le=5, description="Priority 1-5")


class ResearchReport(BaseModel):
    executive_summary: str = Field(..., description="Brief summary")
    findings: List[Finding] = Field(..., description="Key findings")
    recommendations: List[Recommendation] = Field(..., description="Action items")
    conclusion: str = Field(..., description="Final thoughts")


def create_agents():
    """Create the research analysis agents."""

    research_agent = Agent(
        role="Research Analyst",
        goal="Gather comprehensive information on {topic}",
        backstory="Expert researcher with deep analytical skills and attention to detail",
        verbose=True
    )

    analysis_agent = Agent(
        role="Data Analyst",
        goal="Analyze research findings and extract key insights",
        backstory="Experienced analyst skilled at identifying patterns and drawing conclusions",
        verbose=True
    )

    report_agent = Agent(
        role="Report Writer",
        goal="Compile findings into a structured, professional report",
        backstory="Technical writer who creates clear, actionable reports",
        verbose=True
    )

    return research_agent, analysis_agent, report_agent


def create_tasks(research_agent, analysis_agent, report_agent):
    """Create the research analysis tasks."""

    research_task = Task(
        description="Research {topic} thoroughly. Gather key facts, statistics, and recent developments.",
        expected_output="Comprehensive research notes with sources and key findings",
        agent=research_agent
    )

    analysis_task = Task(
        description="Analyze the research findings. Identify trends, implications, and recommendations.",
        expected_output="Analysis with key insights and actionable recommendations",
        agent=analysis_agent
    )

    report_task = Task(
        description="Create a structured report combining research and analysis.",
        expected_output="Professional report with executive summary, findings, and recommendations",
        agent=report_agent,
        context=[research_task, analysis_task],
        output_pydantic=ResearchReport
    )

    return research_task, analysis_task, report_task


def create_crew():
    """Create and return the research analysis crew."""
    research_agent, analysis_agent, report_agent = create_agents()
    research_task, analysis_task, report_task = create_tasks(
        research_agent, analysis_agent, report_agent
    )

    crew = Crew(
        agents=[research_agent, analysis_agent, report_agent],
        tasks=[research_task, analysis_task, report_task],
        verbose=True
    )

    return crew


def run_crew(topic: str) -> str:
    """Run the crew with the given topic and return the result."""
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    crew = create_crew()
    result = crew.kickoff(inputs={"topic": topic})

    # Format the structured output nicely
    if result.pydantic:
        report = result.pydantic
        output = f"# Research Report: {topic}\n\n"
        output += f"## Executive Summary\n{report.executive_summary}\n\n"

        output += "## Key Findings\n"
        for finding in report.findings:
            output += f"### {finding.title} ({finding.importance} importance)\n"
            output += f"{finding.description}\n\n"

        output += "## Recommendations\n"
        for rec in report.recommendations:
            output += f"### Priority {rec.priority}: {rec.action}\n"
            output += f"{rec.rationale}\n\n"

        output += f"## Conclusion\n{report.conclusion}"
        return output

    return result.raw
