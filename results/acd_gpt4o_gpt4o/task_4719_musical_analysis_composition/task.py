class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"music_piece": "Twinkle, Twinkle, Little Star", "criteria": "Compose a variation in a minor key. Ensure that the variation includes at least one modulation to a different minor key and a return to the original minor key."},
            "2": {"music_piece": "Happy Birthday", "criteria": "Compose a variation with a jazz style. Include at least two different jazz techniques such as swing rhythm, blue notes, or improvisation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given piece of music and create a new composition based on the specified criteria.

Music Piece: {t['music_piece']}
Criteria: {t['criteria']}

Ensure your composition adheres to the given criteria and maintains a coherent musical structure. Provide your response in plain text format as follows:

Analysis: <Your analysis of the given music piece>
Composition: <Your new composition based on the criteria>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should accurately describe the given music piece, including its key, tempo, and notable features.", "The composition should adhere to the specified criteria and maintain a coherent musical structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
