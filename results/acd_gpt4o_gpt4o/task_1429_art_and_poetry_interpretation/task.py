class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpretation", "art_description": "A painting depicting a serene forest with a small, clear stream flowing through it. The trees are tall and lush, and the sunlight filters through the leaves, casting dappled shadows on the ground."},
            "2": {"type": "generation", "theme": "solitude"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'interpretation':
            instructions = f"""Your task is to interpret the following piece of art and describe what you think it represents. Consider elements such as the mood, symbolism, and any emotions it evokes. Here is the description of the art piece:

{t['art_description']}

Provide your interpretation in a coherent and thoughtful manner."""
        else:
            instructions = f"""Your task is to generate a poem based on the given theme. Ensure that your poem is creative, expressive, and captures the essence of the theme. Here is the theme:

{t['theme']}

Provide your poem in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'interpretation':
            criteria = ["The interpretation should be coherent and thoughtful.", "The interpretation should consider elements such as mood, symbolism, and emotions."]
        else:
            criteria = ["The poem should be creative and expressive.", "The poem should capture the essence of the given theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
