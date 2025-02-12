import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin Chinese", "Swahili"),
            ("Arabic", "Quechua"),
            ("Russian", "Tamil"),
            ("Japanese", "Xhosa")
        ]
        communication_contexts = [
            "Business Negotiation",
            "Medical Consultation",
            "Cultural Exchange Program",
            "Emergency Response Coordination"
        ]
        return {
            "1": {
                "language_pair": random.choice(language_pairs),
                "context": random.choice(communication_contexts)
            },
            "2": {
                "language_pair": random.choice(language_pairs),
                "context": random.choice(communication_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical universal translator system based on linguistic universals and typology, then apply it to solve a cross-cultural communication challenge. Your task involves the following components:

1. Universal Translator System Design (300-350 words):
   a) Explain the key principles of linguistic universals and typology that inform your system design.
   b) Describe the architecture of your universal translator system, including its main components and how they interact.
   c) Explain how your system handles language-specific features such as syntax, morphology, and pragmatics.
   d) Discuss any novel features or improvements your system offers over traditional machine translation approaches.
   e) Provide a visual representation or diagram of your universal translator system design (describe it textually).

2. Linguistic Analysis (250-300 words):
   Language Pair: {t['language_pair'][0]} and {t['language_pair'][1]}
   a) Compare and contrast the linguistic features of the given language pair.
   b) Identify potential challenges in translating between these languages.
   c) Explain how your universal translator system would address these specific challenges.

3. Application to Communication Challenge (250-300 words):
   Context: {t['context']}
   a) Describe a specific scenario within the given context where your universal translator would be used.
   b) Explain how your system would facilitate communication in this scenario.
   c) Discuss any cultural or pragmatic considerations your system takes into account.
   d) Provide an example of a complex phrase or concept and how your system would translate it accurately.

4. Evaluation and Limitations (200-250 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your universal translator system.
   b) Discuss potential limitations of your system, particularly for the given language pair and context.
   c) Suggest areas for future improvement or research in universal translation technology.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the potential impact of a universal translator on global communication and cultural exchange.
   b) Address ethical concerns related to privacy, cultural preservation, and potential misuse of the technology.
   c) Propose guidelines for the responsible development and use of universal translation systems.

6. Interdisciplinary Connections (150-200 words):
   a) Explore how your universal translator system might impact or be applied to fields such as education, diplomacy, or cognitive science.
   b) Discuss potential long-term consequences of widespread adoption of universal translators on language learning and linguistic diversity.

Ensure your response demonstrates a deep understanding of linguistics, language technology, and cross-cultural communication. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section (e.g., '1. Universal Translator System Design', '2. Linguistic Analysis', etc.). Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections comprehensively, following the specified format and word count guidelines.",
            "The universal translator system design demonstrates a clear understanding and application of linguistic universals and typology, including a textual description of a visual representation or diagram.",
            f"The linguistic analysis of the given language pair ({t['language_pair'][0]} and {t['language_pair'][1]}) is thorough and identifies relevant challenges in translation.",
            f"The application to the communication challenge ({t['context']}) is well-explained and demonstrates how the system would be used in a real-world scenario.",
            "The response proposes valid evaluation methods and discusses limitations of the universal translator system.",
            "Ethical and societal implications are thoughtfully addressed, with specific guidelines proposed for responsible development and use.",
            "The interdisciplinary connections section explores novel applications and long-term consequences of the proposed universal translator system.",
            "The writing is clear, well-structured, and demonstrates a high level of creativity while maintaining scientific and technological plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
