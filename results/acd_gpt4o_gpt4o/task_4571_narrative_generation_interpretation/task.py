class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'theme': 'A journey to an unknown land',
                'requirements': 'The story should include at least one main character, a conflict, and a resolution. The setting should be vividly described, and the narrative should be engaging and coherent. The story should be at least 300 words long.'
            },
            '2': {
                'story': 'Once upon a time, in a land far away, there was a small village surrounded by enchanted forests. The villagers lived in peace, but one day, strange creatures began to emerge from the forest, causing havoc. A young hero named Elara decided to venture into the forest to discover the source of the disturbance. After many challenges, she found an ancient tree with magical powers that had been disturbed by a group of treasure hunters. Elara managed to calm the tree and restore peace to the village.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to create a fictional narrative based on the following theme:

Theme: {t['theme']}

Requirements: {t['requirements']}

Ensure that your story includes at least one main character, a conflict, and a resolution. The setting should be vividly described, and the narrative should be engaging and coherent. The story should be at least 300 words long. Provide your response in plain text format."""
        else:
            return f"""Your task is to interpret the following story and analyze its narrative elements:

Story: {t['story']}

Your analysis should include the identification of the main character, the conflict, the resolution, and a description of the setting. Additionally, provide an evaluation of the narrative's coherence and engagement. Provide your response in plain text format with the following structure:

1. Main Character: [Identify the main character]
2. Conflict: [Describe the conflict]
3. Resolution: [Describe the resolution]
4. Setting: [Describe the setting]
5. Coherence: [Evaluate the narrative's coherence]
6. Engagement: [Evaluate the narrative's engagement]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = [
                "The story should include at least one main character.",
                "The story should have a clear conflict and resolution.",
                "The setting should be vividly described.",
                "The narrative should be engaging and coherent.",
                "The story should be at least 300 words long."
            ]
        else:
            criteria = [
                "The analysis should identify the main character.",
                "The analysis should identify the conflict and resolution.",
                "The analysis should describe the setting.",
                "The analysis should evaluate the narrative's coherence and engagement."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
