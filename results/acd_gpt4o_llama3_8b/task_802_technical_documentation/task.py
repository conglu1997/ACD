class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specifications": "Product: Smart Home Thermostat\nFeatures: WiFi connectivity, voice control, energy usage reports, remote access via mobile app\nInstallation: Compatible with most HVAC systems, DIY installation with step-by-step video guide\nTroubleshooting: Common issues include WiFi connectivity problems, inaccurate temperature readings, and unresponsive touch screen."
            },
            "2": {
                "specifications": "Software: Project Management Tool\nFeatures: Task assignment, time tracking, Gantt charts, team collaboration tools, integration with other software (e.g., Slack, Google Calendar)\nUser Guide: Initial setup instructions, creating and assigning tasks, using Gantt charts, tracking time, integrating with other tools\nTroubleshooting: Issues with task notifications, syncing problems with integrations, data export errors."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following technical specifications, generate a user manual or troubleshooting guide. Ensure that your documentation is clear, comprehensive, and easy to follow.

Technical Specifications:
{t['specifications']}

Your documentation should include the following sections:
1. Introduction
2. Features Overview
3. Installation/User Guide
4. Troubleshooting

Submit your documentation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The documentation should include an introduction.", "The documentation should provide a clear overview of the features.", "The documentation should include a comprehensive installation or user guide.", "The documentation should have a troubleshooting section.", "The response should be clear, comprehensive, and easy to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
