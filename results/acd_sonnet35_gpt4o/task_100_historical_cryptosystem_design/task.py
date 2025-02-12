import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "period": "Ancient Rome (1st century BCE)",
                "event": "Julius Caesar's military campaigns",
                "inspiration": "Greek fire signaling system"
            },
            {
                "period": "Renaissance Europe (15th century)",
                "event": "Medici family's banking operations",
                "inspiration": "Leonardo da Vinci's mirror writing"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cryptographic system for {t['period']}, inspired by {t['inspiration']}, and analyze its potential impact on {t['event']}. Your response should include:

1. Cryptosystem Design (4-5 sentences):
   - Describe the basic mechanics of your cryptosystem.
   - Explain how it's inspired by {t['inspiration']}.
   - Discuss how it could be implemented using period-appropriate technology.

2. Encryption Process (2-3 sentences):
   - Provide a step-by-step explanation of how a message would be encrypted.

3. Decryption Process (2-3 sentences):
   - Explain how the intended recipient would decrypt the message.

4. Security Analysis (3-4 sentences):
   - Discuss the strengths and potential vulnerabilities of your cryptosystem.
   - Consider the technological and intellectual context of {t['period']}.

5. Historical Impact Analysis (4-5 sentences):
   - Analyze how your cryptosystem could have influenced {t['event']} if it had been available.
   - Consider both potential positive and negative consequences.

6. Cultural Implications (3-4 sentences):
   - Discuss how the existence of this cryptosystem might have affected the culture or society of {t['period']}.

7. Comparative Analysis (2-3 sentences):
   - Compare your cryptosystem to a real historical cipher or encryption method from a similar time period.

Ensure your cryptosystem is creative, historically plausible, and logically consistent. Your response should demonstrate a strong understanding of both cryptographic principles and historical context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The cryptosystem design is creative, historically plausible, and clearly inspired by the given historical element.",
            "The encryption and decryption processes are logically explained and consistent with the technology of the time period.",
            "The security analysis demonstrates an understanding of cryptographic principles and historical context.",
            "The historical impact analysis provides thoughtful and plausible consequences for the given event.",
            "The cultural implications are well-reasoned and contextually appropriate.",
            "The comparative analysis shows insight into both the designed system and real historical cryptographic methods."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
