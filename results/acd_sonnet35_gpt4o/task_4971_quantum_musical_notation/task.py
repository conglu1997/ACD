import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "superposition",
            "entanglement",
            "wave function collapse",
            "quantum tunneling"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        return {
            "1": {"quantum_property": random.choice(quantum_properties), "musical_element": random.choice(musical_elements)},
            "2": {"quantum_property": random.choice(quantum_properties), "musical_element": random.choice(musical_elements)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that represents quantum states using musical notation, focusing on the quantum property of {t['quantum_property']} and the musical element of {t['musical_element']}. Then, use this system to compose and analyze a quantum-inspired musical piece. Your response should include:

1. Quantum Musical Notation System (300-350 words):
   a) Describe your system for representing quantum states using musical notation.
   b) Explain how your system incorporates {t['quantum_property']} into {t['musical_element']}.
   c) Provide examples of how specific quantum states would be notated in your system.
   d) Discuss any novel features or advantages of your notation system.
   e) Include a detailed textual description of a visual representation or diagram of your notation system.

2. Composition Process (250-300 words):
   a) Outline the steps for composing a quantum-inspired piece using your notation system.
   b) Explain how quantum principles guide or influence the composition process.
   c) Describe any challenges in translating quantum concepts into musical form.
   d) Provide a concrete example of a short composition (4-8 measures) using your system, describing it in detail.

3. Musical Analysis (200-250 words):
   a) Analyze the short composition you provided in the previous section.
   b) Explain how the piece reflects both quantum behavior and musical structure.
   c) Discuss any emergent patterns or properties in the composition.

4. Quantum-Musical Correlation (200-250 words):
   a) Explore how your system might be used to represent or study actual quantum systems.
   b) Discuss any insights about quantum behavior that might be gained through this musical representation.
   c) Propose an experiment that could test the validity or usefulness of your quantum musical notation system.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss potential applications of your system in quantum computing, music education, or data sonification.
   b) Explore how this integration of quantum mechanics and music might influence creative or scientific processes.

6. Ethical and Philosophical Considerations (100-150 words):
   a) Discuss any ethical implications of representing quantum states through music.
   b) Explore philosophical questions raised by the intersection of quantum mechanics and musical composition.

Ensure your response demonstrates a deep understanding of both quantum mechanics and music theory. Use appropriate terminology from both fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and musical integrity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a quantum musical notation system, focusing on {t['quantum_property']} and {t['musical_element']}, with a clear textual description of a visual representation.",
            "The composition process is clearly explained with a concrete example of a short composition using the designed system.",
            "The musical analysis demonstrates a deep understanding of both quantum behavior and musical structure, applied to the provided composition example.",
            "The response explores potential applications and implications of the quantum musical notation system, including a proposed experiment to test its validity or usefulness.",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving, with appropriate use of terminology from both quantum mechanics and music theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
