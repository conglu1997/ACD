import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "linguistic_focus": "Metaphors related to time",
                "ai_technique": "Transformer-based language model"
            },
            {
                "source_culture": "Inuit",
                "target_culture": "Swahili",
                "linguistic_focus": "Expressions of spatial relationships",
                "ai_technique": "Recurrent Neural Network with attention mechanism"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate culturally-specific linguistic patterns, idioms, and metaphors for the {t['source_culture']} culture, then use this system to create a cross-cultural communication tool targeting the {t['target_culture']} culture. Your system should focus on {t['linguistic_focus']} and utilize {t['ai_technique']} as its core AI technique. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI cultural linguist system.
   b) Explain how your system analyzes and represents cultural-linguistic patterns.
   c) Detail how you implement {t['ai_technique']} in your system.
   d) Discuss any novel techniques or algorithms used in your approach.

2. Cultural-Linguistic Analysis (250-300 words):
   a) Explain how your system analyzes {t['linguistic_focus']} in the {t['source_culture']} culture.
   b) Describe the methods used to identify and categorize culturally-specific patterns.
   c) Discuss how your system handles ambiguities or context-dependent meanings.

3. Cross-Cultural Pattern Generation (250-300 words):
   a) Detail the process by which your system generates equivalent or analogous {t['linguistic_focus']} for the {t['target_culture']}.
   b) Explain how your system ensures cultural sensitivity and appropriateness in its generations.
   c) Describe any techniques used to preserve the original meaning while adapting to the target culture.

4. Communication Tool Design (200-250 words):
   a) Outline the key features of your cross-cultural communication tool.
   b) Explain how users would interact with the tool to improve cross-cultural understanding.
   c) Describe how your tool handles potential misunderstandings or mistranslations.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural appropriateness of your system's outputs.
   b) Describe potential experiments or user studies to validate your system's effectiveness.
   c) Discuss how you would measure the tool's impact on cross-cultural communication.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential biases or limitations in your system's approach to cultural-linguistic analysis and generation.
   b) Address ethical concerns related to AI-mediated cross-cultural communication.
   c) Propose guidelines for the responsible development and use of AI cultural linguist systems.

7. Future Directions and Implications (150-200 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss the broader implications of AI cultural linguist systems for global communication and understanding.
   c) Propose a novel research question that arises from your work.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of linguistics, cultural anthropology, and artificial intelligence, particularly in relation to {t['linguistic_focus']} and {t['ai_technique']}.",
            f"The system design should clearly explain how it analyzes and generates culturally-specific linguistic patterns for the {t['source_culture']} and {t['target_culture']}.",
            "The approach should be innovative while maintaining scientific plausibility.",
            "The cross-cultural communication tool should be well-designed and address potential challenges in bridging the two cultures.",
            "Ethical considerations and limitations should be thoughtfully addressed.",
            "The response should be well-structured, following the provided format, and include all required sections.",
            "The total word count should be between 1500-1850 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
