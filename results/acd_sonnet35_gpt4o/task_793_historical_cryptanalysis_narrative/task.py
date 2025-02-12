import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ciphers = [
            {
                "encrypted": "WKHUH DUH VHFUHW SODQV WR DWWDFN DW GDZQ",
                "key": 3,
                "context": "Ancient Rome",
                "cipher_type": "Caesar Cipher"
            },
            {
                "encrypted": "XLIVI EVI WIGVIX TPERW XS EXXEGO EX HEAR",
                "key": 4,
                "context": "American Revolution",
                "cipher_type": "Caesar Cipher"
            },
            {
                "encrypted": "GSVIV RIV HVXIVG KORMH GL RGGEXP RG WRDM",
                "key": "VIGENERE",
                "context": "World War I",
                "cipher_type": "Vigenère Cipher"
            },
            {
                "encrypted": "AUVEV REV FVPEVA CYRAF GB NGGNPX NG QNJA",
                "key": "ENIGMA",
                "context": "World War II",
                "cipher_type": "Simple Substitution Cipher"
            }
        ]
        return {str(i+1): random.choice(ciphers) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a historian and cryptanalyst tasked with decrypting a historical message and constructing a plausible narrative based on the decrypted information. Follow these steps:

1. Decryption (100-150 words):
   a) The message "{t['encrypted']}" is encrypted using a {t['cipher_type']}.
   b) Explain the decryption process and provide the decrypted message.
   c) Briefly explain how you determined the correct decryption.

2. Historical Context Analysis (150-200 words):
   a) The message is from the {t['context']} era.
   b) Analyze the historical context of the decrypted message.
   c) Identify key historical figures, events, or conflicts that might be related to the message.

3. Narrative Construction (250-300 words):
   a) Construct a plausible historical narrative incorporating the decrypted message.
   b) Your narrative should include:
      - At least two historical figures (real or fictional)
      - A clear conflict or tension related to the message
      - A resolution or consequence stemming from the message
   c) Ensure your narrative is consistent with known historical facts of the era.

4. Cryptographic Impact Analysis (100-150 words):
   a) Discuss the potential impact of cryptography on historical events related to your narrative.
   b) Explain how the use of this cipher might have influenced communication and strategy during the era.

Ensure your response demonstrates a deep understanding of cryptography, historical analysis, and narrative construction. Be creative in your narrative while maintaining historical plausibility.

Your total response should be between 600-800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must correctly decrypt the given message using the specified cipher type.",
            f"The historical analysis should be accurate and relevant to the {t['context']} era.",
            "The constructed narrative should be creative, plausible, and incorporate the decrypted message effectively.",
            "The cryptographic impact analysis should demonstrate understanding of historical cryptography use.",
            "The response should be between 600-800 words in total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
