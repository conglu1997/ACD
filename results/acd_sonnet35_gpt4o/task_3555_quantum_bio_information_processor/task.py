import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        biological_structures = [
            "DNA",
            "Proteins",
            "Cell membranes"
        ]
        information_processes = [
            "Encoding",
            "Storage",
            "Retrieval"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "information_process": random.choice(information_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "information_process": random.choice(information_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-biological hybrid system for information processing and storage, integrating principles from quantum computing, molecular biology, and information theory. Your system should focus on the quantum principle of {t['quantum_principle']}, the biological structure {t['biological_structure']}, and the information process of {t['information_process']}.

Provide your response in the following format:

1. System Overview (250-300 words):
   a) Describe the key components and architecture of your quantum-biological hybrid system.
   b) Explain how {t['quantum_principle']} is utilized in your system's design.
   c) Discuss how {t['biological_structure']} is integrated into the information processing mechanism.
   d) Elaborate on how your system implements the {t['information_process']} process.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system interfaces quantum and biological components.
   b) Describe the process of translating quantum information into biological structures and vice versa.
   c) Discuss any novel mechanisms or principles employed in this interface.

3. Information Processing Mechanism (200-250 words):
   a) Detail the step-by-step process of how information is processed in your hybrid system.
   b) Explain how the quantum and biological components work together to achieve the specified information process.
   c) Describe any error correction or noise reduction mechanisms in your system.

4. Theoretical Performance Analysis (150-200 words):
   a) Analyze the theoretical performance of your system compared to classical computing systems.
   b) Discuss any potential advantages or limitations of your quantum-biological approach.
   c) Propose metrics for evaluating the efficiency and effectiveness of your system.

5. Challenges and Future Directions (150-200 words):
   a) Identify at least two major challenges in implementing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss the potential impact of overcoming these challenges on the field of computing and biology.

6. Ethical Implications and Applications (150-200 words):
   a) Discuss the ethical implications of developing quantum-biological hybrid systems.
   b) Propose three potential applications of your system in scientific research or technology.
   c) Speculate on how this technology might influence our understanding of life and computation.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific quantum principle: {t['quantum_principle']}",
            f"The system integrates the biological structure: {t['biological_structure']}",
            f"The system implements the information process: {t['information_process']}",
            "The response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory",
            "The proposed system is innovative while maintaining scientific plausibility",
            "The response includes all required sections with appropriate detail and word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
