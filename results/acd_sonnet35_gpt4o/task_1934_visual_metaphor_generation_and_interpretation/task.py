import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "type": "generate",
                "concept": "time is money",
                "style": "minimalist"
            },
            {
                "type": "generate",
                "concept": "knowledge is power",
                "style": "surrealist"
            },
            {
                "type": "interpret",
                "image_description": "A tree with books as leaves growing from a human brain"
            },
            {
                "type": "interpret",
                "image_description": "A ticking clock with its hands made of burning candles"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generate':
            return f"Generate a detailed description of a visual metaphor for the concept '{t['concept']}' in a {t['style']} style. Your response should follow this structure:\n\n1. Visual Elements: List and describe the main visual components.\n2. Composition: Explain how these elements are arranged.\n3. Metaphorical Representation: Describe how each element represents aspects of the concept.\n4. Visual Details: Specify colors, textures, and other relevant visual characteristics.\n5. Effectiveness: Explain why this visual metaphor effectively conveys the concept.\n6. Potential Interpretations: Discuss possible ways viewers might interpret this visual metaphor."
        elif t['type'] == 'interpret':
            return f"Interpret the following visual metaphor:\n\n{t['image_description']}\n\nYour response should follow this structure:\n\n1. Initial Impression: Describe your first thoughts on seeing this image.\n2. Element Analysis: Break down the key visual elements and their potential symbolic meanings.\n3. Metaphorical Interpretation: Explain what concept or idea you think this visual metaphor represents.\n4. Justification: Provide reasoning for your interpretation, linking the visual elements to the concept.\n5. Alternative Perspectives: Suggest at least one alternative interpretation and explain why it might be valid.\n6. Effectiveness Evaluation: Assess how effectively this visual metaphor conveys its intended message."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the specified structure completely",
            "The explanation demonstrates a deep understanding of visual metaphors and their interpretation",
            "The response shows creativity and insight in generating or interpreting the visual metaphor",
            "The analysis is thorough, considering multiple perspectives and potential interpretations",
            "The reasoning is clear, coherent, and well-justified"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
