import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "superposition",
                "musical_element": "harmony",
                "composition_style": "classical"
            },
            {
                "quantum_concept": "entanglement",
                "musical_element": "rhythm",
                "composition_style": "jazz"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm for music composition that utilizes the quantum concept of {t['quantum_concept']} to generate {t['musical_element']} in the style of {t['composition_style']} music. Then, analyze its potential applications in both quantum computing and musicology. Your response should include the following sections:

1. Quantum Music Algorithm Design (300-350 words):
   a) Explain how your algorithm incorporates {t['quantum_concept']} to generate {t['musical_element']}.
   b) Describe the quantum circuit or system used in your algorithm.
   c) Explain how classical music theory principles of {t['composition_style']} style are integrated into the quantum system.
   d) Include a high-level pseudocode or diagram illustrating the key steps of your algorithm.

2. Technical Implementation (250-300 words):
   a) Discuss the quantum gates and operations used in your algorithm.
   b) Explain how quantum measurement is performed and interpreted in the context of music generation.
   c) Address any technical challenges in implementing this algorithm on current or near-term quantum hardware.

3. Music Theory Analysis (200-250 words):
   a) Analyze how your quantum approach to generating {t['musical_element']} compares to traditional {t['composition_style']} composition techniques.
   b) Discuss any unique musical structures or patterns that might emerge from this quantum-classical hybrid approach.
   c) Propose a method for evaluating the musical quality and adherence to {t['composition_style']} style of the quantum-generated compositions.

4. Quantum Computing Applications (200-250 words):
   a) Discuss how this algorithm contributes to the field of quantum computing and algorithm design.
   b) Propose two other potential applications of your approach in quantum computing outside of music composition.
   c) Analyze any quantum advantages your algorithm might offer over classical approaches.

5. Musicological Implications (200-250 words):
   a) Discuss how this quantum approach to music composition might influence music theory and analysis.
   b) Explore potential impacts on music education and the creative process for composers.
   c) Analyze ethical considerations related to AI and quantum computing in artistic creation.

6. Future Research Directions (150-200 words):
   a) Propose two extensions or modifications to your algorithm for future research.
   b) Suggest an interdisciplinary research project combining quantum music composition with another scientific field.
   c) Discuss potential long-term implications of quantum algorithms in the arts and creative industries.

Ensure your response demonstrates a deep understanding of both quantum computing and music theory, particularly in relation to {t['quantum_concept']} and {t['composition_style']} music. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific and musical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, particularly {t['quantum_concept']}, and music theory, specifically related to {t['composition_style']} style and {t['musical_element']}.",
            "The quantum music algorithm design is innovative, scientifically plausible, and effectively integrates quantum computing principles with music composition techniques.",
            "The analysis of musicological implications and future research directions is thoughtful and explores novel interdisciplinary connections.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
