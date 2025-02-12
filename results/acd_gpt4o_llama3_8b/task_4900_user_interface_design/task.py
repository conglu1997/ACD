class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "application": "Weather App",
                "requirements": "The UI should display the current weather, a 7-day forecast, and allow users to search for weather in different locations."
            },
            "2": {
                "application": "Task Management App",
                "requirements": "The UI should allow users to create, view, edit, and delete tasks. It should also provide a calendar view for task deadlines and a progress tracker."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a user interface for the following application based on the given requirements:

Application: {t['application']}
Requirements: {t['requirements']}

Ensure that the design is functional, aesthetically pleasing, and adheres to user experience principles. Provide a detailed description of the design, including layout, color scheme, and key UI elements. Submit your design as a plain text string in the following format:

Design Description: [Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design should be functional and meet the specified requirements.",
            "The design should be aesthetically pleasing.",
            "The design should adhere to user experience principles.",
            "The design should be user-friendly and accessible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
