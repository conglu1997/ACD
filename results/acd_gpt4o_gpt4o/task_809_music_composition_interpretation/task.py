class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "music_piece": "Beethoven's Symphony No. 5 - First Movement", "audio_url": "https://example.com/beethoven5.mp3", "prompt": "Interpret the emotions and themes conveyed by this music piece."},
            "2": {"task_type": "compose", "description": "A lively and energetic piece with a fast tempo.", "prompt": "Compose a new music piece that conveys themes of liveliness and energy with a fast tempo."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following music piece and explain the emotions and themes it conveys.\n\nMusic Piece: {t['music_piece']}\nAudio URL: {t['audio_url']}\n\nEnsure your interpretation is detailed and captures the essence of the music piece. Provide your response in the following format:\n\nInterpretation: [Your interpretation]\n\nExample: If the music is fast-paced and in a minor key, an appropriate interpretation could be 'The use of a fast tempo and minor key suggests feelings of urgency and tension.'\n"""
        elif t['task_type'] == 'compose':
            return f"""Your task is to compose a description of a new music piece that conveys themes of liveliness and energy with a fast tempo based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure your composition is vivid and captures the essence of liveliness and energy. Provide your response in the following format:\n\nComposition: [Your composition]\n\nExample: For a lively and energetic piece, an appropriate composition could be 'A fast-paced melody with staccato notes and a strong rhythmic drive that evokes a sense of excitement and movement.'\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The response should be formatted as 'Interpretation: [Your interpretation]'.", "The interpretation must capture the emotions and themes conveyed by the music piece.", "The interpretation must be detailed and relevant to the music piece."]
        elif t['task_type'] == 'compose':
            criteria = ["The response should be formatted as 'Composition: [Your composition]'.", "The composition must convey themes of liveliness and energy.", "The composition must be vivid and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
