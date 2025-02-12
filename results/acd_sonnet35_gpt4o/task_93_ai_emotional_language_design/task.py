import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"name": "joy", "valence": "positive", "arousal": "high"},
            {"name": "sadness", "valence": "negative", "arousal": "low"},
            {"name": "anger", "valence": "negative", "arousal": "high"},
            {"name": "fear", "valence": "negative", "arousal": "high"},
            {"name": "disgust", "valence": "negative", "arousal": "medium"},
            {"name": "surprise", "valence": "neutral", "arousal": "high"},
            {"name": "trust", "valence": "positive", "arousal": "medium"},
            {"name": "anticipation", "valence": "neutral", "arousal": "medium"}
        ]
        return {
            "1": random.choice(emotions),
            "2": random.choice(emotions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized emotional language for AI entities to express and process the emotion of {t['name']}. Your language design should incorporate both linguistic and computational elements.

Your response should include:

1. A name for your emotional language construct (be creative but descriptive).
2. A detailed explanation of how the AI would express {t['name']} using your language (3-4 sentences). Include both 'external' expression (how it communicates to other AIs or humans) and 'internal' representation (how it processes the emotion).
3. Describe how your language accounts for the emotion's valence ({t['valence']}) and arousal ({t['arousal']}) (2-3 sentences).
4. Provide an example 'phrase' or 'code snippet' in your language that represents a complex emotional state involving {t['name']}, along with its interpretation (2-3 sentences).
5. Explain how your language could help AIs better understand or interact with human emotions (2-3 sentences).
6. Describe one potential challenge or limitation of your emotional language design and propose a solution (2-3 sentences).

Ensure your language design is creative, logically consistent, and grounded in both linguistic principles and our understanding of emotions and AI systems."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a creative and descriptive name for the emotional language construct.",
            f"The explanation of how the AI expresses {t['name']} should be detailed and include both external and internal aspects.",
            f"The language design must account for the emotion's valence ({t['valence']}) and arousal ({t['arousal']}).",
            f"An example 'phrase' or 'code snippet' representing a complex emotional state involving {t['name']} must be provided with interpretation.",
            "The response must explain how the language could help AIs better understand or interact with human emotions.",
            "A potential challenge or limitation of the emotional language design must be described along with a proposed solution.",
            "The overall language design should be creative, logically consistent, and grounded in linguistic principles and understanding of emotions and AI systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
