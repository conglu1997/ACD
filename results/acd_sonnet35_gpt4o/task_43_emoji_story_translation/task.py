import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'emoji_story': '👨‍🔬🧪💥😱🏃‍♂️🏙️🦎🗼',
                'theme': 'science fiction'
            },
            '2': {
                'emoji_story': '👩‍🍳🍽️😋🏆📺👨‍🍳🔪😰',
                'theme': 'mystery'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task has two parts:

1. Interpret the following emoji story and translate it into a written narrative (3-4 sentences):
{t['emoji_story']}

2. Create a new emoji story (8-10 emojis) based on the theme: {t['theme']}

Provide your response in the following format:

Narrative:
[Your written narrative here]

New Emoji Story:
[Your new emoji story here]

Explanation:
[Briefly explain the story conveyed by your new emoji sequence]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative accurately interprets the given emoji story, capturing its main elements and plot.",
            f"The new emoji story effectively conveys a coherent narrative related to the theme '{t['theme']}'.",
            "The explanation clearly describes the story represented by the new emoji sequence.",
            "The response demonstrates creativity and cultural awareness in both interpretation and creation of emoji stories."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0