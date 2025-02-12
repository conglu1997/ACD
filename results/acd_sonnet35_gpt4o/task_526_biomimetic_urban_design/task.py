import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "challenge": "Water scarcity",
                "inspiration": "Namib desert beetle's water collection mechanism"
            },
            {
                "challenge": "Urban heat island effect",
                "inspiration": "Termite mound ventilation systems"
            },
            {
                "challenge": "Air pollution",
                "inspiration": "Spider web's ability to capture particles"
            },
            {
                "challenge": "Food production in limited space",
                "inspiration": "Forest canopy layering"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(challenges, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic urban system that addresses the environmental challenge of {t['challenge']}, drawing inspiration from {t['inspiration']}. Your task is to create an innovative urban design solution that integrates principles from biology, architecture, and urban planning.

Provide your response in the following format:

1. Concept Overview (100-150 words):
   Describe your biomimetic urban system, explaining how it addresses the environmental challenge and incorporates the biological inspiration.

2. Key Design Elements (200-250 words):
   a) Identify and explain three key design elements of your system.
   b) For each element, describe how it mimics the biological inspiration and contributes to solving the environmental challenge.

3. Implementation Strategy (150-200 words):
   Outline a strategy for implementing your biomimetic urban system in an existing city, considering practical constraints and potential obstacles.

4. Environmental Impact Analysis (150-200 words):
   Analyze the potential positive and negative environmental impacts of your system, including any unintended consequences.

5. Societal Implications (100-150 words):
   Discuss how your biomimetic urban system might affect social dynamics, quality of life, or economic factors in the city.

6. Future Adaptations (100-150 words):
   Propose one way your system could be adapted or expanded to address an additional urban challenge not initially considered in your design.

Ensure your response demonstrates a deep understanding of biomimicry principles, urban design concepts, and environmental science. Be creative in your approach while maintaining scientific and practical plausibility. Use clear headings for each section of your response.

Your total response should be between 800-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the environmental challenge of {t['challenge']} and draw inspiration from {t['inspiration']}",
            "The biomimetic urban system design should be innovative, coherent, and demonstrate a clear understanding of biomimicry principles",
            "The response should show interdisciplinary integration of biology, architecture, and urban planning concepts",
            "The environmental impact analysis and societal implications should be thoughtful and well-reasoned",
            "The proposed future adaptation should be creative and relevant to urban challenges"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
