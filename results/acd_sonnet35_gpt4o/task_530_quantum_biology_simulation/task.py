import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_biology_phenomena = [
            {
                "name": "Photosynthesis",
                "description": "The process by which plants convert light energy into chemical energy"
            },
            {
                "name": "Avian magnetoreception",
                "description": "The ability of birds to detect Earth's magnetic field for navigation"
            }
        ]
        return {
            "1": random.choice(quantum_biology_phenomena),
            "2": random.choice(quantum_biology_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates quantum effects in {t['name']}, a biological phenomenon described as {t['description']}. Your task has the following parts:

1. Quantum Biology Background (150-200 words):
   Explain the current understanding of quantum effects in {t['name']}. Discuss the key quantum mechanical principles involved and how they interact with biological processes.

2. Computational Model Design (250-300 words):
   a) Describe the architecture of your computational model, including its main components and how they interact.
   b) Explain how your model incorporates both quantum mechanical principles and biological processes.
   c) Detail how your model simulates the specific quantum effects observed in {t['name']}.
   d) Discuss any novel or unique features of your model that address challenges in simulating quantum biological systems.

3. Simulation Algorithm (150-200 words):
   Propose a specific algorithm or approach that your model would use to simulate the quantum effects in {t['name']}. Explain how this algorithm balances quantum mechanical accuracy with biological complexity.

4. Model Evaluation (150-200 words):
   a) Describe how you would evaluate the performance and accuracy of your model.
   b) Propose specific metrics or benchmarks that could be used to compare your model's simulations to experimental observations of {t['name']}.
   c) Discuss potential limitations of your evaluation method and the model itself.

5. Predictions and Implications (200-250 words):
   a) Describe two specific, testable predictions that your model makes about quantum effects in {t['name']}.
   b) Discuss how these predictions might be tested in real-world experiments.
   c) Explain how your model and its predictions might inform our understanding of quantum biology and its potential applications.

6. Philosophical and Ethical Considerations (100-150 words):
   Discuss the philosophical implications of quantum effects in biological systems. Consider questions such as reductionism vs. emergentism, free will, and the nature of consciousness. Address any ethical considerations related to this research.

7. Future Directions (100-150 words):
   Propose two ways your model could be extended or improved in future research. Consider both technological advancements and potential new discoveries in quantum biology.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computational modeling. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Quantum Biology Background:') on a new line, followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of quantum mechanics and its potential role in biological systems, specifically in relation to the given phenomenon.",
            "The computational model design is innovative, detailed, and scientifically plausible, incorporating both quantum and biological principles.",
            "The simulation algorithm is well-explained and appropriate for the complexity of the quantum biological system being modeled.",
            "The model evaluation section provides a logical framework for assessing the accuracy and limitations of the simulation.",
            "The predictions and implications are specific, testable, and relevant to advancing our understanding of quantum biology.",
            "Philosophical and ethical considerations are thoughtfully addressed, demonstrating an understanding of the broader implications of this research.",
            "The future directions proposed are innovative and grounded in current scientific understanding.",
            "The response shows strong interdisciplinary reasoning, combining insights from quantum physics, biology, and computational science.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
