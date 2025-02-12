class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "a blue circle with a radius of 50 pixels centered in a 200x200 pixels SVG canvas"},
            "2": {"description": "a red rectangle with a width of 100 pixels and height of 50 pixels positioned at (50, 50) in a 200x200 pixels SVG canvas"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Generate SVG code based on the following description: '{description}'. Ensure the SVG code is valid and matches the description accurately. Use appropriate SVG tags such as <svg>, <circle>, <rect>, etc. Submit your SVG code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from xml.etree import ElementTree as ET
        description = t["description"]
        try:
            # Check if the submission is valid SVG
            ET.fromstring(submission)
        except ET.ParseError:
            return 0.0
        # Use LLM judge to verify if the SVG code matches the description
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The SVG code should match the description: '{description}'",
            "The SVG code should be valid and contain appropriate SVG tags.",
            "The SVG code should specify correct attributes for the described shapes.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
