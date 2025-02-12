import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        hieroglyphs = [
            {"name": "Ankh", "meaning": "Life", "quantum_property": "Superposition"},
            {"name": "Djed", "meaning": "Stability", "quantum_property": "Entanglement"},
            {"name": "Wadjet", "meaning": "Protection", "quantum_property": "Quantum tunneling"},
            {"name": "Scarab", "meaning": "Creation", "quantum_property": "Wave function collapse"}
        ]
        return {
            "1": random.choice(hieroglyphs),
            "2": random.choice(hieroglyphs)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum encryption system inspired by the ancient Egyptian hieroglyph '{t['name']}' (meaning: {t['meaning']}) and the quantum property of {t['quantum_property']}. Then, use your system to encode and decode a message. Your response should include:

1. Quantum Hieroglyphic Encryption System Design (300-350 words):
   a) Explain how you integrate the meaning of the hieroglyph into your quantum encryption system.
   b) Describe how the specified quantum property is utilized in your encryption method.
   c) Detail the encryption and decryption processes, including any necessary quantum operations.
   d) Discuss potential advantages of your system over classical encryption methods.
   e) Propose a method to combine multiple hieroglyphs in your encryption system for added complexity.

2. Encoding Process (200-250 words):
   a) Choose a short message (10-15 words) related to the hieroglyph's meaning.
   b) Describe step-by-step how your system would encode this message.
   c) Explain how the quantum property is manifested in the encoded message.
   d) Present the encoded message in a standardized format, using a combination of symbols and quantum states (e.g., |ψ⟩ = α|0⟩ + β|1⟩).

3. Decoding Process (200-250 words):
   a) Outline the steps needed to decode the message using your quantum hieroglyphic system.
   b) Discuss any challenges that might arise during decoding and how to address them.
   c) Explain how the original meaning of the hieroglyph aids in the decoding process.
   d) Demonstrate the decoding of your encoded message to retrieve the original text.

4. Security Analysis (150-200 words):
   a) Analyze the security strengths of your quantum hieroglyphic encryption system.
   b) Identify potential vulnerabilities and propose ways to mitigate them.
   c) Compare the security of your system to current quantum encryption methods.
   d) Discuss how the integration of multiple hieroglyphs affects the system's security.

5. Practical Implementation (150-200 words):
   a) Discuss the feasibility of implementing your system with current or near-future quantum computing technology.
   b) Propose potential applications for your quantum hieroglyphic encryption system.
   c) Suggest modifications that could enhance the system's practicality or efficiency.
   d) Outline a potential roadmap for developing and testing a prototype of your system.

Ensure your response demonstrates a deep understanding of both quantum computing principles and the symbolic significance of ancient Egyptian hieroglyphs. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from both fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The encryption system effectively integrates the meaning of the '{t['name']}' hieroglyph and the quantum property of {t['quantum_property']}.",
            "The encoding and decoding processes are clearly explained and scientifically plausible.",
            "The encoded message is presented in the specified standardized format.",
            "The security analysis demonstrates a deep understanding of both quantum encryption and classical cryptography.",
            "The response shows creativity in bridging ancient symbolism with cutting-edge quantum technology.",
            "The practical implementation discussion is realistic and considers current technological limitations.",
            "The proposed method for combining multiple hieroglyphs adds complexity to the encryption system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
