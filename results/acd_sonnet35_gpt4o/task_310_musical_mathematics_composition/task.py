import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            {
                "element": "pitch",
                "mathematical_operation": "modular arithmetic"
            },
            {
                "element": "rhythm",
                "mathematical_operation": "fractional ratios"
            }
        ]
        return {
            "1": random.choice(musical_elements),
            "2": random.choice(musical_elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical composition using {t['mathematical_operation']} applied to {t['element']}. Your task has the following parts:

1. Composition Design (250-300 words):
   a) Explain how you will apply {t['mathematical_operation']} to {t['element']} in your composition.
   b) Describe the overall structure of your composition (e.g., form, length, instrumentation).
   c) Provide a specific example of how a mathematical operation translates into a musical element in your piece.
   d) Discuss how your approach maintains musical coherence while adhering to mathematical rules.

2. Notation and Representation (150-200 words):
   a) Describe how you would notate or represent your composition.
   b) Explain any novel notation systems you've developed, if applicable.
   c) Provide a small excerpt (4-8 measures) of your composition in your chosen notation system.

3. Analysis (200-250 words):
   a) Analyze the mathematical properties of your composition (e.g., patterns, symmetries, ratios).
   b) Explain how these mathematical properties contribute to the musical qualities of the piece.
   c) Discuss any unexpected or interesting emergent properties in your composition.

4. Real-world Application (150-200 words):
   a) Propose an innovative real-world application for your mathematical-musical system.
   b) Explain how this application could benefit or advance a field outside of music (e.g., data analysis, architecture, education).
   c) Discuss any potential challenges in implementing your proposed application.

5. Reflection (100-150 words):
   a) Discuss one advantage and one limitation of using {t['mathematical_operation']} with {t['element']} in musical composition.
   b) Speculate on how this approach might influence or change traditional music theory or composition techniques.

Ensure your response demonstrates a deep understanding of both music theory and mathematical concepts. Be creative in your approach while maintaining musical and mathematical validity. Your total response should not exceed 1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of how {t['mathematical_operation']} is applied to {t['element']} in the composition.",
            "The composition design is well-structured and coherently combines mathematical and musical elements.",
            "The notation and representation section includes a clear description and a sample excerpt.",
            "The analysis demonstrates a deep understanding of both mathematical and musical properties of the composition.",
            "The proposed real-world application is innovative and well-explained.",
            "The reflection shows critical thinking about the advantages and limitations of the approach.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
