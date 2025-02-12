class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "application": "A mobile app for tracking daily water intake.",
                "requirements": "The UI should include features for logging water intake, viewing daily/weekly statistics, and setting reminders."
            },
            "2": {
                "application": "A desktop app for managing personal finances.",
                "requirements": "The UI should include features for tracking income and expenses, generating financial reports, and visualizing spending habits."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to design a user interface for the specified application. Ensure that the UI is user-friendly, aesthetically pleasing, and functional. "
            "Provide a detailed description of the UI, including the layout, color scheme, and key features. "
            "Your response should be structured as follows: \n\n"
            "1. Application description \n"
            "2. UI layout and design \n"
            "3. Color scheme and visual elements \n"
            "4. Key features and functionalities \n"
            "5. Justification for design choices"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed description of the UI layout and design.",
            "The response should describe an appropriate color scheme and visual elements.",
            "The key features and functionalities should meet the specified requirements.",
            "The justification for design choices should be logical and demonstrate an understanding of user experience principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
