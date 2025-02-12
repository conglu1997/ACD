import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum teleportation"
        ]
        cryptographic_goals = [
            "key distribution",
            "secure messaging",
            "authentication",
            "data integrity"
        ]
        multiverse_challenges = [
            "temporal inconsistencies",
            "parallel universe interference",
            "quantum decoherence across realities",
            "multidimensional eavesdropping"
        ]
        
        return {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "cryptographic_goal": random.choice(cryptographic_goals),
                "multiverse_challenge": random.choice(multiverse_challenges)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "cryptographic_goal": random.choice(cryptographic_goals),
                "multiverse_challenge": random.choice(multiverse_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cryptographic protocol for secure communication in a multiverse scenario. Your protocol should utilize the quantum property of {t['quantum_property']} to achieve the cryptographic goal of {t['cryptographic_goal']} while addressing the multiverse challenge of {t['multiverse_challenge']}.

Your response should include:

1. Protocol Overview (100-150 words):
   Provide a high-level description of your quantum cryptographic protocol, explaining how it incorporates the specified quantum property and addresses the cryptographic goal in a multiverse context.

2. Quantum Mechanism (100-150 words):
   Explain the quantum mechanical principles underlying your protocol, focusing on how {t['quantum_property']} is utilized.

3. Multiverse Considerations (100-150 words):
   Describe how your protocol addresses the challenge of {t['multiverse_challenge']} in a multiverse scenario.

4. Protocol Steps (150-200 words):
   Outline the step-by-step process of your protocol, including initialization, key generation, encryption, transmission, and decryption. Use clear, concise language and, if helpful, simple pseudocode or diagrams.

5. Security Analysis (100-150 words):
   Discuss the security strengths and potential vulnerabilities of your protocol, particularly in the context of the multiverse scenario.

6. Practical Challenges (100-150 words):
   Identify and explain at least two practical challenges in implementing your protocol, considering both current technological limitations and the speculative nature of the multiverse scenario.

7. Future Implications (100-150 words):
   Speculate on how your protocol, if realized, might impact fields beyond cryptography, such as physics, computing, or philosophy.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and information theory while creatively applying these concepts to a speculative multiverse scenario. Use appropriate scientific terminology and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The protocol clearly utilizes the quantum property of {t['quantum_property']}.",
            f"The protocol effectively addresses the cryptographic goal of {t['cryptographic_goal']}.",
            f"The response adequately considers the multiverse challenge of {t['multiverse_challenge']}.",
            "The protocol demonstrates a strong understanding of quantum mechanics and cryptography.",
            "The response is creative and scientifically plausible within the speculative scenario.",
            "All seven requested sections are present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
