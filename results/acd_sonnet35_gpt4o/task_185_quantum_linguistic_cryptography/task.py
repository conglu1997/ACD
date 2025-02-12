import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "tonal patterns",
            "grammatical gender",
            "evidentiality",
            "honorifics",
            "aspect marking",
            "ergativity",
            "classificatory verbs",
            "switch-reference"
        ]
        quantum_properties = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum teleportation",
            "quantum interference"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "quantum_property": random.choice(quantum_properties)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "quantum_property": random.choice(quantum_properties)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based cryptographic system that encodes the linguistic feature of {t['linguistic_feature']} using the quantum property of {t['quantum_property']}. Then, create and solve a puzzle using this system. Your task has the following parts:

1. Quantum Linguistic Cryptosystem Design (150-200 words):
   a) Explain how your system uses {t['quantum_property']} to encode {t['linguistic_feature']}.
   b) Describe the encryption and decryption processes.
   c) Discuss how your system ensures security and handles potential quantum attacks.

2. Encoding Process (100-150 words):
   a) Provide a step-by-step explanation of how a specific linguistic element would be encoded.
   b) Include at least one mathematical formula or quantum circuit diagram to illustrate the process.

3. Puzzle Creation (100-150 words):
   a) Create a puzzle that requires decoding a message encrypted with your system.
   b) Provide the encrypted message and any necessary context for solving the puzzle.

4. Puzzle Solution (100-150 words):
   a) Explain the step-by-step process to solve the puzzle.
   b) Decode the message and explain its linguistic significance.

5. Potential Applications (100-150 words):
   a) Propose two potential applications of your quantum linguistic cryptosystem in fields such as secure communication, language preservation, or cognitive science.
   b) Explain how the unique properties of your system make it suitable for these applications.

6. Limitations and Future Improvements (100-150 words):
   a) Discuss two potential limitations of your system.
   b) Propose ways to address these limitations or extend the system's capabilities.

Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of quantum computing, cryptography, and linguistics. Use appropriate terminology from all relevant fields and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cryptosystem must use {t['quantum_property']} to encode {t['linguistic_feature']}.",
            "The response must include a clear explanation of the encryption and decryption processes.",
            "A step-by-step encoding process must be provided with at least one mathematical formula or quantum circuit diagram.",
            "The puzzle created must require decoding a message encrypted with the designed system.",
            "A step-by-step solution to the puzzle must be provided, including the decoded message and its linguistic significance.",
            "Two potential applications of the quantum linguistic cryptosystem must be proposed and explained.",
            "Two limitations of the system must be discussed, with proposals for addressing them.",
            "The response must demonstrate a deep understanding of quantum computing, cryptography, and linguistics, using appropriate terminology from all fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
