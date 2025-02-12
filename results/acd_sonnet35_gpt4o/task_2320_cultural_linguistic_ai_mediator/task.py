import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "culture_pair": "Japanese and American",
                "context": "Business negotiation",
                "linguistic_challenge": "Indirect communication vs. direct communication"
            },
            {
                "culture_pair": "Arabic and Chinese",
                "context": "Diplomatic meeting",
                "linguistic_challenge": "Honorifics and formal address"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of mediating cross-cultural communication between {t['culture_pair']} cultures in the context of a {t['context']}, focusing on the linguistic challenge of {t['linguistic_challenge']}. Your system should be able to understand, interpret, and translate complex cultural linguistic nuances, idioms, and context-dependent meanings to facilitate effective communication.

Provide your response in the following format:

1. Cultural-Linguistic Analysis (250-300 words):
   a) Analyze the specific linguistic and cultural differences between the two cultures in the given context.
   b) Explain how these differences might lead to misunderstandings or communication breakdowns.
   c) Identify key idioms, expressions, or communication styles that are particularly challenging to translate or interpret.

2. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system for cultural-linguistic mediation.
   b) Explain how your system integrates natural language processing, cultural knowledge bases, and context understanding.
   c) Detail the data sources and training approach for your AI system.
   d) Propose a novel technique or algorithm specifically designed to handle the given linguistic challenge.

3. Mediation Process (250-300 words):
   a) Outline the step-by-step process your AI system would follow to mediate a conversation.
   b) Explain how the system would identify and resolve potential misunderstandings in real-time.
   c) Describe how your system would handle ambiguity or multiple possible interpretations.

4. Example Scenario (200-250 words):
   a) Provide a specific example of a challenging exchange between the two cultures in the given context.
   b) Demonstrate how your AI system would mediate this exchange, showing its interpretation and output.
   c) Explain the reasoning behind your system's choices in this scenario.

5. Evaluation and Ethical Considerations (200-250 words):
   a) Propose a method to evaluate the effectiveness of your AI mediator in real-world scenarios.
   b) Discuss potential biases or limitations in your system and how you would address them.
   c) Explore ethical considerations in using AI for cross-cultural mediation, including privacy and cultural sensitivity.

6. Future Developments (150-200 words):
   a) Suggest how your system could be expanded to handle a wider range of cultures and contexts.
   b) Propose an innovative feature or capability that could be added to enhance cross-cultural understanding.
   c) Discuss how this technology might impact global communication and intercultural relations in the future.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural accuracy. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the linguistic and cultural differences between {t['culture_pair']} cultures, particularly in the context of {t['context']}.",
            f"The AI system architecture effectively addresses the linguistic challenge of {t['linguistic_challenge']}.",
            "The proposed AI system integrates knowledge from linguistics, cultural anthropology, and artificial intelligence in a novel and coherent manner.",
            "The mediation process and example scenario demonstrate the system's ability to handle complex cultural-linguistic nuances effectively.",
            "The response addresses ethical considerations and potential biases in cross-cultural AI mediation.",
            "The proposed evaluation method and future developments are innovative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
