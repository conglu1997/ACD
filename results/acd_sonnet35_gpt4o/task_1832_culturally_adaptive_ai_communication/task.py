import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Brazilian",
            "Nigerian",
            "Swedish",
            "Indian"
        ]
        negotiation_contexts = [
            "business merger",
            "international treaty",
            "academic collaboration",
            "conflict resolution",
            "trade agreement"
        ]
        return {
            "1": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(negotiation_contexts)
            },
            "2": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(negotiation_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of adapting its communication style based on cultural contexts, then apply it to a cross-cultural negotiation scenario between {t['culture1']} and {t['culture2']} cultures in the context of a {t['context']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for culturally adaptive communication.
   b) Explain how your system incorporates cultural knowledge and linguistic variations.
   c) Discuss any novel elements in your design that enable real-time adaptation to different cultural contexts.

2. Cultural Modeling (200-250 words):
   a) Explain how your system models cultural differences in communication styles, focusing on {t['culture1']} and {t['culture2']} cultures.
   b) Describe how your model accounts for non-verbal communication and context-dependent meanings.
   c) Discuss how your system handles potential cultural misunderstandings or conflicts.

3. Negotiation Scenario Application (250-300 words):
   a) Apply your AI system to the {t['context']} negotiation scenario between {t['culture1']} and {t['culture2']} parties.
   b) Provide example dialogues demonstrating how your system adapts its communication for each culture.
   c) Explain how your system navigates potential cultural pitfalls in this specific context.

4. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI for cross-cultural communication and negotiation.
   b) Address concerns about cultural stereotyping or oversimplification.
   c) Propose guidelines for responsible development and use of culturally adaptive AI systems.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the effectiveness and cultural appropriateness of your system's communication.
   b) Describe metrics you would use to assess both linguistic accuracy and cultural sensitivity.
   c) Suggest how you would involve human experts from the relevant cultures in the evaluation process.

Ensure your response demonstrates a deep understanding of cross-cultural communication, AI systems, and ethical considerations. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a sophisticated understanding of cultural differences in communication styles, particularly for the specified cultures.",
            "The proposed AI system architecture is innovative and plausibly capable of real-time cultural adaptation.",
            "The application to the negotiation scenario shows nuanced handling of cultural complexities.",
            "Ethical considerations are thoroughly addressed, showing awareness of potential issues like stereotyping.",
            "The evaluation methodology is well-thought-out and includes both quantitative metrics and qualitative cultural expert involvement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
