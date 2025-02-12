import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "math_concept": "Möbius strip",
                "linguistic_style": "Poetic prose",
                "visual_constraint": "Use only straight lines"
            },
            {
                "math_concept": "Mandelbrot set",
                "linguistic_style": "Scientific jargon",
                "visual_constraint": "Use only circles and spirals"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(concepts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a system that translates the mathematical concept of {t['math_concept']} into a linguistic description using {t['linguistic_style']} and a visual representation adhering to the constraint: {t['visual_constraint']}. Then, analyze the implications of this translation process. Your response should include:

1. Concept Translation (300-350 words):
   a) Provide a clear explanation of the {t['math_concept']} using {t['linguistic_style']}.
   b) Describe a visual representation of the concept that adheres to the constraint: {t['visual_constraint']}.
   c) Explain how your linguistic and visual representations capture the essence of the mathematical concept.

2. Translation Process (200-250 words):
   a) Describe the step-by-step process you used to translate the mathematical concept into linguistic and visual forms.
   b) Discuss any challenges you encountered and how you overcame them.
   c) Explain how you ensured accuracy and clarity in your translations.

3. Cognitive Analysis (200-250 words):
   a) Analyze how your translations might affect understanding and memory of the mathematical concept.
   b) Discuss potential benefits and drawbacks of using such translations in mathematical education.
   c) Explore how different individuals (e.g., visual learners, verbal learners) might respond to your translations.

4. Cross-modal Synesthesia (150-200 words):
   a) Discuss how your translation system relates to the phenomenon of synesthesia.
   b) Explore potential applications of this type of cross-modal translation in other fields.
   c) Speculate on how AI systems might develop or simulate synesthetic-like abilities.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss any ethical considerations related to translating abstract concepts across modalities.
   b) Explore philosophical questions raised by the ability to represent mathematical concepts in diverse forms.
   c) Consider potential societal impacts of widespread use of such translation systems.

Ensure your response demonstrates a deep understanding of the mathematical concept, linguistic principles, and visual design. Be creative in your approach while maintaining scientific accuracy. Use appropriate terminology from mathematics, linguistics, and cognitive science.

Format your response with clear headings for each section (e.g., '1. Concept Translation', '2. Translation Process', etc.). Your total response should be between 1000-1250 words. Adhere to the specified word count for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of {t['math_concept']} using {t['linguistic_style']}",
            f"A visual representation adhering to the constraint '{t['visual_constraint']}' is described",
            "The translation process and cognitive analysis are thoroughly explained",
            "The response demonstrates creativity and interdisciplinary knowledge integration",
            "Ethical and philosophical implications are thoughtfully addressed",
            "The response adheres to the specified word count for each section and overall"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
