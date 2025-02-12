import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_technologies = [
            "Emotion recognition AI in public spaces",
            "AI-driven genetic modification for human enhancement",
            "Autonomous AI systems in criminal justice",
            "AI-powered mind-reading devices for marketing"
        ]
        return {
            "1": {"technology": random.choice(ai_technologies)},
            "2": {"technology": random.choice(ai_technologies)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (300-400 words) set in the year 2050 that explores the ethical implications of {t['technology']}. Your story should:

1. Describe a specific scenario where the technology is being used.
2. Highlight at least two ethical dilemmas arising from its use.
3. Show how different stakeholders are affected by the technology.
4. Have a clear narrative arc with a beginning, middle, and end.

After the story, provide an analysis (200-250 words) that:
1. Identifies the main ethical principles or frameworks relevant to the scenario.
2. Discusses the potential long-term consequences of the technology's use as depicted in your story.
3. Proposes at least one potential solution or regulation to address the ethical concerns raised.

Format your response as follows:

Story Title: [Your title]

Story:
[Your story here]

Analysis:
[Your analysis here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story is 300-400 words long and set in the year 2050.",
            "The story explores the ethical implications of the given AI technology.",
            "At least two ethical dilemmas are highlighted in the story.",
            "The story shows how different stakeholders are affected by the technology.",
            "The story has a clear narrative arc with a beginning, middle, and end.",
            "The analysis is 200-250 words long.",
            "The analysis identifies relevant ethical principles or frameworks.",
            "The analysis discusses potential long-term consequences of the technology's use.",
            "The analysis proposes at least one potential solution or regulation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
