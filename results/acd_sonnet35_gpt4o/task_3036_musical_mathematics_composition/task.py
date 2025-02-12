import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "Golden ratio",
            "Prime numbers",
            "Fractals"
        ]
        musical_elements = [
            "Rhythm",
            "Melody",
            "Harmony",
            "Timbre"
        ]
        return {
            "1": {"concept": random.choice(mathematical_concepts), "element": random.choice(musical_elements)},
            "2": {"concept": random.choice(mathematical_concepts), "element": random.choice(musical_elements)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a musical composition system based on the mathematical concept of {t['concept']}, focusing primarily on the musical element of {t['element']}. Then, use this system to compose a short piece that expresses the essence of {t['concept']}. Your response should include:\n\n1. Mathematical-Musical System Design (250-300 words):\n   a) Explain how you translate {t['concept']} into musical parameters.\n   b) Describe the rules and constraints of your composition system.\n   c) Discuss how your system incorporates {t['element']} as a primary focus.\n   d) Provide a simple example of how a mathematical property maps to a musical property in your system.\n\n2. Composition Process (200-250 words):\n   a) Describe step-by-step how you use your system to compose a piece.\n   b) Explain any creative decisions made within the constraints of your system.\n   c) Discuss how your process ensures the piece expresses the essence of {t['concept']}.\n\n3. Musical Analysis (200-250 words):\n   a) Provide a detailed description of your composed piece.\n   b) Analyze how the piece reflects the mathematical concept of {t['concept']}.\n   c) Explain how the focus on {t['element']} contributes to expressing the mathematical concept.\n\n4. Mathematical Analysis (150-200 words):\n   a) Discuss the mathematical properties or patterns present in your composition.\n   b) Explain how these properties relate to {t['concept']}.\n   c) Provide at least one mathematical formula or equation relevant to your composition.\n\n5. Artistic Interpretation (150-200 words):\n   a) Reflect on the artistic qualities of your composition beyond its mathematical basis.\n   b) Discuss how your system balances mathematical rigor with musical aesthetics.\n   c) Propose how listeners might perceive or interpret the mathematical concept through your music.\n\n6. Potential Applications and Extensions (150-200 words):\n   a) Suggest potential applications of your mathematical-musical system in music education or composition.\n   b) Propose an extension of your system to incorporate other mathematical concepts or musical elements.\n   c) Discuss how your approach might contribute to the field of algorithmic composition or music theory.\n\nEnsure your response demonstrates a deep understanding of both mathematics and music theory. Be creative in your system design and composition while maintaining mathematical accuracy. Use appropriate terminology from both fields and provide clear explanations for complex concepts.\n\nYour total response should be between 1100-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified mathematical concept and its application to music.",
            "The musical composition system is well-designed and effectively translates mathematical principles into musical parameters.",
            "The composed piece successfully expresses the essence of the given mathematical concept.",
            "The analysis shows a deep understanding of both the mathematical and musical aspects of the composition.",
            "The response balances creativity with mathematical rigor and musical aesthetics.",
            "The proposed applications and extensions are innovative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
