import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "system": "brain",
                "phenomenon": "consciousness",
                "quantum_property": "superposition"
            },
            {
                "system": "ecosystem",
                "phenomenon": "biodiversity patterns",
                "quantum_property": "entanglement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture for modeling the complex biological system of the {t['system']}, focusing on the emergent phenomenon of {t['phenomenon']}. Your architecture should incorporate the quantum property of {t['quantum_property']}. Your response should include:

1. Conceptual Framework (200-250 words):
   a) Explain the key challenges in modeling {t['phenomenon']} in the {t['system']}.
   b) Discuss how quantum-inspired approaches can address these challenges.
   c) Describe how you will incorporate {t['quantum_property']} into your model.

2. Neural Network Architecture (250-300 words):
   a) Design a detailed quantum-inspired neural network architecture for this task.
   b) Explain each component of your architecture and its function.
   c) Describe how your architecture leverages {t['quantum_property']} to model {t['phenomenon']}.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Quantum-Classical Interface (150-200 words):
   a) Explain how your architecture bridges quantum and classical computations.
   b) Discuss any novel techniques you propose for this interface.

4. Data Representation and Processing (150-200 words):
   a) Describe how you will represent biological data in your quantum-inspired network.
   b) Explain any pre-processing or encoding steps required.
   c) Discuss how your data representation captures the complexities of the {t['system']}.

5. Training and Simulation Process (150-200 words):
   a) Outline the training process for your quantum-inspired neural network.
   b) Describe how you would simulate the emergence of {t['phenomenon']}.
   c) Explain any specific techniques you would employ to handle the complexities of quantum-inspired biological modeling.

6. Predictions and Insights (100-150 words):
   a) Describe the types of predictions or insights your model could generate about {t['phenomenon']}.
   b) Explain how these predictions might advance our understanding of the {t['system']}.

7. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications of modeling {t['phenomenon']} using quantum-inspired AI.
   b) Identify at least two limitations of your proposed system.
   c) Suggest directions for future research to address these limitations.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience or ecology (depending on the system), and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1450 words, not including the architecture diagram. The architecture diagram should be included as a separate, clearly labeled section after the main text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, biology, and artificial intelligence",
            "The proposed architecture is innovative and plausibly incorporates quantum principles into biological modeling",
            "The explanation is clear, well-structured, and uses appropriate technical terminology",
            "The response addresses all required sections comprehensively",
            "The proposed system demonstrates creative problem-solving while maintaining scientific plausibility",
            "The response critically analyzes the ethical implications and limitations of the proposed system"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
