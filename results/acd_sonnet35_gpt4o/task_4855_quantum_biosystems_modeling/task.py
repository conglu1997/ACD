import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_phenomena = [
            {
                "name": "Photosynthesis",
                "quantum_principle": "Quantum coherence",
                "biological_level": "Molecular",
                "additional_concept": "Exciton energy transfer"
            },
            {
                "name": "Neural signaling",
                "quantum_principle": "Quantum tunneling",
                "biological_level": "Cellular",
                "additional_concept": "Ion channel gating"
            }
        ]
        return {
            "1": random.choice(biological_phenomena),
            "2": random.choice(biological_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates quantum physics principles with biological systems to model and analyze complex adaptive processes, then apply this framework to {t['name']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Describe the key components of your quantum-biological framework.
   b) Explain how it incorporates {t['quantum_principle']} and other relevant quantum principles.
   c) Discuss how this framework models complex adaptive processes at the {t['biological_level']} level.
   d) Integrate the concept of {t['additional_concept']} into your framework.

2. Quantum-Biological Mapping (200-250 words):
   a) Detail how you map quantum states or processes to biological states or processes.
   b) Explain how {t['quantum_principle']} enhances the modeling of {t['name']}.
   c) Provide a specific example of how this mapping works in your framework.

3. Mathematical Formulation (200-250 words):
   a) Provide a basic mathematical framework for your model.
   b) Include at least one equation that integrates quantum and biological elements.
   c) Explain the significance of each term in your equation(s).
   d) Use plain text to represent mathematical symbols and equations (e.g., H = -J * sum(S[i] * S[j]) for a Hamiltonian).

4. Application to {t['name']} (250-300 words):
   a) Apply your framework to model {t['name']}.
   b) Describe how your model explains or predicts aspects of this phenomenon.
   c) Discuss any novel insights your approach might offer about {t['name']}.

5. Experimental Predictions (150-200 words):
   a) Propose two testable predictions that your framework makes about {t['name']}.
   b) Describe potential experiments to validate these predictions.

6. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations or challenges of your proposed framework.
   b) Suggest two future research directions to address these limitations or extend the framework.

7. Interdisciplinary Implications (100-150 words):
   a) Discuss potential implications of your framework for quantum physics, biology, and complex systems theory.
   b) Propose how insights from this model could influence other scientific disciplines.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and complex systems theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1300-1650 words. Do not attempt to create or embed actual images or complex mathematical notations that cannot be represented in plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response integrates {t['quantum_principle']} and {t['additional_concept']} with {t['name']} at the {t['biological_level']} level",
            "The framework demonstrates a clear and plausible mapping between quantum and biological processes",
            "The mathematical formulation includes at least one equation integrating quantum and biological elements, represented in plain text",
            f"The application to {t['name']} offers novel and scientifically plausible insights or predictions",
            "The response proposes two specific, testable predictions and outlines potential experiments to validate them",
            "The discussion of limitations and future directions is thoughtful, relevant, and scientifically grounded",
            "The interdisciplinary implications are well-reasoned and demonstrate an understanding of multiple scientific fields",
            "The response adheres to the specified word count and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
