class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"senses": "The sound of waves crashing, the salty smell of the sea, and the feeling of sand between your toes."},
            "2": {"senses": "The aroma of freshly baked bread, the sight of golden crusts, and the warmth of the bakery."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a narrative or scenario that incorporates the following sensory descriptions: {t["senses"]}

Your narrative should be vivid and creative, making the reader feel as if they are experiencing the senses themselves. Ensure the narrative is at least 200 words long and has a clear structure with a beginning, middle, and end."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should accurately incorporate the given sensory descriptions.", "The narrative should be vivid, creative, and engaging.", "The narrative should be at least 200 words long.", "The narrative should have a clear structure with a beginning, middle, and end."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
