class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "intro": "Once upon a time, in a land far away, there was a small village surrounded by dense forests. The villagers were peaceful and lived in harmony with nature. One day, a mysterious figure appeared at the edge of the forest..."
            },
            "2": {
                "intro": "In a futuristic city where robots and humans coexisted, there was a young engineer named Alex. Alex was known for creating innovative gadgets that helped both robots and humans. One day, Alex received a strange message that would change everything..."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an interactive story based on the following introduction:

{t['intro']}

Continue the story and at two different points, prompt the user for an input to decide the direction of the story. Ensure that each section of the story is coherent, engaging, and logically follows from the previous sections. Each section after user input should be at least 100 words long. Submit your interactive story as a plain text string with user inputs clearly marked as [User Input: ...]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be interactive with at least two user inputs clearly marked as [User Input: ...].",
            "Each section after user input should be at least 100 words long.",
            "The story should be coherent, engaging, and logically follow from the previous sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
