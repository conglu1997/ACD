import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "dna_property": "base pairing",
                "storage_goal": "maximize data density"
            },
            {
                "quantum_principle": "entanglement",
                "dna_property": "strand displacement",
                "storage_goal": "enhance retrieval speed"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system for DNA data storage that incorporates the quantum principle of {t['quantum_principle']} and leverages the DNA property of {t['dna_property']} to {t['storage_goal']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain how the chosen quantum principle can be applied to DNA data storage.
   b) Describe how the selected DNA property can be utilized in this context.
   c) Discuss the potential advantages of this approach for the specified storage goal.

2. System Architecture (300-350 words):
   a) Outline the key components of your quantum-enhanced DNA data storage system.
   b) Explain how each component incorporates aspects of quantum mechanics and molecular biology.
   c) Describe the data encoding, storage, and retrieval processes in your system.
   d) Include a diagram or flowchart of your system architecture using ASCII art or Unicode characters.

3. Quantum-Biological Interface (200-250 words):
   a) Propose a theoretical mechanism for interfacing quantum systems with DNA molecules.
   b) Explain how this interface maintains quantum coherence while interacting with biological structures.
   c) Discuss potential challenges and your approaches to overcome them.

4. Information Theoretic Analysis (200-250 words):
   a) Analyze the theoretical information capacity of your system.
   b) Compare it to classical DNA data storage and traditional digital storage methods.
   c) Discuss any trade-offs between storage density, accuracy, and retrieval efficiency.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test a key aspect of your quantum DNA data storage system.
   b) Describe the experimental setup, including any specialized equipment or techniques required.
   c) Explain how you would measure and analyze the results.

6. Potential Applications and Implications (150-200 words):
   a) Discuss potential applications of your quantum DNA data storage system.
   b) Explore the implications of this technology for fields such as cryptography, biocomputing, and data archiving.
   c) Consider any ethical considerations or potential risks associated with this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how {t['quantum_principle']} can be applied to DNA data storage.",
            f"The system design clearly explains how it leverages the DNA property of {t['dna_property']} to {t['storage_goal']}.",
            "The quantum-biological interface is well-explained and scientifically plausible.",
            "The information theoretic analysis is thorough and compares the proposed system to existing methods.",
            "The experimental design is well-thought-out and appropriate for testing the proposed system.",
            "The response demonstrates creativity and innovation while maintaining scientific accuracy.",
            "The potential applications and implications are thoughtfully discussed, including ethical considerations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
