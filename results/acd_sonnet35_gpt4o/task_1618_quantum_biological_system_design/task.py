import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "magnetoreception"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biological system that leverages the quantum effect of {t['quantum_effect']} to enhance the biological process of {t['biological_process']}. Your response should include:

1. System Overview (200-250 words):
   a) Provide a brief explanation of the chosen quantum effect and biological process.
   b) Describe your proposed quantum biological system and its key components.
   c) Explain how the quantum effect enhances or modifies the biological process.

2. Quantum-Biological Interface (250-300 words):
   a) Detail the mechanism by which the quantum effect interacts with the biological components.
   b) Explain how quantum coherence is maintained in a typically noisy biological environment.
   c) Describe any novel biomolecular structures or processes that enable this quantum-biological interface.

3. System Dynamics and Function (200-250 words):
   a) Explain how your system operates on both the quantum and macroscopic biological levels.
   b) Provide a step-by-step description of the enhanced biological process.
   c) Discuss how the quantum effect provides an advantage over classical biological processes.

4. Theoretical Framework (150-200 words):
   a) Present the key equations or principles that govern your quantum biological system.
   b) Explain how these equations integrate quantum and biological concepts.

5. Experimental Detection (150-200 words):
   a) Propose an experimental setup to detect and measure the quantum effect in your biological system.
   b) Discuss potential challenges in experimentally verifying quantum effects in biological systems.

6. Implications and Applications (150-200 words):
   a) Discuss the broader implications of your system for our understanding of quantum biology.
   b) Propose two potential applications of your quantum biological system in medicine or biotechnology.

7. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or criticisms of your proposed system.
   b) Suggest future research directions to address these limitations or expand on your idea.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum effect and biological process.",
            "The proposed quantum biological system is creative, well-defined, and scientifically plausible.",
            "The explanation of the quantum-biological interface is detailed and addresses the challenge of maintaining quantum coherence in biological systems.",
            "The system dynamics and function are clearly explained, showing how the quantum effect enhances the biological process.",
            "The theoretical framework integrates quantum and biological concepts appropriately.",
            "The proposed experimental detection method is reasonable and addresses potential challenges.",
            "The discussion of implications, applications, limitations, and future directions shows critical thinking and insight.",
            "The overall response is coherent, well-structured, and demonstrates strong interdisciplinary reasoning in quantum biology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
