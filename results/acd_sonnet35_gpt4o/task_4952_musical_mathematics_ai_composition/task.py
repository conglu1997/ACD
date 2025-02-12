import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "Golden ratio",
            "Fractals",
            "Prime numbers",
            "Modular arithmetic",
            "Chaos theory"
        ]
        music_theory_concepts = [
            "Serialism",
            "Polyrhythms",
            "Microtonal scales",
            "Spectral music",
            "Xenharmonic music",
            "Generative grammar in music"
        ]
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "music_concept": random.choice(music_theory_concepts)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "music_concept": random.choice(music_theory_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on the mathematical principle of {t['math_concept']} and the music theory concept of {t['music_concept']}.

Brief explanations:
- {t['math_concept']}: [Insert a one-sentence explanation of the mathematical concept]
- {t['music_concept']}: [Insert a one-sentence explanation of the music theory concept]

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music composition system.
   b) Explain how you incorporate {t['math_concept']} into the composition process, providing specific mathematical formulas or algorithms where applicable.
   c) Detail how your system implements {t['music_concept']} in its musical output, including any specific techniques or rules used.
   d) Discuss any novel AI techniques or algorithms used in your system.
   e) Provide a simple diagram or pseudocode snippet (5-10 lines) illustrating a key aspect of your system design.
   f) Explain how your system handles potential conflicts between {t['math_concept']} and {t['music_concept']}.

2. Mathematical-Musical Integration (250-300 words):
   a) Explain the relationship between {t['math_concept']} and musical structures or patterns, citing relevant research or examples.
   b) Describe how your system translates mathematical properties into specific musical elements (e.g., pitch, rhythm, form).
   c) Discuss any challenges in mapping {t['math_concept']} to musical parameters and how your system addresses them.

3. Music Theory Implementation (250-300 words):
   a) Detail how your system incorporates {t['music_concept']} into its compositions, providing specific examples of implementation.
   b) Explain any adaptations or interpretations of {t['music_concept']} necessary for AI implementation.
   c) Discuss how your system ensures musical coherence while adhering to {t['music_concept']}.
   d) Describe any novel approaches your system uses to extend or reinterpret {t['music_concept']}.

4. Sample Composition Analysis (200-250 words):
   a) Provide a short description of a hypothetical piece composed by your AI system.
   b) Analyze this piece, explaining how it demonstrates the integration of {t['math_concept']} and {t['music_concept']}.
   c) Discuss any emergent musical properties or unexpected creative outcomes.
   d) Include a brief musical notation or representation (using ASCII art or text) of a key segment of the composition, clearly explaining how it reflects both {t['math_concept']} and {t['music_concept']}.

5. Evaluation and Aesthetics (200-250 words):
   a) Propose methods to evaluate the musical quality and creativity of your AI's compositions, including both computational and human-based approaches.
   b) Discuss the aesthetic implications of using {t['math_concept']} and {t['music_concept']} in AI-generated music.
   c) Consider potential reactions from human composers and music theorists to your system's approach.
   d) Analyze potential limitations of your AI system and areas for improvement.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical concerns related to AI music composition, particularly in the context of your system.
   b) Discuss implications for copyright, artistic authenticity, and the role of human creativity in music.
   c) Propose future research directions or extensions of your system, considering other mathematical or musical concepts.
   d) Suggest potential applications of your system beyond music composition (e.g., music education, music therapy, or musicology research).

Ensure your response demonstrates a deep understanding of music theory, mathematics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining musical and mathematical coherence. Balance technical depth with clarity of explanation throughout your response.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) within each section as outlined. Your total response should be between 1350-1650 words. Present any diagrams, pseudocode, or musical notations as ASCII art or text-based representations within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['math_concept']} and {t['music_concept']}, and their application to music composition.",
            "The proposed AI system architecture is coherent and innovative, addressing potential conflicts between the mathematical principle and music theory concept.",
            "The response provides specific examples of how the system implements both the mathematical and musical concepts in the composition process.",
            "The sample composition analysis includes a well-explained musical notation or representation that clearly reflects both concepts.",
            "The response discusses evaluation methods, aesthetic implications, and potential limitations of the AI system in a balanced manner.",
            "Ethical considerations and future directions are thoughtfully addressed, including potential applications beyond music composition.",
            "The response follows the specified format and word count range, balancing technical depth with clarity of explanation throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
