import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            ("Wave interference", "Polyrhythms"),
            ("Quantum entanglement", "Counterpoint"),
            ("Brownian motion", "Aleatoric music"),
            ("Resonance", "Overtone series"),
            ("Entropy", "Twelve-tone technique")
        ]
        return {str(i+1): {"phenomenon": pair[0], "musical_concept": pair[1]} for i, pair in enumerate(random.sample(phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a musical composition inspired by the physical phenomenon of {t['phenomenon']} and analyze its mathematical properties. Incorporate the musical concept of {t['musical_concept']} in your composition.

Follow these steps:

1. Briefly explain the physical phenomenon and the musical concept (1-2 sentences each).
2. Describe your musical composition, explaining how it incorporates both the physical phenomenon and the musical concept (3-4 sentences).
3. Provide a short musical score representation of your composition using note names (e.g., C4, D#5) and rhythm notations (e.g., q for quarter note, e for eighth note). Include at least 8 measures, with bar lines represented by '|'.
4. Analyze the mathematical properties of your composition, such as frequency ratios, rhythmic patterns, or structural symmetries (2-3 sentences).
5. Explain how your composition could be used to demonstrate or teach the physical phenomenon to students (2-3 sentences).

Format your response as follows:

Physical Phenomenon ({t['phenomenon']}): [Your explanation]
Musical Concept ({t['musical_concept']}): [Your explanation]
Composition Description: [Your description]
Musical Score:
[Your score representation]
Mathematical Analysis: [Your analysis]
Educational Application: [Your explanation]

Ensure that your composition is musically coherent, creatively incorporates the physical phenomenon and musical concept, and demonstrates a clear understanding of the mathematical relationships involved."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include brief explanations of both {t['phenomenon']} and {t['musical_concept']}",
            "The composition description should clearly incorporate both the physical phenomenon and the musical concept",
            "The musical score should be provided in the specified format and be at least 8 measures long",
            "The mathematical analysis should identify relevant properties of the composition",
            "The educational application should logically connect the composition to the physical phenomenon",
            "The response should demonstrate interdisciplinary knowledge and creative problem-solving",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
