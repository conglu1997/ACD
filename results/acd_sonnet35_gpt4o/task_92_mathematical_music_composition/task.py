import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "mathematical_principle": "Mandelbrot set",
                "musical_constraint": "Serialist technique (using a fixed series of pitches)",
                "time_signature": "13/8",
                "related_concept": "Quantum entanglement"
            },
            {
                "mathematical_principle": "Euler's identity",
                "musical_constraint": "Microtonal scale (using intervals smaller than a semitone)",
                "time_signature": "7/4",
                "related_concept": "Theory of relativity"
            },
            {
                "mathematical_principle": "Riemann hypothesis",
                "musical_constraint": "Spectral music (based on sound spectra)",
                "time_signature": "11/16",
                "related_concept": "DNA replication"
            },
            {
                "mathematical_principle": "Möbius strip",
                "musical_constraint": "Polyrhythmic structure (multiple conflicting rhythms)",
                "time_signature": "5/8 + 7/8",
                "related_concept": "Plate tectonics"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Compose a short musical piece based on the following parameters:\n\n" \
               f"1. Mathematical Principle: {t['mathematical_principle']}\n" \
               f"2. Musical Constraint: {t['musical_constraint']}\n" \
               f"3. Time Signature: {t['time_signature']}\n" \
               f"4. Related Concept: {t['related_concept']}\n\n" \
               f"Your response should include the following sections, clearly labeled and within the specified word limits:\n\n" \
               f"a) Mathematical Incorporation (50-75 words): Explain how you incorporated the mathematical principle into your composition.\n" \
               f"b) Musical Constraint Application (50-75 words): Describe how you applied the musical constraint.\n" \
               f"c) Time Signature Analysis (25-50 words): Analyze how the time signature influences the rhythm and feel of the piece.\n" \
               f"d) Composition (no word limit): Provide a textual representation of your composition using note names (e.g., C4, D#5) and rhythm notations (e.g., q for quarter note, e for eighth note). Include at least 16 measures, with bar lines represented by '|'.\n" \
               f"e) Conceptual Integration (50-75 words): Explain how your composition relates to or represents the given scientific concept or historical event.\n" \
               f"f) Innovation (25-50 words): Explain one unique or innovative aspect of your composition.\n" \
               f"g) Real-world Application (50-75 words): Describe a potential real-world application or implication of your composition.\n\n" \
               f"Ensure your composition is musically coherent while adhering to the given constraints, incorporating the mathematical principle creatively, and drawing meaningful connections to the related concept. Balance creativity with strict adherence to the specified parameters."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The composition clearly and creatively incorporates the {t['mathematical_principle']}, with a specific explanation of how it is used.",
            f"The piece strictly adheres to the {t['musical_constraint']}, demonstrating understanding of the technique.",
            f"The composition is correctly written in {t['time_signature']} time signature, with a clear analysis of its impact.",
            "The response includes all required sections (a-g) as specified, adhering to the given word limits.",
            "The composition is musically coherent and demonstrates advanced understanding of music theory concepts.",
            "The textual representation of the composition includes both note names and rhythm notations for at least 16 measures.",
            f"The composition draws meaningful and creative connections to the related concept: {t['related_concept']}.",
            "The described innovation is unique, relevant to the composition, and well-explained.",
            "The proposed real-world application or implication is plausible, well-reasoned, and original.",
            "The overall response balances creativity with strict adherence to the given parameters and constraints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
