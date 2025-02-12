import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['Quantum superposition', 'Quantum entanglement', 'Quantum tunneling']
        dna_processes = ['DNA replication', 'Transcription', 'Translation']
        error_types = ['Substitution errors', 'Insertion/deletion errors', 'Strand breaks']
        
        tasks = [
            {
                "quantum_concept": random.choice(quantum_concepts),
                "dna_process": random.choice(dna_processes),
                "error_type": random.choice(error_types)
            },
            {
                "quantum_concept": random.choice(quantum_concepts),
                "dna_process": random.choice(dna_processes),
                "error_type": random.choice(error_types)
            }
        ]
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired error correction system for DNA-based data storage, incorporating principles from quantum computing, molecular biology, and information theory. Your system should focus on the following parameters:

1. Quantum concept to incorporate: {t['quantum_concept']}
2. DNA process to model: {t['dna_process']}
3. Error type to address: {t['error_type']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired DNA error correction system.
   b) Explain how you incorporate the specified quantum concept into your model.
   c) Detail how your system interfaces with the DNA-based data storage.
   d) Include a high-level diagram or pseudocode to illustrate your system's structure.

2. Error Detection and Correction Mechanism (250-300 words):
   a) Explain how your system detects and corrects the specified error type in DNA-based data storage.
   b) Describe the role of the quantum concept in error correction.
   c) Discuss how your model accounts for the given DNA process in its error correction strategy.

3. Quantum-Biological Interface (200-250 words):
   a) Explain how you map quantum states or operations to biological processes in DNA.
   b) Describe how the specified quantum concept enhances error correction in DNA-based storage.
   c) Discuss any novel insights this quantum-biological approach might offer to information theory or molecular biology.

4. Performance Analysis (200-250 words):
   a) Provide a theoretical analysis of your system's error correction capabilities.
   b) Compare your approach to classical error correction methods for DNA-based storage.
   c) Discuss potential advantages and limitations of your quantum-inspired approach.

5. Implementation Challenges and Solutions (150-200 words):
   a) Identify key challenges in implementing your proposed system.
   b) Suggest potential solutions or research directions to address these challenges.
   c) Discuss any ethical considerations related to manipulating DNA for data storage.

6. Future Implications (150-200 words):
   a) Explore potential applications of your quantum-inspired DNA error correction system beyond data storage.
   b) Discuss how this technology might impact fields such as bioinformatics, quantum biology, and biocomputing.
   c) Speculate on future developments that could arise from the integration of quantum computing and molecular biology.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['quantum_concept']}, {t['dna_process']}, and {t['error_type']}.",
            "The proposed system should be innovative and scientifically plausible.",
            "The error correction mechanism should coherently integrate quantum and biological principles.",
            "The performance analysis should be logical and offer novel insights.",
            "The implementation challenges and solutions should be realistic and well-reasoned.",
            "The future implications should demonstrate critical thinking about the potential impact of the technology.",
            "The overall response should be well-structured, clear, and demonstrate strong interdisciplinary reasoning and creativity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
