import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_type": "Ancient",
                "civilization": "Minoan",
                "script": "Linear A",
                "context": "Administrative tablet"
            },
            {
                "language_type": "Fictional",
                "civilization": "Elven",
                "script": "Tengwar",
                "context": "Magical incantation"
            },
            {
                "language_type": "Ancient",
                "civilization": "Indus Valley",
                "script": "Indus Script",
                "context": "Seal inscription"
            },
            {
                "language_type": "Fictional",
                "civilization": "Klingon",
                "script": "pIqaD",
                "context": "Spaceship manual"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that combines principles of cryptography and linguistic evolution to decrypt and interpret {t['language_type'].lower()} languages, then apply it to decrypting and interpreting a {t['civilization']} {t['script']} {t['context']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for decrypting and interpreting unknown languages.
   b) Explain how your system integrates cryptographic techniques with linguistic analysis.
   c) Discuss any novel algorithms or approaches in your design that enable effective decryption of ancient or fictional scripts.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture (describe it textually).

2. Cryptolinguistic Modeling (250-300 words):
   a) Explain how your system models the evolution of languages and scripts over time.
   b) Describe how it incorporates known linguistic universals and patterns of language change.
   c) Discuss how your model handles the challenges specific to decrypting {t['language_type'].lower()} languages.

3. Decryption Process (250-300 words):
   a) Outline the step-by-step process your AI system would follow to decrypt the {t['civilization']} {t['script']}.
   b) Explain how it would handle unknown symbols, grammatical structures, and contextual meanings.
   c) Describe how your system would validate its decryption and interpretation hypotheses.

4. Application to Scenario (200-250 words):
   a) Apply your AI system to the task of decrypting and interpreting the {t['civilization']} {t['script']} {t['context']}.
   b) Provide a hypothetical example of a partially decrypted text and explain your system's interpretation process.
   c) Discuss any specific challenges this scenario presents and how your system addresses them.

5. Ethical and Historical Implications (150-200 words):
   a) Discuss the potential impact of your AI system on fields such as archaeology, historical linguistics, and cryptography.
   b) Address ethical considerations related to using AI for decrypting culturally significant or sensitive texts.
   c) Propose guidelines for the responsible use and development of cryptolinguistic AI systems.

6. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the accuracy and reliability of your system's decryptions and interpretations.
   b) Describe how you would validate the system's results against existing linguistic and historical knowledge.
   c) Suggest how domain experts could be involved in refining and validating the AI's outputs.

Ensure your response demonstrates a deep understanding of cryptography, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and historical plausibility. Balance innovation with realistic constraints based on current technological capabilities.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cryptography, linguistics, and artificial intelligence.",
            "The proposed AI system effectively integrates principles from cryptography and linguistic evolution.",
            f"The system is appropriately applied to the {t['civilization']} {t['script']} decryption scenario.",
            "The response includes creative and plausible solutions to the challenges of decrypting unknown languages.",
            "Ethical implications and evaluation methods are thoroughly discussed.",
            "The response is well-structured, clear, and within the specified word count range.",
            "The proposed solutions balance innovation with realistic constraints based on current technological capabilities."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
