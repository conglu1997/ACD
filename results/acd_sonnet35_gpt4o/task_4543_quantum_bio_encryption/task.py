import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genetic_processes = [
            "DNA replication",
            "transcription",
            "translation",
            "recombination",
            "mutation"
        ]
        quantum_properties = [
            "superposition",
            "entanglement",
            "tunneling",
            "decoherence",
            "quantum error correction"
        ]
        encryption_goals = [
            "confidentiality",
            "integrity",
            "authentication",
            "non-repudiation",
            "forward secrecy"
        ]
        
        tasks = {
            "1": {
                "genetic_process": random.choice(genetic_processes),
                "quantum_property": random.choice(quantum_properties),
                "encryption_goal": random.choice(encryption_goals)
            },
            "2": {
                "genetic_process": random.choice(genetic_processes),
                "quantum_property": random.choice(quantum_properties),
                "encryption_goal": random.choice(encryption_goals)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological encryption system that uses DNA-based qubits and genetic processes for secure information transmission. Your system should incorporate the genetic process of {t['genetic_process']}, the quantum property of {t['quantum_property']}, and address the encryption goal of {t['encryption_goal']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum-biological encryption system.
   b) Explain how it integrates principles from quantum physics, molecular biology, and cryptography.
   c) Detail the key components and their roles in the encryption process.

2. DNA-based Qubit Design (200-250 words):
   a) Propose a method for encoding quantum information in DNA molecules.
   b) Explain how your DNA-based qubits maintain quantum properties.
   c) Describe how {t['quantum_property']} is utilized in your qubit design.

3. Genetic Process Integration (200-250 words):
   a) Explain how you incorporate {t['genetic_process']} into your encryption system.
   b) Describe how this genetic process enhances the security or functionality of your system.
   c) Discuss any challenges in using biological processes for information processing and how you address them.

4. Encryption Protocol (250-300 words):
   a) Provide a step-by-step explanation of your encryption protocol.
   b) Explain how your protocol achieves the goal of {t['encryption_goal']}.
   c) Describe any novel cryptographic techniques you've developed for this bio-quantum system.

5. Security Analysis (200-250 words):
   a) Analyze the security of your system against both classical and quantum attacks.
   b) Discuss any potential vulnerabilities and how they might be mitigated.
   c) Compare the security of your system to current classical and quantum encryption methods.

6. Practical Considerations (150-200 words):
   a) Discuss the feasibility of implementing your system with current or near-future technology.
   b) Identify key technological hurdles that need to be overcome.
   c) Propose potential applications for your quantum-biological encryption system.

7. Ethical and Environmental Implications (100-150 words):
   a) Discuss any ethical concerns related to using biological components in encryption systems.
   b) Analyze the potential environmental impact of your system.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and cryptography. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, molecular biology, and cryptography.",
            f"The system effectively incorporates the genetic process of {t['genetic_process']} and the quantum property of {t['quantum_property']}.",
            f"The encryption protocol clearly addresses the goal of {t['encryption_goal']}.",
            "The response includes creative and scientifically plausible solutions to the challenges of quantum-biological encryption.",
            "The security analysis is thorough and compares the system to current encryption methods.",
            "The response addresses practical considerations, ethical implications, and potential applications of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
