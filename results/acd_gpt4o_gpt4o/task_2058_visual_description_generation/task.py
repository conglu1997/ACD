class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Time as a physical space"},
            "2": {"concept": "A city where emotions are buildings"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed visual description based on the following abstract concept:

Concept: {t["concept"]}

The description should be vivid, imaginative, and coherent. It should create a clear mental image of the concept, incorporating sensory details and spatial relationships. Ensure that the description is well-structured and logically coherent. Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid.", "The description should be imaginative.", "The description should be coherent.", "The description should create a clear mental image of the concept.", "The description should incorporate sensory details and spatial relationships.", "The description should be well-structured and logically coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
