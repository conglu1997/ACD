import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            {
                "name": "Ancient Egypt",
                "writing_system": "Hieroglyphics",
                "key_cultural_element": "Afterlife and burial practices"
            },
            {
                "name": "Mayan Empire",
                "writing_system": "Mayan script",
                "key_cultural_element": "Astronomical knowledge and calendar systems"
            }
        ]
        return {str(i+1): civ for i, civ in enumerate(civilizations)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a historical cryptographic system based on the ancient civilization of {t['name']}, then use it to encode and decode a message reflecting their culture. Your task has the following parts:

1. Cryptographic System Design (300-350 words):
   a) Design an original cryptographic system inspired by the {t['writing_system']} of {t['name']}. Avoid directly copying existing historical or modern cryptographic systems.
   b) Explain the encryption and decryption processes of your system, including at least two distinct encryption methods.
   c) Describe how your system incorporates at least three specific elements of the civilization's culture or beliefs.
   d) Provide an example of how a simple word or phrase would be encrypted using both methods.
   e) Discuss potential weaknesses in your cryptographic system and how they might be addressed.
   f) Create a visual representation or diagram of your cryptographic system and explain its key components.
   Note: Ensure your system is historically plausible and avoid anachronistic elements.

2. Historical and Cultural Analysis (250-300 words):
   a) Explain how your cryptographic system reflects the historical context of {t['name']}.
   b) Discuss how the system might have been used in that society, considering their technological capabilities and social structure.
   c) Analyze how the {t['key_cultural_element']} influenced your design, citing at least two specific examples.
   d) Compare how your cryptographic system might differ if designed for the other civilization mentioned in this task family, and explain why.
   e) Discuss the ethical implications of using such a cryptographic system in the historical context of {t['name']}.

3. Message Encoding (200-250 words):
   a) Create a short message (30-40 words) about {t['key_cultural_element']} in {t['name']}.
   b) Encode this message using your cryptographic system, demonstrating both encryption methods.
   c) Explain any challenges in encoding this particular message and how you overcame them.
   d) Discuss how the encoded message might be misinterpreted by someone from a different culture.

4. Message Decoding (200-250 words):
   a) Provide step-by-step instructions for decoding the message, including any necessary cultural context.
   b) Explain how knowledge of the civilization's culture might aid in decryption, giving at least two specific examples.
   c) Discuss any ambiguities or potential misinterpretations in the decoding process and how to resolve them.
   d) Describe a scenario where partial knowledge of the key or system could lead to incorrect but plausible decryptions.

5. Modern Implications (250-300 words):
   a) Compare your historical cryptographic system to a modern encryption method, noting at least three similarities and three differences.
   b) Discuss how studying historical cryptography can inform current security practices, providing at least two concrete examples.
   c) Propose an interdisciplinary research question that this analysis might inspire, involving at least three distinct fields of study.
   d) Speculate on how AI might be used to enhance or break your historical cryptographic system.

Ensure your response demonstrates a deep understanding of cryptography, the specified ancient civilization, and linguistic principles. Be creative in your approach while maintaining historical plausibility. Use clear headings for each section of your response.

Your total response should be between 1200-1450 words. Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['name']}, its {t['writing_system']}, and {t['key_cultural_element']}, with in-depth analysis and specific examples.",
            "The cryptographic system design is original, creative, coherent, and historically plausible, with two distinct encryption methods, consideration of potential weaknesses, and a clear visual representation.",
            "The analysis shows a deep understanding of cryptography and its historical context, with insightful connections between the cryptographic system and the civilization's culture, including ethical considerations.",
            "The encoding and decoding processes are well-explained, logically consistent, and reflect the civilization's technological capabilities, with thorough consideration of potential misinterpretations and ambiguities.",
            "The response addresses all five parts of the task comprehensively, demonstrating creativity, analytical depth, comparative analysis, and interdisciplinary thinking throughout.",
            "The modern implications section provides thoughtful connections to current practices, proposes a compelling interdisciplinary research question, and offers insightful speculation on the interaction between AI and the historical cryptographic system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
