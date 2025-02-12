import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "language": "Pirahã",
                "feature": "absence of recursion",
                "quantum_principles": ["superposition", "entanglement", "quantum tunneling"]
            },
            {
                "language": "Rotokas",
                "feature": "extremely small phoneme inventory",
                "quantum_principles": ["quantum teleportation", "quantum superposition", "quantum interference"]
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system using the unique features of {t['language']} (specifically its {t['feature']}) and quantum computing principles. Your response should include the following sections:

1. Linguistic Analysis (200-250 words):
   a) Explain the key features of {t['language']}, focusing on its {t['feature']}.
   b) Discuss how these features could be leveraged for encryption purposes.
   c) Analyze potential challenges in using this language for encryption.

2. Quantum Principles Integration (250-300 words):
   a) Describe how you will incorporate the following quantum principles into your encryption system: {', '.join(t['quantum_principles'])}.
   b) Explain how these principles complement the linguistic features of {t['language']}.
   c) Discuss any novel quantum-linguistic interactions in your system.

3. Encryption System Design (300-350 words):
   a) Detail the architecture of your quantum-linguistic encryption system.
   b) Explain the encryption and decryption processes, using specific examples.
   c) Describe how your system ensures security and resists quantum attacks.
   d) Include a simple ASCII diagram or pseudocode (10-15 lines) to illustrate your system's core algorithm.

4. Practical Application (200-250 words):
   a) Propose a real-world scenario where your encryption system could be uniquely useful.
   b) Discuss potential advantages and limitations of your system compared to traditional encryption methods.
   c) Explain how your system could be implemented using current or near-future technology.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss ethical considerations in using endangered languages for encryption purposes.
   b) Analyze potential societal impacts of quantum-linguistic encryption systems.
   c) Propose guidelines for responsible development and use of such technologies.

Ensure your response demonstrates a deep understanding of linguistics, quantum computing, and cryptography. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['language']} and its {t['feature']}.",
            f"The integration of the specified quantum principles ({', '.join(t['quantum_principles'])}) is well-explained and scientifically plausible.",
            "The encryption system design is innovative, coherent, and addresses both linguistic and quantum aspects.",
            "The response includes a clear ASCII diagram or pseudocode (10-15 lines) illustrating the core algorithm.",
            "The practical application scenario is realistic and well-thought-out.",
            "Ethical and societal implications are thoroughly considered, with specific guidelines proposed.",
            "The response shows creativity and interdisciplinary thinking in addressing the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
