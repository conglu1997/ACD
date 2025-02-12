class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A peaceful morning in the countryside", "description": "Compose a short piece of music that captures the essence of a peaceful morning in the countryside. Describe the instruments used, the tempo, and the overall mood of the piece. The piece should be between 1-2 minutes long."},
            "2": {"notation": "C4 E4 G4 C5", "description": "Interpret the given musical notation and describe the type of piece it could represent. Include the possible instruments, tempo, and mood. Provide a brief narrative of how the piece progresses."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Your task is to compose a short piece of music based on the given theme. Ensure that your composition captures the essence of the theme. Provide a description of the instruments used, the tempo, and the overall mood of the piece. The piece should be between 1-2 minutes long.

Theme: {t['theme']}

Response format: 
1. Composition description (text)
2. Instruments used (text)
3. Tempo (text)
4. Overall mood (text)"""
        else:
            return f"""Your task is to interpret the given musical notation and describe the type of piece it could represent. Include the possible instruments, tempo, and mood in your description. Provide a brief narrative of how the piece progresses.

Musical Notation: {t['notation']}

Response format: 
1. Interpretation (text)
2. Possible instruments (text)
3. Tempo (text)
4. Mood (text)
5. Narrative (text)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = [
                "The composition should capture the essence of the given theme.",
                "The description should include the instruments used, the tempo, and the overall mood.",
                "The piece should be between 1-2 minutes long.",
                "The response should be creative and coherent."]
        else:
            criteria = [
                "The interpretation should reflect the given musical notation accurately.",
                "The description should include possible instruments, tempo, and mood.",
                "The response should include a brief narrative of how the piece progresses.",
                "The response should be detailed and insightful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
