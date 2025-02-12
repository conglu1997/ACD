import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'love', 'surprise']
        mathematical_concepts = ['Fibonacci sequence', 'golden ratio', 'prime numbers', 'fractals', 'chaos theory']
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'avant-garde']
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "math_concept": random.choice(mathematical_concepts),
                "style": random.choice(musical_styles)
            },
            "2": {
                "emotion": random.choice(emotions),
                "math_concept": random.choice(mathematical_concepts),
                "style": random.choice(musical_styles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music based on mathematical principles and emotional intent. Your system should create a {t['style']} composition that expresses the emotion of {t['emotion']} using the mathematical concept of {t['math_concept']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI music composition system.\n   b) Explain how it incorporates the given mathematical concept.\n   c) Detail how the system interprets and expresses the specified emotion.\n   d) Outline how it adheres to the given musical style.\n\n2. Composition Algorithm (200-250 words):\n   a) Provide a high-level description of the main algorithm used for composition.\n   b) Include a simple pseudocode representation (8-10 lines) of a key part of this algorithm.\n   c) Explain how the algorithm integrates the mathematical concept, emotion, and musical style.\n\n3. Emotional-Mathematical Mapping (150-200 words):\n   a) Describe how your system maps the given emotion to musical elements (e.g., tempo, key, rhythm).\n   b) Explain how the mathematical concept influences these mappings.\n   c) Discuss any challenges in this mapping process and how you addressed them.\n\n4. Style Adaptation (150-200 words):\n   a) Explain how your system adapts its composition to the specified musical style.\n   b) Describe any style-specific rules or constraints implemented in your system.\n   c) Discuss how the system balances style adherence with emotional expression and mathematical structure.\n\n5. Evaluation and Iteration (150-200 words):\n   a) Propose a method for evaluating the quality and effectiveness of the compositions.\n   b) Describe how your system might iterate and improve its compositions based on feedback.\n   c) Discuss potential limitations of your approach and areas for future improvement.\n\n6. Ethical and Creative Implications (100-150 words):\n   a) Discuss the ethical implications of using AI for creative tasks like music composition.\n   b) Explore how this technology might impact human creativity and the music industry.\n\nEnsure your response demonstrates a deep understanding of music theory, mathematical concepts, and AI principles. Be creative in your approach while maintaining scientific and artistic plausibility. Use appropriate technical terminology and provide clear explanations where necessary."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, the specified mathematical concept, and AI principles.",
            "The system architecture and composition algorithm are well-explained and integrate the emotion, mathematical concept, and musical style effectively.",
            "The emotional-mathematical mapping and style adaptation are clearly described and plausible.",
            "The evaluation method and ethical implications are thoughtfully discussed.",
            "The response is creative while maintaining scientific and artistic plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
