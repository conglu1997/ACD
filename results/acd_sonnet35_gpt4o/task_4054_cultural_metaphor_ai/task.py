import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Nigerian (Yoruba)",
            "Mexican",
            "Russian",
            "Indian (Hindi)",
            "Australian Aboriginal"
        ]
        domains = [
            "Nature and Environment",
            "Family and Relationships",
            "Work and Business",
            "Emotions and Mental States",
            "Time and Change",
            "Life and Death"
        ]
        return {
            "1": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "domain": random.choice(domains)
            },
            "2": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "domain": random.choice(domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding, analyzing, and generating culturally-specific metaphors and idioms across multiple languages and cultures. Your system should be able to translate metaphors from the {t['source_culture']} culture to equivalent or similar metaphors in the {t['target_culture']} culture, focusing on the domain of {t['domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure and key components of your AI system.
   b) Explain how your system represents and processes cultural knowledge and linguistic information.
   c) Detail the mechanisms for metaphor analysis, translation, and generation.
   d) Discuss how your system integrates natural language processing with cultural understanding.

2. Cultural Knowledge Representation (250-300 words):
   a) Explain how your system encodes and represents cultural knowledge relevant to metaphor understanding.
   b) Describe how you ensure comprehensive and accurate representation of the specified cultures.
   c) Discuss any novel approaches to capturing the nuances and contexts of cultural metaphors.
   d) Explain how your system handles cultural evolution and regional variations within cultures.

3. Metaphor Analysis and Translation Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to analyze a metaphor from the source culture.
   b) Explain how your system identifies equivalent or similar metaphors in the target culture.
   c) Describe how your system handles cases where direct equivalents don't exist.
   d) Provide an example of how your system would translate a specific metaphor from {t['source_culture']} to {t['target_culture']} culture in the domain of {t['domain']}.

4. Metaphor Generation (200-250 words):
   a) Explain how your system generates new, culturally appropriate metaphors.
   b) Describe the creative process and any constraints or guidelines used.
   c) Discuss how your system ensures the generated metaphors are meaningful and culturally sensitive.
   d) Provide an example of a novel metaphor your system might generate for the {t['target_culture']} culture in the domain of {t['domain']}.

5. Evaluation and Refinement (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural authenticity of your system's metaphor translations and generations.
   b) Describe how you would incorporate feedback from native speakers and cultural experts.
   c) Explain how your system learns and improves its performance over time.
   d) Discuss any potential biases in your system and how you would address them.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss the ethical implications of an AI system that generates and translates cultural metaphors.
   b) Address potential issues of cultural appropriation or misrepresentation.
   c) Propose guidelines for the responsible development and use of such systems.
   d) Suggest potential applications of your system in fields such as education, diplomacy, or cross-cultural communication.

7. Limitations and Future Work (150-200 words):
   a) Acknowledge the limitations of your current system design.
   b) Suggest areas for future research or improvement.
   c) Discuss how advancements in AI and cultural studies might enhance systems like yours in the future.

Ensure your response demonstrates a deep understanding of cultural anthropology, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            "The proposed AI system demonstrates a deep understanding of cultural metaphors and idioms.",
            f"The system effectively handles metaphor translation between {t['source_culture']} and {t['target_culture']} cultures.",
            f"The response shows a strong grasp of the cultural nuances related to the domain of {t['domain']}.",
            "The proposed system is innovative yet scientifically plausible.",
            "The response addresses ethical considerations and potential applications of the technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
