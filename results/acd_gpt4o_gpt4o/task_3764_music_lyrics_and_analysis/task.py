class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "melody": "C D E F G A B C",
                "requirements": "Generate lyrics that fit the mood and rhythm of the given melody."
            },
            "2": {
                "music_piece": "Twinkle, Twinkle, Little Star",
                "requirements": "Analyze the piece and identify its structure (e.g., verses, chorus, bridge)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "melody" in t:
            return (
                "Your task is to generate lyrics for the given melody. Ensure that the lyrics fit the mood and rhythm of the melody. "
                "Provide your response in the following format: \n\n"
                "1. Melody \n"
                "2. Generated Lyrics"
            )
        elif "music_piece" in t:
            return (
                "Your task is to analyze the given piece of music and identify its structure. Provide a detailed analysis, including the identification of verses, chorus, bridge, and any other relevant sections. "
                "Provide your response in the following format: \n\n"
                "1. Music Piece \n"
                "2. Analysis"
            )
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "melody" in t:
            criteria = [
                "The generated lyrics should fit the mood and rhythm of the given melody.",
                "The lyrics should be coherent and meaningful."
            ]
        elif "music_piece" in t:
            criteria = [
                "The analysis should correctly identify the structure of the piece.",
                "The response should be detailed and accurate."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
