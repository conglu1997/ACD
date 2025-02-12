import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions_concepts = [
            {"name": "Serenity", "description": "A state of calm peacefulness and absence of worry"},
            {"name": "Entropy", "description": "The gradual decline into disorder within a system"},
            {"name": "Emergence", "description": "The process of complex patterns arising from simple interactions"},
            {"name": "Nostalgia", "description": "A sentimental longing for a period in the past"},
            {"name": "Quantum Superposition", "description": "The principle of being in multiple states simultaneously"},
            {"name": "Fractal Infinity", "description": "The concept of self-similarity at different scales"}
        ]
        return {str(i+1): emotion for i, emotion in enumerate(random.sample(emotions_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for generating and evaluating abstract art, then use it to create a piece based on the emotion or concept: {t['name']} ({t['description']}). Your response should include the following sections:

1. Quantum-Inspired AI Art System Architecture (300-400 words):
   a) Describe the key components of your quantum-inspired AI art generation and evaluation system.
   b) Explain how quantum computing principles are incorporated into the system design.
   c) Detail the AI algorithms and techniques used for art generation and aesthetic evaluation.
   d) Provide a high-level diagram of your system architecture (describe it textually).

2. Quantum-Aesthetic Approach (250-350 words):
   a) Explain how quantum principles (e.g., superposition, entanglement) are used to represent and manipulate artistic elements.
   b) Describe how your approach translates quantum states or operations into visual artistic features.
   c) Discuss how quantum randomness or uncertainty is leveraged in the creative process.

3. Emotion-to-Art Translation (250-350 words):
   a) Explain how your system interprets and represents the given emotion or concept: {t['name']}.
   b) Describe the process of translating this emotion into quantum states or operations.
   c) Detail how these quantum representations are then transformed into visual art elements.
   d) Provide an example of a specific quantum operation used to represent an aspect of {t['name']}.

4. Art Generation Process (250-350 words):
   a) Describe the step-by-step process your system uses to generate an abstract art piece.
   b) Explain how quantum and classical computations are combined in this process.
   c) Discuss how the system ensures the final art piece reflects the given emotion or concept.
   d) Provide a textual description of the abstract art piece your system would generate for {t['name']}.

5. Aesthetic Evaluation Mechanism (200-300 words):
   a) Explain how your system evaluates the aesthetic quality of the generated art.
   b) Describe any quantum-inspired metrics or criteria used in this evaluation.
   c) Discuss how the system balances novelty, coherence, and emotional resonance in its evaluation.

6. Ethical and Philosophical Implications (150-250 words):
   a) Discuss the implications of using quantum-inspired AI for creative tasks traditionally done by humans.
   b) Explore how this technology might impact our understanding of creativity and consciousness.
   c) Address potential concerns about the authenticity or value of quantum-AI generated art.

7. Future Developments and Applications (150-250 words):
   a) Propose two potential enhancements or extensions to your quantum-inspired AI art system.
   b) Discuss how this technology could be applied to other forms of artistic expression or creative tasks.
   c) Suggest a research study to explore the reception of quantum-AI generated art by human audiences.

Ensure your response demonstrates a deep understanding of quantum computing principles, AI algorithms, and aesthetic theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-2250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, AI algorithms, and aesthetic theory.",
            f"The proposed system effectively addresses the generation of art based on the emotion or concept: {t['name']}.",
            "The quantum-inspired approach to art generation is well-explained and innovative.",
            "The process of translating emotions or concepts into quantum states and then into visual art is clearly described.",
            "A concrete example of a specific quantum operation used in the art generation process is provided.",
            "The aesthetic evaluation mechanism is sophisticated and well-explained.",
            "Ethical and philosophical implications are thoroughly addressed.",
            "The future developments and applications proposed are innovative and plausible.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
