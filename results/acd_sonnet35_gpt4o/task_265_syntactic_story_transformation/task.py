import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        stories = [
            {
                "text": "The old man sat by the window, watching the rain fall. He sighed, remembering sunny days long past. A knock at the door startled him. He opened it to find a child holding a colorful umbrella, smiling brightly.",
                "transformation": "passive_voice"
            },
            {
                "text": "Sarah sprinted through the crowded streets, her heart racing. The package in her hand felt heavy with responsibility. She ducked into an alley, checked her watch, and took a deep breath. Time was running out.",
                "transformation": "future_tense"
            }
        ]
        return {
            "1": random.choice(stories),
            "2": random.choice(stories)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following story by applying the specified syntactic change. Your task is to rewrite the story while:

1. Applying the syntactic transformation: {t['transformation']}
2. Maintaining the original narrative structure and key events
3. Preserving the emotional tone and impact of the story
4. Ensuring the transformed text remains coherent and readable

Original story:
{t['text']}

Provide your transformed story, followed by a brief explanation (50-75 words) of how you applied the syntactic change and maintained the story's essence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story must be fully transformed according to the specified syntactic change: {t['transformation']}.",
            "The transformed story must maintain the original narrative structure and key events.",
            "The emotional tone and impact of the original story must be preserved in the transformation.",
            "The transformed text must be coherent and readable.",
            "The explanation must accurately describe how the syntactic change was applied and how the story's essence was maintained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
