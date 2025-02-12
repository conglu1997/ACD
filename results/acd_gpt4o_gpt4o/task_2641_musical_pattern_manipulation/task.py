class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "C-E-G", "manipulation": "Create an inversion of this pattern. Inversion means reversing the interval direction of each note relative to the starting note. For example, if the original pattern is 'C-E-G', an inversion could be 'C-A-F' where the intervals between C-E-G (up-4, up-3) are changed to C-A-F (down-3, down-4)."},
            "2": {"pattern": "A-B-C-D", "analysis": "Identify whether this pattern forms a recognizable musical scale or sequence, such as a major scale, minor scale, pentatonic scale, or any other well-known sequence, and explain your reasoning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "manipulation" in t:
            return f"""Your task is to manipulate the given musical pattern based on the specified criteria:

Pattern: {t['pattern']}

Manipulation: {t['manipulation']}

Ensure your response adheres to the criteria and provide the resulting musical pattern in plain text format. For example, 'C-A-F' for an inversion."""
        elif "analysis" in t:
            return f"""Your task is to analyze the given musical pattern and provide your insights based on the specified query:

Pattern: {t['pattern']}

Analysis: {t['analysis']}

Ensure your analysis is clear, detailed, and accurate. Provide your response in plain text format. For example, 'The pattern is a sequence of ascending whole steps, which is part of a major scale.'"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "manipulation" in t:
            criteria = ["The response should provide a valid inversion of the original pattern by reversing the interval direction of each note relative to the starting note."]
        elif "analysis" in t:
            criteria = ["The response should correctly identify whether the pattern forms a recognizable musical scale or sequence and provide a clear, accurate explanation."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
