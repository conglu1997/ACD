class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "puzzle", "theme": "ancient ruins", "mechanics": "pattern recognition"},
            "2": {"type": "board game", "theme": "space exploration", "mechanics": "resource management"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a new {t['type']} concept based on the given criteria. Ensure that your concept is well-detailed, coherent, and includes the specified theme and mechanics. Provide the following details in your response:\n\n1. Title: [Title of the puzzle/game]\n2. Description: [Detailed description of the puzzle/game]\n3. Rules: [Rules and objectives of the puzzle/game]\n4. Components: [List of components needed (if any)]\n5. Example play: [An example of how the puzzle/game is played]\n\nHere are the criteria:\nType: {t['type']}\nTheme: {t['theme']}\nMechanics: {t['mechanics']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The concept should be well-detailed and coherent.", "The concept should include the specified theme and mechanics.", "The rules and objectives should be clear and logical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
