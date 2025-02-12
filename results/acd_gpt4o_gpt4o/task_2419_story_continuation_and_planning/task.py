class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "Once upon a time in a small village, there was a young girl named Lily who discovered a mysterious glowing stone in the forest. Curious and brave, she decided to take it home and investigate its origin."},
            "2": {"story": "In a distant kingdom, the king has fallen ill, and the only cure lies in a hidden garden guarded by mythical creatures. A young knight volunteers to embark on this perilous journey to save the king.", "guidelines": "The knight should face three major challenges: a riddle from a sphinx, a battle with a dragon, and a moral dilemma involving the garden's guardian."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'story' in t and 'guidelines' not in t:
            return f"""Your task is to continue the following story. Ensure that your continuation is coherent, engaging, and logically follows from the given narrative. Provide your response in plain text format.

Story: {t['story']}"""
        elif 'story' in t and 'guidelines' in t:
            return f"""Your task is to continue the following story and outline a plan for the subsequent events based on the specified guidelines. Ensure that your continuation is coherent, engaging, and logically follows from the given narrative. Additionally, provide a detailed plan for the subsequent events, including the challenges and their resolutions. Provide your response in plain text format.

Story: {t['story']}
Guidelines: {t['guidelines']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should be coherent and logically follow from the given narrative.",
            "The continuation should be engaging and maintain the story's tone.",
            "If guidelines are provided, the plan should include the specified challenges and their resolutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
