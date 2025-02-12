import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "message": "The red fox jumps over the lazy dog",
                "quantum_states": ["spin-up", "spin-down"],
                "entanglement_pairs": [(0, 3), (1, 4), (2, 5)],
                "example_superposition": "0.6|spin-up⟩ + 0.8|spin-down⟩"
            },
            "2": {
                "message": "To be or not to be that is the question",
                "quantum_states": ["horizontal", "vertical", "diagonal"],
                "entanglement_pairs": [(0, 2), (1, 3), (4, 5)],
                "example_superposition": "0.5|horizontal⟩ + 0.5|vertical⟩ + 0.707|diagonal⟩"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system based on principles of quantum superposition and entanglement, then use it to encode and decode the following message: "{t['message']}". Your system should use the following quantum states: {', '.join(t['quantum_states'])}. Consider the entanglement pairs: {t['entanglement_pairs']}.

Brief explanation of key concepts:
- Quantum superposition: A quantum state can exist in multiple states simultaneously. For example: {t['example_superposition']}
- Quantum entanglement: Two particles are entangled when the quantum state of each particle cannot be described independently of the other.

Your response should include the following sections, with the specified word counts:

1. Encryption System Design (300-350 words):
   a) Describe the key components of your quantum-inspired linguistic encryption system.
   b) Explain how your system incorporates quantum superposition and entanglement principles.
   c) Detail how linguistic elements (e.g., phonemes, morphemes, or words) are mapped to quantum states.
   d) Discuss any novel features that make your system particularly secure or efficient.

2. Encoding Process (250-300 words):
   a) Provide a step-by-step explanation of how your system encodes the given message.
   b) Describe how quantum superposition is used in the encoding process.
   c) Explain how entanglement is incorporated and its role in the encryption.
   d) Present the encoded message in a suitable format (e.g., quantum state representation).

3. Decoding Process (250-300 words):
   a) Detail the steps required to decode the encrypted message.
   b) Explain how the quantum properties are 'measured' or interpreted during decoding.
   c) Discuss how entanglement information is used in the decoding process.
   d) Demonstrate the successful recovery of the original message.

4. Security Analysis (200-250 words):
   a) Analyze the security strengths of your quantum-inspired linguistic encryption system.
   b) Discuss potential vulnerabilities and how they might be addressed.
   c) Compare your system's security to classical encryption methods.

5. Linguistic Impact (150-200 words):
   a) Discuss how your encryption system might influence our understanding of language structure.
   b) Explore potential applications in linguistic research or natural language processing.

6. Quantum-Classical Interface (150-200 words):
   a) Explain how your system bridges quantum concepts with classical linguistic elements.
   b) Discuss challenges in implementing such a system on classical computers.
   c) Propose ideas for a physical realization of your encryption system.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory.",
            "The encryption system design incorporates principles of quantum superposition and entanglement, with clear explanations of how they are used.",
            "The encoding process is clearly explained, step-by-step, and includes a representation of the encoded message.",
            "The decoding process is logically sound and demonstrates successful recovery of the original message.",
            "The security analysis is thorough, addresses potential vulnerabilities, and compares the system to classical encryption methods.",
            "The response explores the linguistic impact and potential applications of the system in a meaningful way.",
            "The quantum-classical interface is discussed, including specific implementation challenges and plausible ideas for physical realization.",
            "The response is innovative while maintaining scientific plausibility.",
            "The submission is well-structured with clear headings and falls within the specified word count for each section.",
            "The response correctly uses the provided quantum states and entanglement pairs in the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
