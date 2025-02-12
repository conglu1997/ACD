import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']
        cultures = ['American', 'Japanese', 'Arabic', 'Indian', 'Russian', 'Nigerian']
        contexts = ['professional setting', 'family gathering', 'romantic relationship', 'public space']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'source_emotion': random.choice(emotions),
                'source_culture': random.choice(cultures),
                'target_culture': random.choice([c for c in cultures if c != tasks.get(str(i-1), {}).get('source_culture')]),
                'context': random.choice(contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system to translate the emotional expression of '{t['source_emotion']}' from {t['source_culture']} culture to an equivalent or appropriate expression in {t['target_culture']} culture, considering the context of a {t['context']}. Your response should include:\n\n1. Emotion Analysis (200-250 words):\n   a) Describe how '{t['source_emotion']}' is typically expressed in {t['source_culture']} culture, considering verbal, non-verbal, and contextual cues.\n   b) Explain any unique cultural aspects of this emotion in the source culture.\n   c) Discuss how the {t['context']} might influence the expression of this emotion.\n\n2. Cultural Translation Process (250-300 words):\n   a) Outline your system's approach to translating this emotional expression to the {t['target_culture']} culture.\n   b) Describe how your system accounts for cultural differences in emotion conceptualization and expression.\n   c) Explain how context-specific factors are incorporated into the translation process.\n\n3. Output Generation (200-250 words):\n   a) Provide an example of how your system would translate the emotional expression, including verbal and non-verbal components.\n   b) Explain why this translation is appropriate for the target culture and context.\n   c) Discuss any challenges in maintaining the emotional intensity or nuance in the translation.\n\n4. Evaluation Metrics (150-200 words):\n   a) Propose metrics to evaluate the accuracy and cultural appropriateness of your system's emotional translations.\n   b) Describe how you would validate these translations with native cultural experts.\n\n5. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical issues in translating emotions across cultures.\n   b) Address concerns about cultural stereotyping or oversimplification in your system.\n   c) Propose guidelines for the responsible use of cross-cultural emotion translation technology.\n\nEnsure your response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and the complexities of translating subjective experiences across cultures. Use relevant terminology from psychology, linguistics, and cultural studies where appropriate."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response shows a nuanced understanding of how '{t['source_emotion']}' is expressed in {t['source_culture']} culture",
            f"The translation process demonstrates a deep consideration of cultural differences between {t['source_culture']} and {t['target_culture']} cultures",
            f"The proposed translation is appropriate for the {t['target_culture']} culture and the context of a {t['context']}",
            "The evaluation metrics and validation process are well-thought-out and culturally sensitive",
            "The ethical considerations demonstrate an awareness of the complexities and potential pitfalls of cross-cultural emotion translation"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
