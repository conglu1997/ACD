import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        contexts = [
            "business negotiation",
            "diplomatic exchange",
            "educational setting",
            "healthcare consultation",
            "social media interaction",
            "religious ceremony"
        ]
        culture_pairs = [
            ("Japanese", "Brazilian"),
            ("Nigerian", "Swedish"),
            ("Indian", "Australian"),
            ("Egyptian", "South Korean"),
            ("Russian", "Mexican"),
            ("Canadian", "Saudi Arabian")
        ]
        communication_modes = [
            "verbal (speech and text)",
            "non-verbal (gestures and facial expressions)",
            "paralinguistic (tone, pitch, and rhythm of speech)"
        ]
        communication_challenges = [
            "expressing disagreement politely",
            "conveying urgency without causing offense",
            "showing respect to authority figures",
            "expressing gratitude appropriately",
            "navigating taboo topics",
            "interpreting indirect communication"
        ]
        
        return {
            "1": {
                "context": random.choice(contexts),
                "culture_pair": random.choice(culture_pairs),
                "primary_mode": random.choice(communication_modes),
                "challenge": random.choice(communication_challenges)
            },
            "2": {
                "context": random.choice(contexts),
                "culture_pair": random.choice(culture_pairs),
                "primary_mode": random.choice(communication_modes),
                "challenge": random.choice(communication_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating and adapting multimodal communication across different cultures, then use it to analyze and generate culturally appropriate communication in a {t['context']} context, focusing on translating between {t['culture_pair'][0]} and {t['culture_pair'][1]} cultures, with emphasis on the {t['primary_mode']} mode of communication. Your system should specifically address the challenge of {t['challenge']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-cultural, multimodal communication translation.
   b) Explain how your system integrates linguistic, psychological, and cultural knowledge.
   c) Discuss how your system handles the primary mode of communication and its interaction with other modes.
   d) Include a high-level diagram or detailed description of your system's architecture.

2. Cultural Analysis (250-300 words):
   a) Compare and contrast how the specified cultures typically communicate in the given context.
   b) Identify at least three key differences in {t['primary_mode']} communication between these cultures.
   c) Discuss how these differences might lead to misunderstandings and how your system would address them.

3. Translation and Adaptation Process (250-300 words):
   a) Explain your system's approach to translating and adapting communication between the specified cultures.
   b) Provide a specific example of how your system would handle the given communication challenge in the specified context.
   c) Discuss how your system ensures cultural appropriateness and maintains the original intent of the communication.

4. Multimodal Integration (200-250 words):
   a) Describe how your system integrates different modes of communication in its translation process.
   b) Explain how the primary mode interacts with and influences other modes in your system.
   c) Discuss any challenges in aligning multiple communication modes across cultures and how your system addresses them.

5. Evaluation and Ethical Considerations (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural sensitivity of your system's outputs.
   b) Discuss potential biases or limitations in your approach and how they might be addressed.
   c) Explore ethical implications of using AI for cross-cultural communication and propose guidelines for responsible use.

Ensure your response demonstrates a deep understanding of linguistics, psychology, cultural studies, and AI technologies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural accuracy.

Format your response with clear headings for each section and number your points as shown above. Use concrete examples and scenarios to illustrate your points. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed AI system architecture for cross-cultural, multimodal communication translation, with clear integration of linguistic, psychological, and cultural knowledge.",
            "The cultural analysis demonstrates a deep understanding of the specified cultures and their communication differences in the given context, with at least three key differences identified.",
            "The translation and adaptation process is clearly explained with a relevant example that specifically addresses the given communication challenge in the specified context.",
            "The multimodal integration section effectively describes how different communication modes are handled and aligned across cultures, with a focus on the primary mode specified in the task.",
            "The evaluation and ethical considerations section provides thoughtful methods for system evaluation and addresses potential biases and ethical implications, including guidelines for responsible use.",
            "The overall response is well-structured, coherent, and adheres to the specified word count and formatting requirements, using concrete examples and scenarios to illustrate key points."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
