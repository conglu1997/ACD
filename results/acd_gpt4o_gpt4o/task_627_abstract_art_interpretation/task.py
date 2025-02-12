class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "art_piece": "Abstract Art Piece 1", "image_url": "https://example.com/art1.jpg", "prompt": "Interpret the emotions and themes conveyed by this art piece."},
            "2": {"task_type": "generate", "description": "A chaotic mix of colors and shapes suggesting confusion.", "prompt": "Generate an abstract art description that conveys themes of confusion and chaos."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following abstract art piece and explain the emotions and themes it conveys.\n\nArt Piece: {t['art_piece']}\nImage URL: {t['image_url']}\n\nEnsure your interpretation is detailed and captures the essence of the art piece. Provide your response in the following format:\n\nInterpretation: [Your interpretation]\n\nExample: If the art piece is a swirl of dark colors with sharp edges, an appropriate interpretation could be 'The use of dark colors and sharp edges suggests feelings of anger and turmoil.'\n"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a description of an abstract art piece that conveys themes of confusion and chaos based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure your description is vivid and captures the essence of confusion and chaos. Provide your response in the following format:\n\nDescription: [Your description]\n\nExample: For a chaotic mix of colors and shapes, an appropriate description could be 'A whirlwind of clashing colors and jagged lines that evoke a sense of disarray and unpredictability.'\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The response should be formatted as 'Interpretation: [Your interpretation]'.", "The interpretation must capture the emotions and themes conveyed by the art piece.", "The interpretation must be detailed and relevant to the art piece."]
        elif t['task_type'] == 'generate':
            criteria = ["The response should be formatted as 'Description: [Your description]'.", "The description must convey themes of confusion and chaos.", "The description must be vivid and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
