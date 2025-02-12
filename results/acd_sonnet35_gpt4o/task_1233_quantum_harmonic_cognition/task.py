import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                "process": "decision making",
                "musical_element": "harmony",
                "quantum_concept": "superposition"
            },
            {
                "process": "memory formation",
                "musical_element": "rhythm",
                "quantum_concept": "entanglement"
            },
            {
                "process": "attention",
                "musical_element": "melody",
                "quantum_concept": "interference"
            },
            {
                "process": "emotion regulation",
                "musical_element": "timbre",
                "quantum_concept": "tunneling"
            }
        ]
        return {
            "1": random.choice(cognitive_processes),
            "2": random.choice(cognitive_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that translates the cognitive process of {t['process']} into musical compositions, focusing on the musical element of {t['musical_element']} and utilizing the quantum concept of {t['quantum_concept']}. Then, analyze its potential applications in neuroscience and artistic expression. This task requires integration of concepts from quantum computing, cognitive science, and music theory.

Your response should include:

1. Quantum System Design (250-300 words):
   a) Describe the key components and mechanisms of your quantum computing system.
   b) Explain how it incorporates the specified quantum concept ({t['quantum_concept']}).
   c) Detail how the system translates {t['process']} into {t['musical_element']}.
   d) Include at least one innovative feature that distinguishes your system from classical computing approaches.

2. Cognitive-Musical Mapping (200-250 words):
   a) Explain the theoretical basis for mapping {t['process']} to {t['musical_element']}.
   b) Describe how your system represents and processes cognitive data.
   c) Provide a specific example of how an aspect of {t['process']} would be translated into a musical feature. Include a simple diagram or notation to illustrate this example.

3. Quantum Advantage Analysis (200-250 words):
   a) Discuss how quantum properties enhance the system's ability to model cognitive processes or generate music.
   b) Identify potential limitations or challenges in implementing this quantum approach.
   c) Compare the expected performance of your system to classical algorithms for similar tasks.

4. Neuroscientific Applications (200-250 words):
   a) Propose two potential applications of your system in neuroscience research.
   b) Explain how these applications could advance our understanding of {t['process']}.
   c) Discuss any ethical considerations related to using this technology in brain research.

5. Artistic and Cultural Implications (150-200 words):
   a) Explore how this quantum-cognitive-musical system might influence artistic expression and creativity.
   b) Discuss potential impacts on music composition, performance, and appreciation.
   c) Consider how this technology might bridge the gap between science and art.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and music theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Provide specific examples and concrete details where possible to illustrate your points.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1000-1250 words. Include any diagrams or notations as text-based representations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and creative design for a quantum computing system that effectively translates {t['process']} into {t['musical_element']} using {t['quantum_concept']}, with clear explanations of key components and mechanisms.",
            f"The cognitive-musical mapping is well-explained and theoretically sound, with a specific, concrete example and illustration provided for translating an aspect of {t['process']} into a musical feature.",
            f"The quantum advantage analysis demonstrates a clear understanding of how {t['quantum_concept']} enhances the system's capabilities, including a substantive comparison with classical approaches and a discussion of potential limitations.",
            f"The proposed neuroscientific applications are innovative, well-reasoned, and directly related to advancing understanding of {t['process']}, with thoughtful consideration of ethical implications.",
            "The discussion of artistic and cultural implications shows depth of thought and creativity, considering specific impacts on multiple aspects of music creation, performance, and appreciation.",
            "The overall response demonstrates a strong grasp and integration of quantum computing, cognitive science, and music theory, with appropriate use of technical terminology from all three fields and clear connections drawn between them.",
            "The response adheres to the specified format and word count requirements, and provides specific examples and concrete details throughout to support the proposed ideas and designs."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
