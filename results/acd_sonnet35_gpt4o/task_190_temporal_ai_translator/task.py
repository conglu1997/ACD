import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_periods = [
            {
                "era": "Medieval Europe",
                "year": "1200 CE",
                "language": "Middle English",
                "topic": "Chivalry and courtly love"
            },
            {
                "era": "Ancient Rome",
                "year": "100 CE",
                "language": "Classical Latin",
                "topic": "Expansion of the Roman Empire"
            },
            {
                "era": "Tang Dynasty China",
                "year": "750 CE",
                "language": "Middle Chinese",
                "topic": "Silk Road trade"
            },
            {
                "era": "Elizabethan England",
                "year": "1600 CE",
                "language": "Early Modern English",
                "topic": "Shakespearean theater"
            }
        ]
        return {
            "1": random.choice(time_periods),
            "2": random.choice(time_periods)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical AI language model capable of translating and communicating between the present day and {t['era']} ({t['year']}), with a focus on {t['language']}. Your task is to:\n\n1. Model Architecture (200-250 words):\n   Describe the key components and features of your AI model that enable it to handle temporal linguistic drift and cultural context. Include:\n   a) How the model processes and represents different time periods\n   b) Mechanisms for handling changes in grammar, vocabulary, and syntax\n   c) Approaches for maintaining cultural context and nuance\n\n2. Training Data and Methodology (150-200 words):\n   Explain how you would acquire and prepare training data for this model, considering the challenges of historical language resources. Describe the training methodology, including any novel approaches to handle temporal aspects.\n\n3. Temporal Adaptation Mechanism (150-200 words):\n   Detail how your model adapts to different time periods, including:\n   a) How it recognizes and adjusts to the target time period\n   b) Techniques for handling intermediate time periods not explicitly trained on\n   c) Methods for maintaining coherence across large time gaps\n\n4. Cultural Context Integration (150-200 words):\n   Describe how your model integrates and maintains cultural context, especially for the given topic of {t['topic']}. Include strategies for:\n   a) Recognizing and preserving culturally specific concepts and idioms\n   b) Adapting modern concepts to historical contexts and vice versa\n   c) Handling potential cultural misunderstandings or anachronisms\n\n5. Ethical Considerations and Limitations (150-200 words):\n   Discuss at least two ethical implications or potential misuses of this technology. Also, address two major limitations of your proposed model and suggest directions for future research to overcome them.\n\n6. Practical Application (100-150 words):\n   Provide a specific example of how your model would translate a modern English sentence related to {t['topic']} into {t['language']} appropriate for {t['era']}. Explain the key challenges in this translation and how your model addresses them.\n\nEnsure your response demonstrates a deep understanding of linguistics, language evolution, and AI technologies. Be creative in your approach while grounding your ideas in plausible scientific and technological concepts. Use clear headings for each section of your response. Your total response should be between 900-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of linguistic principles, language evolution, and AI technologies.",
            "The proposed model architecture is innovative, logically consistent, and effectively addresses the challenges of temporal linguistic drift and cultural context.",
            "The training data and methodology section provides plausible and creative solutions to the challenges of acquiring historical language data.",
            "The temporal adaptation mechanism is well-thought-out and addresses the complexities of adapting language across different time periods.",
            "The cultural context integration section shows a deep understanding of the given historical era and topic, and provides insightful strategies for preserving cultural nuances.",
            "The ethical considerations and limitations section demonstrates critical thinking about the potential impacts and constraints of the technology.",
            "The practical application example is relevant, creative, and effectively illustrates the model's capabilities and challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
