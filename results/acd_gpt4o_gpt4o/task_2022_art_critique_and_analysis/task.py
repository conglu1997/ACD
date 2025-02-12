class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Analyze the famous painting 'Starry Night' by Vincent van Gogh. Provide a detailed analysis, including the use of color, composition, brushwork, and emotional impact. Additionally, discuss the historical context and significance of the painting.", "criteria": ["The analysis should be detailed and cover all specified aspects.", "The historical context should be accurate and relevant.", "The emotional impact should be thoughtfully discussed."]},
            "2": {"task": "Imagine a painting titled 'The Enchanted Forest' which depicts a magical forest scene at twilight. The painting features vibrant colors, whimsical creatures, and a serene atmosphere. Critique this hypothetical artwork, discussing its composition, use of color, thematic elements, and overall aesthetic appeal.", "criteria": ["The critique should be thorough and cover all specified aspects.", "The interpretation should be creative and insightful.", "The overall critique should be coherent and well-structured."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "task" in t and "Starry Night" in t["task"]:
            instructions = """Your task is to analyze the famous painting 'Starry Night' by Vincent van Gogh. Provide a detailed analysis, including the use of color, composition, brushwork, and emotional impact. Additionally, discuss the historical context and significance of the painting. Ensure that your analysis is detailed, accurate, and well-structured. Provide your response in the following format:\n\nAnalysis: [Your analysis]"""
        else:
            instructions = """Your task is to critique a hypothetical painting titled 'The Enchanted Forest', which depicts a magical forest scene at twilight. The painting features vibrant colors, whimsical creatures, and a serene atmosphere. Critique this hypothetical artwork, discussing its composition, use of color, thematic elements, and overall aesthetic appeal. Ensure that your critique is thorough, creative, and well-structured. Provide your response in the following format:\n\nCritique: [Your critique]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get("criteria", [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
