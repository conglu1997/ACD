class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"musical_piece": "A 4-bar melody in C major with a simple I-IV-V-I chord progression. The melody primarily uses quarter notes and has a bright, cheerful character."},
            "2": {"composition_criteria": "Compose a 4-bar melody in A minor that uses a I-VI-III-VII chord progression. The melody should evoke a sense of melancholy and use a mix of quarter notes and eighth notes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'musical_piece' in t:
            return f"""Your task is to analyze the following musical piece based on its description.

Musical Piece Description:
{t['musical_piece']}

Instructions:
1. Provide a detailed analysis of the musical piece, discussing its melody, harmony, rhythm, and overall character.
2. Suggest potential improvements or changes to enhance the musical piece.

Your response should be in the following format:
Analysis: [Your analysis]
Suggestions: [Your suggestions]"""
        elif 'composition_criteria' in t:
            return f"""Your task is to compose a short piece of music based on the given criteria.

Composition Criteria:
{t['composition_criteria']}

Instructions:
1. Provide a detailed description of the new musical piece, ensuring that it includes all the specified elements.
2. Ensure that your description is coherent and captures the essence of the specified style and character.

Your response should be in the following format:
Composition: [Your composition]
Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'musical_piece' in t:
            criteria = ["The analysis should discuss the melody, harmony, rhythm, and overall character of the musical piece.", "The suggestions should be relevant and aimed at enhancing the musical piece."]
        elif 'composition_criteria' in t:
            criteria = ["The composition should include all specified elements in a coherent and detailed manner.", "The composition should capture the essence of the specified style and character."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
