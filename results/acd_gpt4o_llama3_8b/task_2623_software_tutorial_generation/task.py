class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Create a simple website using HTML and CSS.",
                "details": "The website should have a header, a navigation bar, a main content section, and a footer. The main content section should include a welcome message and a brief paragraph about the purpose of the website."
            },
            "2": {
                "task": "Set up a basic Python development environment.",
                "details": "The setup should include installing Python, setting up a virtual environment, and installing necessary packages such as 'requests' and 'flask'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed step-by-step tutorial for completing the following task using the specified software tools:

Task: {t['task']}

Details: {t['details']}

Your tutorial should be clear, logically sequenced, and cover all necessary steps from start to finish. Ensure that the tutorial can be followed by someone with basic knowledge of the tools involved. Each step should include a brief explanation of what is being done and why it is necessary. Submit your response as a plain text string in the following format:

1. Step 1: [First step]
2. Step 2: [Second step]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The tutorial should be clear and logically sequenced.", "The tutorial should cover all necessary steps from start to finish.", "Each step should include a brief explanation of what is being done and why it is necessary.", "The tutorial should be understandable by someone with basic knowledge of the tools involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
