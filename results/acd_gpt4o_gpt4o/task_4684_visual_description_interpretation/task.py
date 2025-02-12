class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpretation", "description": "A bustling city street during mid-day with people walking on sidewalks, cars honking, vendors selling food, a street musician playing guitar, and a child flying a kite in the park across the street."},
            "2": {"type": "interpretation", "description": "A quiet beach at sunset with waves gently crashing, seagulls flying, a couple walking hand-in-hand, a person collecting seashells near the water's edge, and a small bonfire with people sitting around it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to interpret the following detailed textual description of a visual scene and summarize the key elements of the scene:\n\n{description}\n\nProvide your summary in plain text format. Your summary should include all notable features and activities described in the text.\n\nExample Format:\n1. Key elements: [List of key elements]\n2. Summary: [Your summary]\n\nEnsure that your summary is coherent, detailed, and well-organized."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary accurately captures the essence of the described scene.", "The summary includes all notable features and activities described in the text.", "The summary is coherent, detailed, and well-organized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
