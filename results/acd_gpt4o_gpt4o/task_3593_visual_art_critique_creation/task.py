class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "art_piece": "Starry Night by Vincent van Gogh",
                "criteria": "Critique the piece focusing on elements such as color, composition, emotion, and technique."
            },
            "2": {
                "theme": "A futuristic cityscape at dawn",
                "criteria": "Describe a new piece of art based on this theme. Focus on elements such as color, composition, emotion, and technique."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to either critique the given piece of visual art or create a new conceptual art piece based on the specified theme. Provide a detailed explanation that aligns with the criteria provided.\n\nFor critique:\nArt Piece: {t.get('art_piece', '')}\nCriteria: {t.get('criteria', '')}\n\nFor creation:\nTheme: {t.get('theme', '')}\nCriteria: {t.get('criteria', '')}\n\nProvide your response in plain text format. Ensure your response includes:\n- For critique: A detailed analysis of the art piece focusing on elements such as color, composition, emotion, and technique.\n- For creation: A detailed description of the conceptualized art piece focusing on elements such as color, composition, emotion, and technique.\n\nFormat your response as follows:\n- Critique/Description: [Your detailed analysis or description]\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should align with the specified criteria.", "The analysis or description should demonstrate a deep understanding of the visual art elements such as color, composition, emotion, and technique."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
