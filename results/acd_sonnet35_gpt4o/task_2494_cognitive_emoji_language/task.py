import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "democracy",
            "climate change",
            "artificial intelligence",
            "quantum entanglement",
            "cultural identity",
            "economic inequality",
            "biodiversity",
            "consciousness"
        ]
        languages = [
            "English",
            "Mandarin Chinese",
            "Arabic",
            "Swahili",
            "Hindi",
            "Russian",
            "Spanish",
            "Japanese"
        ]
        return {
            "1": {
                "concept": random.choice(concepts),
                "source_language": random.choice(languages),
                "target_language": random.choice(languages)
            },
            "2": {
                "concept": random.choice(concepts),
                "source_language": random.choice(languages),
                "target_language": random.choice(languages)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system using emojis based on cognitive linguistics principles, then use it to translate the complex concept of '{t['concept']}' from {t['source_language']} to {t['target_language']}. Your task has the following parts:

1. Cognitive Emoji System Design (250-300 words):
   a) Outline the key principles of your emoji-based communication system, drawing from cognitive linguistics theories.
   b) Explain how your system represents different types of concepts (e.g., actions, objects, abstract ideas) using combinations of emojis.
   c) Describe how your system handles grammar, syntax, and complex relationships between concepts.
   d) Provide examples of basic emoji combinations and their meanings in your system.

2. Cultural Adaptation Mechanism (200-250 words):
   a) Explain how your system adapts to cultural differences when translating between languages.
   b) Describe the process of mapping culturally specific concepts to more universal representations.
   c) Discuss how your system handles idioms, metaphors, and other culturally embedded expressions.

3. Concept Translation (250-300 words):
   a) Translate the concept of '{t['concept']}' from {t['source_language']} into your emoji-based system.
   b) Explain the rationale behind your emoji choices and combinations.
   c) Then, translate this emoji representation into {t['target_language']}.
   d) Analyze how the meaning may have changed or been preserved through this double translation.

4. Linguistic Analysis (200-250 words):
   a) Compare the original {t['source_language']} expression of the concept with the final {t['target_language']} translation.
   b) Identify any challenges or insights gained from this translation process.
   c) Discuss how your emoji-based system might reveal underlying cognitive structures common across languages.

5. AI Integration Proposal (150-200 words):
   a) Propose how AI could be integrated into your cognitive emoji system to improve its translation capabilities.
   b) Describe potential machine learning approaches for automatically generating and interpreting emoji combinations.
   c) Discuss how this AI-enhanced system could be used for real-time cross-lingual communication.

Ensure your response demonstrates a deep understanding of cognitive linguistics, emoji semantics, cross-cultural communication, and AI principles. Be creative in your system design while maintaining scientific plausibility and practical applicability.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a detailed design of a cognitive emoji-based communication system with clear principles and examples.",
            "The cultural adaptation mechanism should be thoroughly explained, addressing how the system handles cultural differences and idioms.",
            f"The concept of '{t['concept']}' must be translated from {t['source_language']} to emoji, then to {t['target_language']}, with a clear explanation of the process.",
            "A linguistic analysis comparing the original and final translations should be provided, including challenges and insights.",
            "An AI integration proposal for improving the system must be included, with specific machine learning approaches suggested.",
            "The response should demonstrate deep understanding of cognitive linguistics, emoji semantics, cross-cultural communication, and AI principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
