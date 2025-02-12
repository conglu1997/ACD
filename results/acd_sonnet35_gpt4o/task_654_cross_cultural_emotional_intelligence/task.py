import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion": "grief",
                "culture1": "Japanese",
                "culture2": "Italian",
                "context": "loss of a loved one"
            },
            {
                "emotion": "pride",
                "culture1": "American",
                "culture2": "Chinese",
                "context": "academic achievement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system for cross-cultural emotional intelligence, focusing on the emotion of {t['emotion']} in the context of {t['context']}. Your system should be able to interpret and generate emotionally nuanced language for both {t['culture1']} and {t['culture2']} cultures. Provide your response in the following format:\n\n1. System Overview (200-250 words):\nDescribe the key components and mechanisms of your AI system for cross-cultural emotional intelligence.\n\n2. Cultural Analysis (200-250 words):\nAnalyze how the expression of {t['emotion']} in the context of {t['context']} differs between {t['culture1']} and {t['culture2']} cultures.\n\n3. Language Processing (150-200 words):\nExplain how your system would interpret emotionally nuanced language related to {t['emotion']} in both cultures.\n\n4. Language Generation (150-200 words):\nDescribe how your system would generate culturally appropriate emotional language for {t['emotion']} in both cultures.\n\n5. Evaluation Method (100-150 words):\nPropose a method to evaluate the effectiveness of your system in accurately interpreting and generating emotionally nuanced language across these cultures.\n\n6. Ethical Considerations (100-150 words):\nDiscuss potential ethical implications or challenges arising from the development or application of your cross-cultural emotional intelligence system.\n\nEnsure your response demonstrates a deep understanding of emotional intelligence, cultural anthropology, and natural language processing. Be innovative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively addresses the interpretation and generation of language related to {t['emotion']} in both {t['culture1']} and {t['culture2']} cultures.",
            "The response demonstrates a nuanced understanding of cultural differences in emotional expression.",
            "The proposed AI system is innovative and theoretically sound.",
            "The cultural analysis shows depth and insight into the specific emotion and context.",
            "The language processing and generation components are well-explained and culturally sensitive.",
            "The evaluation method is appropriate and well-designed for cross-cultural comparison.",
            "Ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
