class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "composition": "Twinkle, Twinkle, Little Star",
                "criteria": "Suggest improvements to make the composition more suitable for a modern pop audience. Focus on elements like melody, harmony, rhythm, and instrumentation."
            },
            "2": {
                "composition": "Beethoven's Für Elise",
                "criteria": "Suggest modifications to adapt the piece for a jazz trio. Focus on elements like melody, harmony, rhythm, and instrumentation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the given musical composition and suggest improvements or modifications based on the specified criteria. Provide a detailed explanation of your suggestions and ensure they align with the criteria provided.\n\nComposition: {t['composition']}\n\nCriteria: {t['criteria']}\n\nProvide your analysis and suggestions in plain text format. Ensure your response includes: 1. A detailed analysis of the original composition, including its melody, harmony, rhythm, and instrumentation, 2. Specific improvements or modifications, 3. Justifications for your suggestions.\n\nFormat your response as follows:\n- Analysis: [Your analysis]\n- Improvements/Modifications: [Your suggestions]\n- Justifications: [Your justifications]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The suggestions should align with the specified criteria.", "The analysis should demonstrate a deep understanding of the original composition, including its melody, harmony, rhythm, and instrumentation.", "The improvements or modifications should be creatively and musically coherent.", "The justifications should be logical and well-explained."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
