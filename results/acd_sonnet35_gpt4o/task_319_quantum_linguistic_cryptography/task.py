import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "linguistic_structure": "syntactic tree",
                "quantum_principle": "entanglement",
                "message_type": "diplomatic communication"
            },
            "2": {
                "linguistic_structure": "phonological rules",
                "quantum_principle": "superposition",
                "message_type": "scientific data"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum encryption system based on linguistic structures, specifically using {t['linguistic_structure']} and the quantum principle of {t['quantum_principle']}. Then, use your system to encode a {t['message_type']}. Your task has the following components:

1. Quantum-Linguistic Encryption System Design (250-300 words):
   a) Explain how you integrate {t['linguistic_structure']} with {t['quantum_principle']} to create an encryption system.
   b) Describe the quantum states or operations used to represent linguistic elements.
   c) Explain how encryption and decryption would work in your system.
   d) Discuss how your system ensures security and resists potential quantum attacks.

2. Encoding Process (200-250 words):
   a) Provide a step-by-step explanation of how you would encode a {t['message_type']} using your system.
   b) Include a simple example, showing how a short phrase or sentence would be encrypted.
   c) Explain how the linguistic structure influences the encoding process.

3. Quantum Circuit Description (150-200 words):
   a) Describe the quantum circuit or algorithm that would implement your encryption system.
   b) Explain the types and sequence of quantum gates used.
   c) Discuss how many qubits would be required and why.

4. Advantages and Limitations (150-200 words):
   a) Analyze the potential advantages of your system over classical encryption methods.
   b) Discuss any limitations or challenges in implementing your system.
   c) Suggest potential improvements or areas for further research.

5. Interdisciplinary Implications (100-150 words):
   Discuss how your quantum-linguistic encryption system might impact or advance the fields of linguistics, quantum computing, and cryptography.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and cryptography. Be creative in your approach while maintaining scientific and theoretical plausibility. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response integrates {t['linguistic_structure']} with {t['quantum_principle']} in a plausible encryption system",
            "The encryption and decryption process is clearly explained",
            f"A step-by-step encoding process for a {t['message_type']} is provided with a simple example",
            "The quantum circuit or algorithm is described with appropriate quantum gates and qubit requirements",
            "Advantages and limitations of the system are analyzed",
            "Interdisciplinary implications are discussed",
            "The response demonstrates deep understanding of quantum mechanics, linguistics, and cryptography",
            "The proposed system is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
