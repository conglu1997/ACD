import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "global financial system",
                "ethical_concern": "privacy vs. transparency"
            },
            {
                "context": "healthcare data management",
                "ethical_concern": "data security vs. accessibility"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-resistant cryptographic system for use in the {t['context']} and analyze its ethical implications, particularly focusing on the tension between {t['ethical_concern']}. Your response should include:

1. Quantum-Resistant Cryptographic System Design (250-300 words):
   a) Describe the key components of your quantum-resistant cryptographic system.
   b) Explain how your system resists attacks from quantum computers.
   c) Discuss any trade-offs between security and efficiency in your design.

2. Technical Implementation (200-250 words):
   a) Outline the mathematical principles underlying your cryptographic system.
   b) Provide a high-level description of the encryption and decryption processes.
   c) Discuss potential vulnerabilities and how you address them.

3. Application to {t['context']} (200-250 words):
   a) Explain how your system would be implemented in the given context.
   b) Discuss any specific challenges or considerations for this application.
   c) Analyze potential impacts on existing systems and processes.

4. Ethical Analysis (250-300 words):
   a) Examine the ethical implications of implementing your system, focusing on {t['ethical_concern']}.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines for ethical use and governance of your cryptographic system.

5. Future Implications (150-200 words):
   a) Speculate on how quantum-resistant cryptography might evolve in the next decade.
   b) Discuss potential new applications or challenges that may arise.
   c) Consider how society might need to adapt to widespread use of such systems.

Ensure your response demonstrates a deep understanding of quantum computing, cryptography, and ethical reasoning. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum-resistant cryptography.",
            "The cryptographic system design is innovative and well-explained.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The response shows clear application of the system to the given context.",
            "Future implications are insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
