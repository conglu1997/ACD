import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "English",
                "target_language": "Japanese",
                "emotion": "melancholy",
                "domain": "nature"
            },
            {
                "source_language": "Spanish",
                "target_language": "Mandarin Chinese",
                "emotion": "joy",
                "domain": "technology"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates metaphors from {t['source_language']} to {t['target_language']} while preserving the emotional content of '{t['emotion']}', focusing on metaphors related to {t['domain']}. Then, analyze its potential impact on cross-cultural communication and AI development. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your metaphor translation system.
   b) Explain how your system identifies and preserves emotional content in metaphors.
   c) Detail the process of translating metaphors while maintaining their emotional impact.
   d) Discuss how your system handles culture-specific metaphors and emotions.
   e) Provide a simple diagram or flowchart of your system's architecture (describe it textually).

2. Linguistic and Emotional Analysis (250-300 words):
   a) Analyze the challenges in translating metaphors between {t['source_language']} and {t['target_language']}.
   b) Explain how your system captures and translates the emotion of '{t['emotion']}' in metaphors.
   c) Provide two examples of metaphors related to {t['domain']} in {t['source_language']}, and explain how your system would translate them to {t['target_language']} while preserving the emotional content.

3. Cross-cultural Impact (200-250 words):
   a) Discuss the potential impact of your system on cross-cultural communication.
   b) Analyze how preserving emotional content in metaphor translation might affect intercultural understanding.
   c) Explore potential applications of your system in fields such as diplomacy, international business, or global education.

4. AI and Cognitive Science Implications (200-250 words):
   a) Explain how your system contributes to our understanding of the relationship between language, emotion, and cognition.
   b) Discuss the implications of your system for developing emotionally intelligent AI.
   c) Propose a hypothesis about how this approach to metaphor translation might inform theories of human language processing.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues or concerns raised by your proposed system.
   b) Discuss how these ethical considerations might be addressed or mitigated.
   c) Propose guidelines for the responsible development and use of emotion-preserving metaphor translation technology.

6. Evaluation and Future Work (150-200 words):
   a) Describe how you would evaluate the effectiveness and accuracy of your system.
   b) Discuss potential limitations of your approach.
   c) Suggest areas for future research or improvement in metaphor translation and emotional preservation in AI systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on translating metaphors from {t['source_language']} to {t['target_language']}.",
            f"The system design addresses preserving the emotional content of '{t['emotion']}'.",
            f"The response includes metaphors related to {t['domain']}.",
            "The system design is innovative yet plausible, demonstrating interdisciplinary knowledge.",
            "The response covers all six required sections with appropriate detail and coherence.",
            "The linguistic and emotional analysis demonstrates understanding of metaphor translation challenges.",
            "The cross-cultural impact and AI implications are thoughtfully discussed.",
            "The response includes a textual description of a diagram or flowchart of the system's architecture.",
            "The ethical considerations section discusses potential issues and proposes guidelines.",
            "The evaluation and future work section addresses limitations and suggests areas for improvement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
