class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_phenomenon": "Confirmation bias",
                "quantum_concept": "Superposition"
            },
            "2": {
                "cognitive_phenomenon": "Decision-making under uncertainty",
                "quantum_concept": "Entanglement"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired model of human decision-making, then apply it to the cognitive phenomenon of {t['cognitive_phenomenon']}, focusing on the quantum concept of {t['quantum_concept']}. Your response should include:

1. Quantum Cognition Framework (250-300 words):
   a) Explain the basic principles of quantum cognition and how they differ from classical cognitive models.
   b) Describe how the quantum concept of {t['quantum_concept']} can be applied to cognitive processes.
   c) Discuss the potential advantages and limitations of using quantum-inspired models in cognitive science.

2. Model Design (300-350 words):
   a) Describe the architecture of your quantum-inspired cognitive model.
   b) Explain how your model incorporates the quantum concept of {t['quantum_concept']}.
   c) Detail the key components and mathematical formalism of your model.
   d) Provide a diagram or equation representing the core structure of your model.

3. Application to {t['cognitive_phenomenon']} (250-300 words):
   a) Explain how your model represents and processes information related to {t['cognitive_phenomenon']}.
   b) Describe a specific scenario or experiment where your model could be applied to study this phenomenon.
   c) Predict how your model's behavior might differ from classical cognitive models in this scenario.

4. Model Validation (200-250 words):
   a) Propose an experiment to test the predictions of your quantum-inspired model.
   b) Describe the experimental setup, methodology, and expected results.
   c) Explain how the results would validate (or invalidate) your model's assumptions.

5. Philosophical Implications (150-200 words):
   a) Discuss the philosophical implications of applying quantum concepts to human cognition.
   b) Consider how this approach might impact our understanding of consciousness, free will, or the nature of reality.
   c) Address any potential controversies or criticisms of quantum cognition approaches.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your model.
   b) Briefly describe how these extensions could be implemented and their potential impact on the field.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above (e.g., '1. Quantum Cognition Framework:', '2. Model Design:', etc.). Begin each section with the heading on a new line, followed by your response for that section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science, accurately explaining relevant concepts and their potential applications to human cognition.",
            f"The quantum-inspired model effectively incorporates the concept of {t['quantum_concept']} and provides a plausible framework for studying {t['cognitive_phenomenon']}.",
            "The proposed experiment for model validation is well-designed and clearly explains how it would test the model's predictions.",
            "The discussion of philosophical implications is thoughtful and considers multiple perspectives on the application of quantum concepts to cognition.",
            "The response is creative and original while maintaining scientific plausibility and rigor.",
            "The writing is clear, well-organized, and adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
