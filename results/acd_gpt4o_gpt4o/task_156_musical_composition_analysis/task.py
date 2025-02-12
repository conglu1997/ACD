class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "Compose a short piece of music in the style of a waltz with a 3/4 time signature and a cheerful mood. Provide the composition in plain text format using musical notation or a simplified representation."},
            "2": {"piece": "Twinkle, Twinkle, Little Star", "question": "Analyze the piece 'Twinkle, Twinkle, Little Star' and identify its key elements such as melody, harmony, and structure. Provide your analysis in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "parameters" in t:
            instructions = f"""Your task is to compose a short piece of music based on the following parameters:

Parameters: {t['parameters']}

Ensure that the composition adheres to the given style, time signature, and mood. Provide the composition in plain text format using musical notation or a simplified representation."""
        else:
            instructions = f"""Your task is to analyze the following piece of music and identify its key elements:

Piece: {t['piece']}

Question: {t['question']}

Your analysis should be clear, detailed, and cover aspects such as melody, harmony, and structure. Provide your analysis in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "parameters" in t:
            criteria = [
                "The composition should adhere to the given style (waltz), time signature (3/4), and mood (cheerful).",
                "The composition should be clear and coherent, using musical notation or a simplified representation."]
        else:
            criteria = [
                "The analysis should cover key elements such as melody, harmony, and structure.",
                "The analysis should be clear, detailed, and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
