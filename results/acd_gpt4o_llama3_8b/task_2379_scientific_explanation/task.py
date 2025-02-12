class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Why does ice float on water?"
            },
            "2": {
                "phenomenon": "How do airplanes stay in the air?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific phenomenon in layman's terms. Your explanation should include real-world examples to help illustrate the concept.

{t['phenomenon']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear and understandable to someone without a scientific background.",
                    "The explanation should include a real-world example."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
