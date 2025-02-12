import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Japanese",
                "context": "Business negotiation",
                "key_concepts": ["harmony", "indirect communication", "hierarchy"]
            },
            {
                "name": "Brazilian",
                "context": "Social gathering",
                "key_concepts": ["warmth", "personal relationships", "flexibility"]
            },
            {
                "name": "Bedouin",
                "context": "Conflict resolution",
                "key_concepts": ["honor", "hospitality", "tribal loyalty"]
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can adapt its language use to the {t['name']} cultural context, specifically for a {t['context']} scenario. Your task has four parts:

1. Cultural-Linguistic Analysis (200-250 words):
   a) Explain the key linguistic features and communication styles associated with {t['name']} culture, particularly in the context of {t['context']}.
   b) Discuss how the key concepts of {', '.join(t['key_concepts'])} are typically expressed in language and behavior.
   c) Provide examples of common idioms, metaphors, or expressions used in this cultural context.

2. AI System Design (250-300 words):
   a) Outline the main components of your AI system, including data input, processing, and output generation.
   b) Explain how your system would identify and generate culturally appropriate language.
   c) Describe how the system would handle ambiguity and context-dependent meanings.
   d) Discuss how your system would avoid cultural stereotypes or oversimplifications.

3. Adaptation Mechanism (200-250 words):
   a) Propose a method for your AI system to adapt its language in real-time based on user interactions.
   b) Explain how the system would learn from mistakes or misunderstandings.
   c) Describe how the system would balance maintaining its core knowledge while being flexible to new input.

4. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues in creating an AI system that emulates cultural-specific communication.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Explain limitations of your proposed system and areas for future improvement.

Ensure your response demonstrates a deep understanding of computational linguistics, cultural anthropology, and AI capabilities. Be creative in your approach while grounding your ideas in established theories and ethical considerations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a nuanced understanding of {t['name']} culture and its linguistic features, especially in the context of {t['context']}.",
            f"The AI system design should clearly address how it would incorporate the key concepts of {', '.join(t['key_concepts'])} into its language generation.",
            "The proposed adaptation mechanism should be technically feasible and culturally sensitive.",
            "The response must thoughtfully address ethical considerations and potential limitations of the system.",
            "The overall solution should be creative while remaining grounded in real-world cultural and linguistic knowledge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
