import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conditions = [
            {
                "magnetic_field_strength": random.uniform(20, 60),  # microtesla
                "light_intensity": random.uniform(100, 2000),  # lux
                "temperature": random.uniform(0, 30),  # Celsius
            },
            {
                "magnetic_field_strength": random.uniform(20, 60),  # microtesla
                "light_intensity": random.uniform(100, 2000),  # lux
                "temperature": random.uniform(0, 30),  # Celsius
            }
        ]
        return {
            "1": conditions[0],
            "2": conditions[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the quantum-based magnetoreception system in migratory birds, focusing on the radical pair mechanism and its interaction with environmental factors. Your task has the following parts:

1. Quantum Magnetoreception Model (250-300 words):
   a) Describe the key components of your computational model for avian quantum magnetoreception, focusing on the radical pair mechanism.
   b) Explain how your model represents the interaction between cryptochrome proteins and magnetic fields.
   c) Provide a high-level diagram or flowchart of your model's architecture (describe it textually).

2. Environmental Influence Simulation (200-250 words):
   a) Detail how your model simulates the effects of environmental factors on the quantum magnetoreception system.
   b) Explain how you incorporate the given conditions: magnetic field strength ({t['magnetic_field_strength']:.2f} microtesla), light intensity ({t['light_intensity']:.2f} lux), and temperature ({t['temperature']:.2f} Celsius).
   c) Discuss any challenges in modeling these environmental influences and how you addressed them.

3. Navigation Behavior Prediction (200-250 words):
   a) Describe how your model predicts the bird's navigation behavior based on the simulated quantum magnetoreception.
   b) Provide a specific example of predicted navigation behavior under the given environmental conditions.
   c) Explain any assumptions or simplifications made in your behavioral predictions.

4. Model Validation and Future Research (150-200 words):
   a) Propose a method to validate your model against real-world data on bird migration patterns.
   b) Suggest one potential expansion or application of your quantum avian navigation model.
   c) Discuss how this research might contribute to our understanding of quantum biology.

Ensure your response demonstrates an understanding of quantum mechanics and its application in biological systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 800-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates understanding of the radical pair mechanism in quantum magnetoreception.",
            "The model incorporates the given environmental conditions and their effects on the quantum system.",
            "The navigation behavior prediction is based on the quantum magnetoreception model and considers the specific environmental conditions.",
            "The response includes a plausible validation method and future research direction.",
            "The response meets the required word count and follows the specified format."
        ]
        word_count = len(submission.split())
        if word_count < 800 or word_count > 1000:
            return 0.0
        score = sum([0.2 for criterion in criteria if eval_with_llm_judge(instructions, submission, [criterion])])
        return round(score, 2)
