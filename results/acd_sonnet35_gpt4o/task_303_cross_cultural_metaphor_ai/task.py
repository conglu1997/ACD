import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_types = [
            {
                "type": "Embodied Metaphor",
                "description": "Metaphors based on physical experiences and bodily sensations"
            },
            {
                "type": "Structural Metaphor",
                "description": "Metaphors that map one concept onto another, more complex concept"
            }
        ]
        cultures = [
            "Japanese",
            "Brazilian",
            "Egyptian",
            "Finnish"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "metaphor_type": random.choice(metaphor_types),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != tasks.get(str(i), {}).get("source_culture")])
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system capable of generating and interpreting metaphors across different languages and cultures. Focus on {t['metaphor_type']['type']} metaphors, translating from {t['source_culture']} culture to {t['target_culture']} culture.

Your task is to:

1. System Design (250-300 words):
   a) Describe the architecture of your AI system, including the main components and their functions.
   b) Explain how your system incorporates cultural knowledge and linguistic patterns to generate and interpret metaphors.
   c) Detail the specific techniques or algorithms used for metaphor generation and interpretation.

2. Metaphor Analysis (200-250 words):
   a) Generate an example metaphor in the {t['source_culture']} culture using your proposed system.
   b) Explain the cultural significance and meaning of this metaphor in the source culture.
   c) Describe how your system would translate or adapt this metaphor for the {t['target_culture']} culture.
   d) Analyze the challenges in preserving the original meaning and emotional impact during this cross-cultural translation.

3. Evaluation Method (150-200 words):
   a) Propose a method to evaluate the effectiveness and cultural accuracy of your AI system's metaphor generation and interpretation.
   b) Describe specific metrics or criteria you would use for this evaluation.
   c) Explain how you would account for cultural biases in the evaluation process.

4. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications or concerns related to using AI for cross-cultural metaphor generation and interpretation.
   b) Propose safeguards or guidelines to address these ethical concerns.

Ensure your response demonstrates a deep understanding of metaphor theory, cultural linguistics, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section and subsections where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections: System Design, Metaphor Analysis, Evaluation Method, and Ethical Considerations",
            "The AI system design is innovative and plausible, incorporating cultural knowledge and linguistic patterns",
            "The metaphor analysis demonstrates a deep understanding of both source and target cultures",
            "The evaluation method is well-thought-out and considers cultural biases",
            "Ethical considerations are thoroughly discussed with proposed safeguards",
            "The response shows interdisciplinary knowledge application and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
