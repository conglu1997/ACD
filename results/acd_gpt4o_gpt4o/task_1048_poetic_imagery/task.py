class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "prompt": "Describe the sunset as if it were a painting, focusing on the interplay of light and shadow."},
            "2": {"type": "interpret", "poem": "The moon whispers secrets to the night, while the stars dance in silent delight. The wind hums a lullaby, and the trees sway to the rhythm of the dark."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generate':
            return f"""Your task is to generate poetic imagery based on the following prompt:

{t['prompt']}

Ensure that your response is vivid, creative, and evocative. Use descriptive language to create a rich and immersive image. Provide your response in plain text format."""
        elif t['type'] == 'interpret':
            return f"""Your task is to interpret the poetic imagery in the following poem:

{t['poem']}

Provide a detailed analysis of the imagery and metaphors used in the poem. Explain what the imagery conveys and how it contributes to the overall meaning of the poem. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'generate':
            criteria.append("The response should be vivid, creative, and evocative.")
        elif t['type'] == 'interpret':
            criteria.append("The analysis should be detailed and insightful, accurately interpreting the poetic imagery and metaphors.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
