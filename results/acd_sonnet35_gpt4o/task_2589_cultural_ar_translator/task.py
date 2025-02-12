import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "context": "Business meeting",
                "linguistic_feature": "Honorifics"
            },
            {
                "source_culture": "Bedouin",
                "target_culture": "Nordic",
                "context": "Family gathering",
                "linguistic_feature": "Proverbs"
            },
            {
                "source_culture": "Indian",
                "target_culture": "German",
                "context": "Academic conference",
                "linguistic_feature": "Formal address"
            },
            {
                "source_culture": "Maori",
                "target_culture": "Russian",
                "context": "Cultural festival",
                "linguistic_feature": "Metaphors"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an augmented reality cultural translation system that bridges {t['source_culture']} and {t['target_culture']} cultures in the context of a {t['context']}, with a focus on the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AR cultural translation system.
   b) Explain how the system integrates NLP, cultural knowledge bases, and AR technology.
   c) Detail how the system handles real-time processing and display of cultural information.
   d) Discuss any novel techniques used to ensure accuracy and cultural sensitivity.

2. Cultural-Linguistic Analysis (200-250 words):
   a) Analyze how the specified linguistic feature differs between the source and target cultures.
   b) Explain how your system interprets and translates this feature in real-time.
   c) Discuss potential challenges in maintaining cultural authenticity during translation.
   d) Provide an example of how your system would handle a specific phrase or interaction.

3. User Experience Design (200-250 words):
   a) Describe the user interface and interaction methods of your AR system.
   b) Explain how cultural information is visually presented to the user.
   c) Discuss how the system adapts to different user proficiency levels in either culture.
   d) Address potential issues of information overload or distraction in the given context.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to privacy, cultural representation, and technological dependency.
   b) Discuss how your system addresses issues of bias and stereotyping.
   c) Propose guidelines for responsible development and use of AR cultural translation technology.

5. Evaluation and Testing (150-200 words):
   a) Propose a method for evaluating the accuracy and cultural appropriateness of your system.
   b) Describe an experiment to test your system's performance in the given context.
   c) Discuss how you would measure the system's impact on cross-cultural understanding.

6. Future Developments (100-150 words):
   a) Suggest two potential expansions or modifications to your system.
   b) Briefly describe how these changes would enhance its effectiveness or applicability.

Ensure your response demonstrates a deep understanding of both cultures, linguistic principles, and AR technology. Be creative in your design while maintaining scientific and cultural plausibility. Your total response should be between 1050-1350 words. Each section should adhere to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['source_culture']} and {t['target_culture']} cultures.",
            f"The system effectively handles the linguistic feature of {t['linguistic_feature']} in the context of a {t['context']}.",
            "The proposed AR system is innovative yet plausible given current technology.",
            "The response addresses ethical considerations and potential challenges thoroughly.",
            "The evaluation method and future developments are well-thought-out and relevant.",
            "The design shows creativity and original thinking in addressing cross-cultural communication challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
