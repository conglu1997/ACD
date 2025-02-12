import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_principles = [
            {
                "principle": "Fibonacci sequence",
                "description": "A sequence where each number is the sum of the two preceding ones"
            },
            {
                "principle": "Golden ratio",
                "description": "A special number approximately equal to 1.618, often found in nature and art"
            },
            {
                "principle": "Fractals",
                "description": "Self-similar patterns that repeat at different scales"
            }
        ]
        musical_elements = ["melody", "harmony", "rhythm", "form"]
        musical_genres = ["classical", "jazz", "electronic", "folk"]
        return {
            "1": {
                "math_principle": random.choice(mathematical_principles),
                "musical_element": random.choice(musical_elements),
                "genre": random.choice(musical_genres)
            },
            "2": {
                "math_principle": random.choice(mathematical_principles),
                "musical_element": random.choice(musical_elements),
                "genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithmic music composition system that applies the mathematical principle of {t['math_principle']['principle']} ({t['math_principle']['description']}) to the musical element of {t['musical_element']} within the {t['genre']} genre. Then, implement this system using AI techniques.

An algorithmic music composition system is a set of rules or procedures that generate musical content based on predefined parameters and algorithms, often with minimal human intervention during the composition process.

Your response should include the following sections, with a total word count not exceeding 1000 words:

1. System Design (250-300 words):
   - Explain how you will apply the {t['math_principle']['principle']} to generate or manipulate {t['musical_element']} in {t['genre']} music.
   - Describe the key components of your system and how they interact.
   - Discuss how your system ensures musical coherence and aesthetic quality within the {t['genre']} style.

2. Mathematical Implementation (200-250 words):
   - Provide a detailed explanation of how you translate the {t['math_principle']['principle']} into musical parameters specific to {t['genre']}.
   - Include at least one mathematical formula or algorithm that your system uses.
   - Explain how this mathematical approach enhances or challenges traditional {t['musical_element']} composition in {t['genre']}.

3. AI Integration (200-250 words):
   - Describe how you would implement your system using AI techniques (e.g., machine learning, neural networks, evolutionary algorithms).
   - Explain the role of AI in enhancing the creativity or efficiency of your system within the context of {t['genre']}.
   - Discuss any challenges in combining mathematical principles with AI for {t['genre']} music composition.

4. Sample Composition Process (150-200 words):
   - Walk through the process of how your system would compose a short {t['genre']} musical piece.
   - Highlight how the {t['math_principle']['principle']} and AI work together in this process.

5. Evaluation and Future Directions (150-200 words):
   - Propose criteria for evaluating the musical output of your system within the context of {t['genre']}.
   - Discuss potential limitations of your approach in composing {t['genre']} music.
   - Suggest one way to expand or improve your system in future iterations.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and artificial intelligence, particularly as they apply to {t['genre']} music. Be creative in your design while maintaining scientific and musical plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design clearly applies {t['math_principle']['principle']} to {t['musical_element']} in {t['genre']} music",
            "The mathematical implementation includes at least one formula or algorithm specific to the genre",
            "The AI integration explains how AI techniques are used in the system for the given genre",
            f"The sample composition process demonstrates how the {t['math_principle']['principle']} and AI work together in {t['genre']} music",
            f"Evaluation criteria and future directions are proposed specifically for {t['genre']} music",
            "The response shows a deep understanding of music theory, mathematics, and AI as applied to the given genre",
            "The design is creative while maintaining scientific and musical plausibility within the genre",
            "The response adheres to the specified word limit of 1000 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
