---
title: Research Analysis Flow
emoji: 🔬
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
---

# Research Analysis Flow

[![Live Demo](https://img.shields.io/badge/Live%20Demo-HuggingFace%20Spaces-blue)](https://huggingface.co/spaces/davidleocadio94DLAI/practical-multi-ai-agents-with-crewai_research-analysis-flow)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.100.1-orange)](https://crewai.com)

An advanced multi-agent AI system that conducts comprehensive research and produces structured, actionable reports with prioritized recommendations.

## Features

- **Structured Output** - Reports with executive summary, findings, and recommendations
- **Priority Ranking** - Recommendations sorted by priority (1-5)
- **Importance Levels** - Findings categorized as high/medium/low importance
- **Multi-Agent Analysis** - Research, analysis, and writing agents collaborate

## Tech Stack

![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991)
![CrewAI](https://img.shields.io/badge/CrewAI-Flows-FF6B6B)
![Pydantic](https://img.shields.io/badge/Pydantic-Structured%20Output-E92063)
![Gradio](https://img.shields.io/badge/Gradio-UI-F97316)

## Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/davidleocadio94/practical-multi-ai-agents-with-crewai_research-analysis-flow.git
cd practical-multi-ai-agents-with-crewai_research-analysis-flow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run Locally

```bash
python app.py
```

Open http://localhost:7860 in your browser.

## How It Works

1. **Research Analyst Agent** - Gathers comprehensive information, facts, and statistics
2. **Data Analyst Agent** - Identifies patterns, trends, and implications
3. **Report Writer Agent** - Compiles findings into a structured Pydantic model

### Output Structure

```
Research Report
├── Executive Summary
├── Key Findings
│   ├── Finding 1 (importance: high/medium/low)
│   ├── Finding 2
│   └── ...
├── Recommendations
│   ├── Priority 1: Action item
│   ├── Priority 2: Action item
│   └── ...
└── Conclusion
```

## Example Topics

- "AI trends in 2024"
- "The future of renewable energy"
- "Impact of remote work on productivity"
- "Emerging cybersecurity threats"

---

Built as part of the [Practical Multi AI Agents and Advanced Use Cases with CrewAI](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/) course on DeepLearning.AI
