class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image": "<URL to image 1>", "criteria": "Analyze the elements of composition, color usage, and overall theme. Provide specific observations on the arrangement of elements, the color palette, and the central theme of the artwork. Use art terminology where appropriate."},
            "2": {"image": "<URL to image 2>", "criteria": "Interpret the emotions conveyed, the use of light and shadow, and the historical context. Provide specific observations on the emotional tone, light and shadow effects, and the historical significance of the artwork. Use art terminology where appropriate."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given artwork based on the specified criteria. Ensure that your analysis is well-detailed, coherent, and includes specific observations that support your interpretation. Use art terminology where appropriate. Provide your response in plain text format.\n\nArtwork: {t['image']}\nCriteria: {t['criteria']}\n\nResponse format:\n1. Composition: [Detailed analysis of the composition] (if applicable)\n2. Color Usage: [Detailed analysis of color usage] (if applicable)\n3. Theme: [Detailed analysis of the theme] (if applicable)\n4. Emotions: [Detailed interpretation of emotions] (if applicable)\n5. Light and Shadow: [Detailed analysis of light and shadow] (if applicable)\n6. Historical Context: [Detailed interpretation of historical context] (if applicable)\n\nExample response:\nComposition: The artwork is divided into three main sections, with a strong diagonal line creating a sense of movement.\nColor Usage: The color palette is dominated by warm tones, creating a feeling of warmth and comfort.\nTheme: The central theme appears to be the harmony between nature and humanity.\nEmotions: The artwork conveys a sense of calm and tranquility.\nLight and Shadow: The use of light and shadow creates a dramatic contrast, highlighting the central figures.\nHistorical Context: The artwork reflects the artistic trends of the early 20th century, with influences from Impressionism."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be well-detailed and coherent.", "The analysis should include specific observations that support the interpretation.", "The response should follow the specified format.", "The response should use appropriate art terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
