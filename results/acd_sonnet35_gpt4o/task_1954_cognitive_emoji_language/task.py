import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "climate change",
                "domain": "environmental science"
            },
            {
                "concept": "artificial intelligence ethics",
                "domain": "technology and philosophy"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a comprehensive communication system using only emojis, based on cognitive linguistics principles, and demonstrate its application in conveying complex ideas. Your task has the following parts:

1. Emoji Language Design (250-300 words):
   a) Outline the key principles of your emoji-based language, drawing from cognitive linguistics theories.
   b) Explain how your system handles grammar, syntax, and semantics using only emojis.
   c) Describe how your language incorporates cognitive concepts like metaphor, metonymy, and image schemas.
   d) Provide examples of basic emoji combinations and their meanings.

2. Cognitive Basis (200-250 words):
   a) Explain how your emoji language aligns with theories of human cognition and language processing.
   b) Discuss potential cognitive advantages or challenges of using this emoji-based system.
   c) Describe how your system might impact memory, comprehension, and cross-cultural communication.

3. Complex Idea Expression (250-300 words):
   Demonstrate how your emoji language can be used to explain the concept of "{t['concept']}" in the domain of {t['domain']}. Provide:
   a) A sequence of emojis representing key aspects of the concept.
   b) A detailed explanation of how each emoji or combination conveys specific ideas.
   c) An analysis of how the overall sequence captures the complexity of the concept.

4. Translation Challenge (150-200 words):
   a) Provide a short paragraph (3-4 sentences) in English about {t['concept']}.
   b) Translate this paragraph into your emoji language.
   c) Explain your translation process and any challenges encountered.

5. Potential Applications (150-200 words):
   a) Propose two potential real-world applications of your emoji-based language system.
   b) Discuss how these applications could benefit from the cognitive principles underlying your design.

Ensure your response demonstrates a deep understanding of cognitive linguistics, emoji semantics, and the chosen concept. Be creative in your language design while maintaining logical consistency and clarity in communication.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The emoji language design is comprehensive and based on cognitive linguistics principles.",
            f"The complex idea of {t['concept']} is effectively conveyed using the emoji language.",
            "The response demonstrates creativity and a deep understanding of cognitive science and linguistics.",
            "The potential applications proposed are innovative and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
