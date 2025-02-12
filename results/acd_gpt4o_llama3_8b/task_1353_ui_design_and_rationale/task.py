class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"application": "A mobile app for tracking personal fitness goals.", "requirements": "The UI should include a dashboard, goal-setting features, and progress tracking. The design should be user-friendly and visually appealing."},
            "2": {"application": "A desktop software for managing project tasks.", "requirements": "The UI should include a task list, calendar view, and collaboration features. The design should be intuitive and support productivity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        application = t["application"]
        requirements = t["requirements"]
        return f"""Design a user interface (UI) for the specified application based on the given requirements:

Application: {application}
Requirements: {requirements}

Provide your design solution with the following elements:
1. A comprehensive and detailed description of the UI design, including the layout, colors, typography, and key features.
2. The rationale for your design choices, explaining how they meet the requirements and enhance user experience.
3. Any additional considerations for usability and accessibility, including how the design accommodates diverse user needs.

Submit your solution as a plain text string in the following format:

Description: [Comprehensive and detailed description of the UI design]
Rationale: [Rationale for design choices]
Additional Considerations: [Usability and accessibility considerations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be comprehensive and detailed, covering layout, colors, typography, and key features.",
            "The rationale should be logical and explain how the design meets the requirements.",
            "The additional considerations should address usability and accessibility for diverse users."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
