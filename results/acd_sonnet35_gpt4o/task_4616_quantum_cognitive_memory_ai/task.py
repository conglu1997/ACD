import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "memory_process": "episodic memory formation",
                "quantum_principle": "superposition"
            },
            "2": {
                "memory_process": "working memory capacity",
                "quantum_principle": "entanglement"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for modeling and enhancing the human memory process of {t['memory_process']}, focusing on the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum-Cognitive Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how your system models the specified memory process.
   c) Detail how you incorporate the given quantum principle into your design.
   d) Discuss any novel approaches in your architecture for bridging quantum computing and cognitive processes.

2. Quantum-Neural Interface (200-250 words):
   a) Explain how your system interfaces between quantum states and neural representations.
   b) Describe any quantum algorithms or techniques you would use to process cognitive information.
   c) Discuss how this quantum approach enhances the modeling or augmentation of the specified memory process.

3. Memory Enhancement Mechanisms (200-250 words):
   a) Detail the specific mechanisms your system uses to enhance the given memory process.
   b) Explain how these mechanisms leverage quantum principles to improve cognitive function.
   c) Provide an example of how your system might enhance memory in a practical scenario.

4. Cognitive Modeling and Simulation (150-200 words):
   a) Describe how your system models and simulates the specified memory process.
   b) Explain how you validate your model against known cognitive neuroscience findings.
   c) Discuss any predictions your model makes about memory function that could be experimentally tested.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in using quantum-inspired AI for cognitive enhancement.
   b) Discuss any limitations of your approach and areas where our understanding of quantum cognition is still limited.
   c) Propose guidelines for responsible development and use of quantum cognitive AI systems.

6. Future Implications and Research Directions (150-200 words):
   a) Speculate on how your system might impact our understanding of human cognition and quantum biology.
   b) Propose two specific research directions to further explore the intersection of quantum computing and cognitive neuroscience.
   c) Discuss potential applications of your system beyond memory enhancement.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and cognitive neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, and cognitive neuroscience.",
            f"The design effectively incorporates the quantum principle of {t['quantum_principle']} in modeling and enhancing {t['memory_process']}.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The ethical considerations and limitations are thoughtfully discussed.",
            "The future implications and research directions are insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
