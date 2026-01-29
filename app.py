"""Gradio interface for the Research Analysis Flow."""

import gradio as gr
from src.crew import run_crew


def analyze_topic(topic: str):
    """Run research analysis on the given topic."""
    if not topic.strip():
        yield "Please enter a topic to research."
        return

    try:
        # Show processing status
        yield """## Processing...

The multi-agent crew is analyzing your topic. This typically takes 1-3 minutes.

**Current Status:**
1. Research Analyst - Gathering comprehensive information...
2. Data Analyst - (waiting)
3. Report Writer - (waiting)

Please wait..."""

        # Run the crew (this is where the actual work happens)
        result = run_crew(topic)

        # Return the final result
        yield result
    except Exception as e:
        yield f"Error during analysis: {str(e)}"


# Create Gradio interface
with gr.Blocks(title="Research Analysis Flow", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Research Analysis Flow

        An advanced multi-agent system that conducts research and produces structured reports.

        **How it works:**
        1. **Research Analyst** - Gathers comprehensive information on your topic
        2. **Data Analyst** - Analyzes findings and identifies key insights
        3. **Report Writer** - Compiles everything into a structured report

        The output includes:
        - Executive Summary
        - Key Findings (with importance levels)
        - Prioritized Recommendations
        - Conclusion

        *Note: Analysis takes 1-3 minutes as multiple AI agents work together.*
        """
    )

    with gr.Row():
        topic_input = gr.Textbox(
            label="Research Topic",
            placeholder="e.g., AI trends in 2024, Electric vehicle market, Remote work productivity",
            scale=4
        )
        submit_btn = gr.Button("Analyze", variant="primary", scale=1)

    output = gr.Markdown(label="Research Report")

    gr.Examples(
        examples=[
            ["AI trends in 2024"],
            ["The future of renewable energy"],
            ["Impact of remote work on productivity"],
            ["Emerging cybersecurity threats"],
        ],
        inputs=topic_input,
    )

    submit_btn.click(
        fn=analyze_topic,
        inputs=topic_input,
        outputs=output,
    )

    topic_input.submit(
        fn=analyze_topic,
        inputs=topic_input,
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()
