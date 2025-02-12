import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "period": "Bronze Age Mediterranean",
                "linguistic_family": "Proto-Indo-European",
                "message": "The sea peoples approach from the west"
            },
            {
                "period": "Classical Maya",
                "linguistic_family": "Mayan",
                "message": "A new king will rise when the stars align"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a historically plausible ancient cryptographic system for the {t['period']} civilization, based on the {t['linguistic_family']} language family. Then, use your system to encode the message: "{t['message']}". Your response should include:

1. Historical and Linguistic Context (200-250 words):
   a) Briefly describe the historical context of the chosen period and civilization.
   b) Explain key features of the specified linguistic family relevant to your cryptographic system.
   c) Discuss any known writing systems or codes from this period that inform your design.

2. Cryptographic System Design (300-350 words):
   a) Describe the key components and mechanisms of your cryptographic system.
   b) Explain how your system incorporates linguistic features of the specified language family.
   c) Discuss how historical and cultural factors of the period influence your design.
   d) Provide a simple visual representation or diagram of your system (use ASCII characters).

3. Encoding Process (200-250 words):
   a) Explain step-by-step how to encode a message using your cryptographic system.
   b) Demonstrate the encoding process with the given message.
   c) Discuss any special considerations or rules for encoding in your system.
   d) Provide the encoded message in a clearly marked format. The encoded message should be at least 50 characters long.

4. Decoding Process (200-250 words):
   a) Describe the procedure for decoding a message in your cryptographic system.
   b) Explain any challenges in decoding and how they might be overcome.
   c) Discuss how a hypothetical archaeologist might approach deciphering your system.

5. Cultural and Historical Implications (150-200 words):
   a) Analyze how your cryptographic system might have been used in its historical context.
   b) Discuss potential impacts of such a system on the civilization's communication and record-keeping.
   c) Propose how the existence of this system might change our understanding of the period.

6. Comparative Analysis (150-200 words):
   a) Compare your system to a known historical cryptographic method.
   b) Discuss similarities and differences in complexity, security, and cultural relevance.
   c) Analyze the strengths and weaknesses of your system in its historical context.

Ensure your response demonstrates a deep understanding of historical linguistics, cryptography, and the specified cultural context. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining historical and linguistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Please include a word count at the end of your submission.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes the historical context of the {t['period']} civilization and key features of the {t['linguistic_family']} language family.",
            "The cryptographic system design is creative, historically plausible for the given period, and incorporates relevant linguistic features.",
            "A visual representation or diagram of the cryptographic system is provided using ASCII characters.",
            f"The encoding process is clearly explained and correctly applied to the message: '{t['message']}'.",
            "The encoded message is provided and is at least 50 characters long.",
            "The decoding process is logically described, with challenges and solutions discussed.",
            "The cultural and historical implications of the cryptographic system are thoughtfully analyzed and historically plausible.",
            "The comparative analysis demonstrates understanding of historical cryptographic methods.",
            "The response is well-structured, uses appropriate terminology, and falls within the specified word count of 1200-1500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
