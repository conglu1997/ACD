class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "discovery": "a new element with unique properties that revolutionizes energy storage"
            },
            "2": {
                "discovery": "a groundbreaking method for faster-than-light space travel"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Your task is to describe the following fictional scientific discovery or invention: {t['discovery']}\n"
            "Ensure your description includes the following:\n"
            "1. The name of the discovery or invention.\n"
            "2. A detailed explanation of its properties or mechanism.\n"
            "3. The potential impact it could have on society or technology.\n"
            "4. Any challenges or limitations associated with it.\n"
            "Your response should be creative, scientifically plausible, and coherent. Provide your response in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
